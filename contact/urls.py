from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('submissions/', views.submissions, name='submissions'),
    path('update_submission/<int:pk>', views.update_submission, name='update_submission'),
    path('delete_submission/<int:pk>', views.delete_submission, name='delete_submission'),
]
