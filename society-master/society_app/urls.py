from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.h_login, name="h_login"),

    path('admin-home/', views.admin_home, name="admin_home"),
    path('admin-login/', views.admin_login, name="admin_login"),

    path('member-register/', views.member_register, name="member_register"),
    path('member-login/', views.member_login, name="member_login"),
    path('logout/', views.logoutUser, name="logout"),

    path('member/<str:pk>/', views.member, name="member"),
    path('a-member/<str:pk>/', views.a_member, name="a_member"),
    path('member-update/<str:pk>/', views.member_update, name="member_update"),
    path('a-update/<str:pk>/', views.a_update, name="a_update"),
    path('member-delete/<str:pk>/', views.delete_member, name="delete_member"),
    path('members/', views.members, name="members"),

    path('file-complaint/', views.file_complaint, name="file_complaint"),
    path('members-complaint/<str:username>/', views.member_complaints, name="member_complaints"),
    path('delete-complaint/<int:pk>/', views.delete_complaint, name="delete_complaint"),
    path('admin-complaints/', views.admin_complaints, name="admin_complaints"),

    path('m-maintenance/<str:username>/', views.m_maintenance, name="m_maintenance"),
    path('maintenance/', views.maintenance, name="maintenance"),
]