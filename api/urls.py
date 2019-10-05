from django.urls import path, include
from .views import OrderView, OrderFilterEmailView, UserView


urlpatterns = [
  path('api/v1/orders/', OrderView.as_view()),
  path('api/v1/order/<int:pk>', OrderView.as_view()),
  path('api/v1/orders/filter-email', OrderFilterEmailView.as_view()),
  path('api/v1/users/', UserView.as_view()),
  path('api/v1/user/<int:pk>', UserView.as_view())
]