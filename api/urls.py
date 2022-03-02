from django.urls import path
from .views.account_views import AccountsView, AccountDetailView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = [
  	# Restful routing
    path('accounts/', AccountsView.as_view(), name='accounts'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account_detail'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-pw/', ChangePasswordView.as_view(), name='change-pw')
]
