from django.urls import path, include
from .views import OrderView, OrderFilterEmailView, UserView, CategoryProductView, ProductView, UserWalletView


urlpatterns = [
  path('api/v1/orders/', OrderView.as_view()),
  path('api/v1/order/<int:pk>', OrderView.as_view()),
  path('api/v1/orders/filter-email', OrderFilterEmailView.as_view()),
  path('api/v1/users/', UserView.as_view()),
  path('api/v1/user/<int:pk>', UserView.as_view()),
  path('api/v1/categories/', CategoryProductView.as_view()),
  path('api/v1/category/<int:pk>', CategoryProductView.as_view()),
  path('api/v1/products/', ProductView.as_view()),
  path('api/v1/product/<int:pk>', ProductView.as_view()),
  path('api/v1/user_wallets/', UserWalletView.as_view()),
  path('api/v1/user_wallet/<int:pk>', UserWalletView.as_view())
]