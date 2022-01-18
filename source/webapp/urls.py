from django.urls import path
from .views import IndexView, it_and_software

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('it_and_software/', it_and_software, name='it_soft')


 ]