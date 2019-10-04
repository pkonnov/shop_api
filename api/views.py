from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Order
from .serializers import OrderViewSerializer, OrderFilterEmailViewSerializer
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

# class OrderChangeStatusView(APIView):

#   def update(self, request):