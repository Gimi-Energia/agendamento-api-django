from emails.views import EmailViewSet
from rest_framework import routers

email_routes = routers.DefaultRouter()

email_routes.register('', EmailViewSet, basename="department_viewset")