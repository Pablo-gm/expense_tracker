from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.registration_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('account/', views.account_view, name="account"),

    # Custom password reset views
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Budgets views
    path('budgets/', views.budgets, name="budgets"),
    path('view_budget/<str:budget_id>', views.view_budget, name="view_budget"),
    path('delete_budget/<str:budget_id>', views.delete_budget, name="delete_budget"),
    path('create_budget/', views.create_budget, name="create_budget"),
]