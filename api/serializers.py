from rest_framework import serializers
from .models import Order


class OrderViewSerializer(serializers.ModelSerializer):

  def create(self, validate_data):
    mailing_addr_user = validate_data['mailing_addr_user']
    count = validate_data['count']
    order_status = validate_data['order_status']
    total_cost = validate_data['total_cost']
    user = validate_data['user']
    products = validate_data['product']
    order = Order.objects.create(
      mailing_addr_user=mailing_addr_user,
      count=count, order_status=order_status,
      total_cost=total_cost,
      user=user)
    for p in products:
      order.product.add(p)
    return order

  # def update(self, instance, validate_data):
  #   print(instance)
  #   instance.order_status = validate_data.get('order_status', instance.order_status)
  #   instance.save()
  #   return instance

  class Meta:
    model = Order
    fields = '__all__'

# >> order = Order.objects.create(mailing_addr_user='городfdfd Саратов fdfул Чернышевского кв 5', count=2, order_status=True, total_cost=9100.00, user_id=1)
# >>> order.product.add(1)

class OrderFilterEmailViewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'