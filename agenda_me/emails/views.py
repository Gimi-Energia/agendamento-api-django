from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from emails.models import Email
from emails.serializers import EmailSerializer

from user.models import User

class EmailPagination(PageNumberPagination):
    page_size = 25
    page_query_param = 'page'
    max_page_size = 100

class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    pagination_class = EmailPagination

    def get_queryset(self):
        user: User = self.request.user
        qset = Email.objects.filter(company=user.company)
        if (self.request.GET.get('address', None)):
            qset = qset.filter(
                address__icontains=self.request.GET.get('address')
            )
        return qset.order_by('address')

