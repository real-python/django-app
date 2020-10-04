from django.urls import path
from .import views

urlpatterns = [
    
    # path('employee/', views.employee, name='employee_url'),
    # path('student/', views.student, name='student_url'),

    path('', views.home_view, name='home_url'),
    path('create/', views.create_post, name="create_post_url"),
    path('signup/', views.signup_view, name='signup_url'),
    path('login/', views.login_view, name='login_url'),
    path('logout/', views.logout_view, name="logout_url"),

]