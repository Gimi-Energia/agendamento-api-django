import os
import pytz
from datetime import datetime, timedelta

from django.db import models
from agenda.models.agenda_base import AgendaBase
from agenda.models.periodic_agenda import PeriodicAgenda
from emails.models import Email
from agenda_me.utils import MailSender

from dateutil import parser as dateparser


class Agenda(AgendaBase):
    date_init = models.DateTimeField(blank=False, null=True, verbose_name="Data/Hora de início")
    date_end = models.DateTimeField(blank=True, null=True, verbose_name="Data/Hora de término")
    must_repeat = models.BooleanField(default=False, verbose_name="Reunião se repete?", blank=True)
    periodic_agenda = models.ForeignKey(PeriodicAgenda, null=True, blank=True, on_delete=models.CASCADE)

    def send_code_email(self, receiver_email, receiver_name, code, schedule_data):
        """Tenta enviar o email com o código de segurança para a pessoa que agendou"""

        mail = MailSender(
            os.getenv('EMAIL_SENDER_ADDRESS'),
            os.getenv('EMAIL_SENDER_PASSWORD'),
            sender_email_alias='Reuniao GIMI <reuniao@gimi.com.br>'
        )
        mail.send_via_outlook(
            to=receiver_email,
            name=receiver_name,
            code=code,
            data=schedule_data
        )
        print(f'[!] Code email sended to <{receiver_email}>, from <{mail.sender_email}> at {datetime.now()} [!]')

    def save(self, *args, **kwargs):
        if not kwargs.pop('ignore_time_rule', False):
            tz = pytz.timezone('America/Sao_Paulo')
            init_datetime = dateparser.parse(str(self.date_init))
            print('INICIO DA REUNIAO CRIADA (string antes do parser):', self.date_init)
            print('INICIO DA REUNIAO CRIADA (depois do parser):', init_datetime)
            print('AGORA SAO:', datetime.now(tz))
            if (init_datetime < datetime.now(tz) + timedelta(minutes=2.5)): # tolerância de 2 minutos e meio de atraso ao agendar
                raise ValueError('Agende um horário a partir de agora.')

        periodic_agenda = kwargs.pop('periodic_agenda', None)
        code = kwargs.pop('code', None)

        # TODO: self.duplicado() tem que verificar se não há alguma agenda periódica marcada para esse dia
        if (self.duplicado(Agenda) > 0):
            raise ValueError('Sala já em uso nesse dia e horário.')
        elif (not os.getenv('EMAIL_SENDER_ADDRESS')) or (not os.getenv('EMAIL_SENDER_PASSWORD')):
            raise ValueError('Não foi possível enviar um email de confirmação ao usuário.')
        else:
            # Só executar quando o dado está sendo criado no banco
            if not self.id:
                receiver_email: str = self.creator_email.address
                receiver_name: str = self.created_by
                schedule_data = {
                    'schedule_title': self.titulo,
                    'schedule_department': self.creator_department.name,
                    'schedule_date_init': self.date_init,
                    'schedule_date_end': self.date_end
                }

                # Código gerado automaticamente e salvo na instancia.
                code = code or self.generate_code(receiver_name=receiver_name)
                self.code = code

                # Envia o email com o <code> ao <receiver_email> 
                try:
                    self.send_code_email(
                        receiver_email,
                        receiver_name,
                        code,
                        schedule_data,
                    )
                except Exception as e:
                    print('Error sending email:', e)
                    raise ConnectionError('Erro de conexão ao enviar o email de confirmação. Tente novamente.')

            # Só executar quando for editar
            if self.id:
                pass
                
            super(Agenda, self).save(*args, **kwargs)
