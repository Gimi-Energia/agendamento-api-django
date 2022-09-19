from cProfile import label
from rest_framework import serializers

from agenda.models.periodic_agenda import Weekdays
from emails.models import Email
from departamento.models import Department

from .models import Agenda, PeriodicAgenda


class InnerEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'address']

class InnerDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class BaseAgendaSerializer(serializers.ModelSerializer):
    repeat_weekday = serializers.MultipleChoiceField(
        write_only=True,
        choices=PeriodicAgenda.WEEKDAY_CHOICES,
        label=PeriodicAgenda._meta.get_field('repeat_weekday').verbose_name,
        initial=[Weekdays.NONE],
        default=[Weekdays.NONE],
        allow_blank=True,
        allow_null=True,
        required=False,
    )

    creator_email = InnerEmailSerializer()
    creator_department = InnerDepartmentSerializer()

    class Meta:
        abstract = True
        model = Agenda
        fields = '__all__'

    @property
    def errors(self):
        """Exibe o verbose_name como nome do campo, ao exibir as mensagens de erro"""

        # get errors
        errors = super().errors
        verbose_errors = {}

        # fields = { field.name: field.verbose_name } for each field in model
        fields = {field.name: field.verbose_name for field in
                   self.Meta.model._meta.get_fields() if hasattr(field, 'verbose_name')}

        # iterate over errors and replace error key with verbose name if exists
        for field_name, error in errors.items():
            if field_name in fields:
                verbose_errors[str(fields[field_name])] = error
            else:
                verbose_errors[field_name] = error
        return verbose_errors

    def create(self, validated_data: dict):
        validated_data.pop('repeat_weekday', None)

        try:
            agenda = Agenda(**validated_data)
            agenda.save()
            return agenda
        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error, code=400)

    def update(self, instance, validated_data):
        try:
            return super(BaseAgendaSerializer, self).update(instance, validated_data)
        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error, code=400)


class AgendaSerializer(BaseAgendaSerializer):
    class Meta(BaseAgendaSerializer.Meta):
        read_only_fields = ('date_created', 'date_modified', 'code')


class AgendaNoCodeFieldSerializer(BaseAgendaSerializer):
    """Igual ao AgendaSerializer, porém não exibe o campo 'code'"""
    class Meta(BaseAgendaSerializer.Meta):
        read_only_fields = ('date_created', 'date_modified')
        exclude = ('code',)


class PeriodicAgendaSerializer(serializers.ModelSerializer):
    repeat_weekday = serializers.MultipleChoiceField(
        choices=PeriodicAgenda.WEEKDAY_CHOICES,
        label=PeriodicAgenda._meta.get_field('repeat_weekday').verbose_name,
        allow_blank=True,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = PeriodicAgenda
        fields = '__all__'

   
        

           
    