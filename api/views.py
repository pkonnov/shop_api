from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Order, User, CategoryProduct, Product, UserWallet
from .serializers import OrderViewSerializer, OrderFilterEmailViewSerializer, UserViewSerializer, CategoryProductViewSerializer, ProductViewSerializer, UserWalletViewSerializer
from .utils import *
import datetime


class OrderView(APIView):

  def get(self, request, *args, **kwargs):
    orders = Order.objects.all()
    serializer = OrderViewSerializer(orders, many=True)
    return Response({'orders': serializer.data})

  def post(self, request):
    order = request.data.get('order')
    date_now = datetime.datetime.now()
    orders_today_one_addr = Order.objects.filter(place_of_order__date=date_now).filter(mailing_addr_user=order['mailing_addr_user'])
    if len(orders_today_one_addr) > 5:
      return Response({'error': f'Created > 5 orders with one addr'})

    serializer = OrderViewSerializer(data=order)
    if serializer.is_valid(raise_exception=True):
      order_saved = serializer.save()
    return Response({'success': f'Order {order_saved.id} created'})

  def put(self, request, pk):
    # update order status
    data = request.data.get('order_status')
    if data == 'True' or data == 'False':
      obj, created = Order.objects.update_or_create(
          pk=pk,
          defaults={'order_status': data}
      )
      return Response({'success': f'order update status {obj.id}'})
    return Response({'error': 'invalid data'})
  

# get orders in email
class OrderFilterEmailView(APIView):

  def get(self, request, *args, **kwargs):
    email = request.data.get('email')
    orders = Order.objects.all()
    orders_filter_email = orders.filter(user__email=email)
    serializer = OrderFilterEmailViewSerializer(orders_filter_email, many=True)
    if len(serializer.data) > 0:
      return Response({'orders with such email': serializer.data})
    return Response({'error': 'with such email not orders'})


class UserView(APIView):
  
  def get(self, request, *args, **kwargs):
    users = User.objects.all()
    serializer = UserViewSerializer(users, many=True)
    return Response({'users': serializer.data})
  
  def post(self, request):
    user = request.data.get('user')
    serializer = UserViewSerializer(data=user)
    email = serializer.initial_data['email']
    isEmailAlreadyExist = True if len(User.objects.filter(email=email)) > 0 else False
    if isEmailAlreadyExist:
      return Response({'error': f'User with such email {email} already exist'})
    if serializer.is_valid(raise_exception=True):
      user = serializer.save()
      return Response({'success': f'User with id={user.id} create'})
    return Response({'error': 'invalid data'})

  def put(self, request, pk):
    update_user = get_object_or_404(User.objects.all(), pk=pk)
    data = request.data.get('user')
    serializer = UserViewSerializer(instance=update_user, data=data, partial=True)
    if serializer.is_valid():
      user = serializer.save()
      return Response({'success': f'User with id={user.id} update'})
    return Response({'error': '¯\＿(ツ)＿/¯'})

  def delete(self, request, pk):
    delete_user = get_object_or_404(User.objects.all(), pk=pk)
    delete_user.delete()
    return Response({'success': f'User with id={pk} delete'})


class CategoryProductView(APIView, 
                          InstanceGetListMxixin, 
                          InstanceCreateMixin, 
                          InstanceUpdateMixin, 
                          InstanceDeleteMixin):

  model = CategoryProduct
  name_model = 'category'
  name_instance = 'category'
  name_data_from_req = 'category'
  serializer_class = CategoryProductViewSerializer 


class ProductView(APIView, 
                    InstanceGetListMxixin, 
                    InstanceCreateMixin, 
                    InstanceUpdateMixin,
                    InstanceDeleteMixin):

  model = Product
  name_model = 'product'
  name_instance = 'product'
  name_data_from_req = 'product' 
  serializer_class = ProductViewSerializer


class UserWalletView(APIView, 
                    InstanceGetListMxixin, 
                    InstanceCreateMixin, 
                    InstanceUpdateMixin,
                    InstanceDeleteMixin):
                    
  model = UserWallet 
  name_model = 'user_wallet'
  name_instance = 'user_wallet'
  name_data_from_req = 'user_wallet' 
  serializer_class = UserWalletViewSerializer
