from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show-modal/', views.show_modal, name='show-modal'),
    path('button/', views.show_button),
    path('employees/', views.employee_list, name='employee-list'),
    path('employee-add', views.employee_add, name='employee-add'),
    path('employee-edit/<pk>/', views.employee_edit, name='employee-edit'),
    path('employee-delete/<pk>/', views.employee_delete, name='employee-delete'),
]