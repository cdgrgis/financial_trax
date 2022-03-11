from django.urls import path
from .views.fund_views import FundsView, FundDetailView
from .views.account_views import AccountsView, AccountDetailView
from .views.fund_info_views import FundInfosView, FundInfoDetailView, AccountFundInfosView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = [
  	# Restful routing
    path('accounts/', AccountsView.as_view(), name='accounts'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account_detail'),
    path('accounts/<int:pk>/fund-infos/', AccountFundInfosView.as_view(), name='account_fund_infos'),
    path('funds/', FundsView.as_view(), name='funds'),
    path('funds/<int:pk>/', FundDetailView.as_view(), name='fund_detail'),
    path('fund-infos/', FundInfosView.as_view(), name='fundinfos'),
    path('fund-infos/<int:pk>/', FundInfoDetailView.as_view(), name='fund_info_detail'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-pw/', ChangePasswordView.as_view(), name='change-pw')
]
