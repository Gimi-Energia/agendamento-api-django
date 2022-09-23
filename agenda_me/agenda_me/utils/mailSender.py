import smtplib, ssl, pytz
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from typing import Literal, Union, Callable
from dateutil import parser as dateparser

from emails.models import Email


class MailSender:
    def __init__(self, sender_email: str, password: Union[str, int], sender_email_alias: Union[str, None] = None) -> None:
        self.sender_email = sender_email or ""
        self.password = password
        self.sender_email_alias = sender_email_alias

    @property
    def sender_email(self) -> str:
        return self._sender_email

    @sender_email.setter
    def sender_email(self, email: str):
        self._sender_email = email


    def __get_delete_message(self, receiver_email: str, receiver_name: str, code: str, data: dict):
        """
            Retorna a mensagem para o corpo do email,
            indicando que o agendamento foi excluído.
        """

        message = MIMEMultipart("alternative")
        message["Subject"] = "GIMI - Seu código de agendamento de reunião."
        message["From"] = self.sender_email_alias or self.sender_email
        message["To"] = receiver_email

        html = f"""
        <html>
            <head>
                <style>
                    p {'{ font-size: 1rem; }'}
                </style>
            </head>
            <body>
                <div id="container">
                    Seu agendamento foi excluído com sucesso.
                </div>
            </body>
        </html>
        """
        message.attach(MIMEText(html, "html"))

        return message
        

    def __get_info_message(self, receiver_email: str, receiver_name: str, code: str, data: dict):
        """
            Retorna a mensagem para o corpo do email,
            indicando as informações do agendamento.
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = "GIMI - Seu código de agendamento de reunião."
        message["From"] = self.sender_email_alias or self.sender_email
        message["To"] = receiver_email

        tz = pytz.timezone('America/Sao_Paulo')
        date = dateparser.parse(data.get('schedule_date_init')).replace(tzinfo=tz).date().strftime('%d-%m-%Y')
        time_init = dateparser.parse(data.get('schedule_date_init')).replace(tzinfo=tz).time().strftime('%H:%M')
        time_end =dateparser.parse(data.get('schedule_date_end')).replace(tzinfo=tz).time().strftime('%H:%M')

        html = f"""
        <html>
            <head>
                <style>
                    p {'{ font-size: 1rem; }'}
                </style>
            </head>
            <body>
                <div id="container">
                    <p>
                        Olá, {receiver_name}
                        <br>
                        Segue abaixo os dados do seu agendamento:
                        <br>
                        <br> 
                    </p>
                    <ul>
                        <li><b>Assunto Reunião:</b> {data.get('schedule_title')}</li>
                        <li><b>Setor:</b> {data.get('schedule_department')}</li>
                        <li><b>Data:</b> {date}</li>
                        <li><b>Hora:</b> {time_init} até {time_end}</li>
                        <li><b>Código Agendamento:</b> {code}</li>
                    </ul>
                    <br>
                    <h3><b>IMPORTANTE:</b></h3>
                    <p><b>Em caso de necessidade de cancelamento da reunião, siga os passos abaixo:</b><br></p>
                    <ol>
                        <li>Copie o código acima</li>
                        <li>Vá até a data agendada e marque a opção "Ver Horários Agendados"</li>
                        <li>Clique no botão EXCLUIR</li>
                        <li>Se tudo deu certo, você verá a seguinte mensagem na tela: "Agendamento removido com sucesso." (aperte F5 para atualizar a página)</li>
                    </ol>

                </div>
            </body>
        </html>
        """
        message.attach(MIMEText(html, "html"))

        return message


    def __connect_to_smtp_server_and_send_mail(
        self,
        server_host: str,
        server_port: int,
        receiver_email: str,
        message: str,
        has_ssl: Union[bool, None] = None,
        tls: Union[bool, None] = None,
    ) -> Literal['success', 'failure']:
        """Realiza uma conexão SMTP e envia um email."""

        SMTP_HANDLER = smtplib.SMTP_SSL if has_ssl else smtplib.SMTP
        smtp_kwargs = { 'host': server_host, 'port': server_port }

        ssl_context = ssl.create_default_context()
        if has_ssl:
            smtp_kwargs['context'] = ssl_context

        with SMTP_HANDLER(**smtp_kwargs) as server:
            if tls:
                server.starttls(context=ssl_context)

            server.login(self.sender_email, self.password)
            server.sendmail(
                from_addr=self.sender_email_alias or self.sender_email,
                to_addrs=receiver_email,
                msg=message
            )
        return 'success'


    def send_via_gmail(self, to: str, name: str, code: str, **kwargs) -> None:
        '''
            Envia um email com o código de agendamento utilizando o servidor SMTP do Gmail.\n

            [to]: email do destinatário\n
            [name]: nome do destinatário\n
            [code]: código do agendamento, o mesmo código deve ser salvo no banco de dados
        '''
        receiver_email: str = kwargs.get('to', to)
        receiver_name: str = kwargs.get('name', name)

        message = self.__get_info_message(receiver_email, receiver_name, code)

        self.__connect_to_smtp_server_and_send_mail(
            server_host='smtp.gmail.com',
            server_port=465,
            has_ssl=True,
            receiver_email=receiver_email,
            message=message.as_string(),
        )


    def send_via_outlook(self, to: str, name: str, code: str, data: dict, message_type: Literal['info', 'delete'], **kwargs) -> None:
        '''
            Envia um email com o código de agendamento utilizando o servidor SMTP do Outlook.\n

            [to]: email do destinatário\n
            [name]: nome do destinatário\n
            [code]: código do agendamento, o mesmo código deve ser salvo no banco de dados
        '''

        receiver_email: Union[str, Email] = kwargs.get('to', to)
        if isinstance(receiver_email, Email):
            receiver_email = receiver_email.address

        receiver_name: str = kwargs.get('name', name)
        msg_data: dict = kwargs.get('data', data)

        messages: dict[str, Callable] = {
            'info': self.__get_info_message,
            'delete': self.__get_delete_message 
        }

        print(message_type, receiver_email, receiver_name, code, msg_data)
        try:
            message = messages[message_type](receiver_email, receiver_name, code, data=msg_data)
        except KeyError as e:
            raise KeyError('Informe um tipo válido de mensagem.')

        self.__connect_to_smtp_server_and_send_mail(
            server_host='smtp-mail.outlook.com',
            server_port=587,
            tls=True,
            receiver_email=receiver_email,
            message=message.as_string(),
        )
    