from django.urls import path

from . import views

app_name = 'alerts'
urlpatterns = [
    # ex: /alerts/checkAbnormalReading/1/
    # path('checkAbnormalReading/<int:patient_id>/', views.checkAbnormalReading, name='checkAbnormalReading'),
]