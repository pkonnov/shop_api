from rest_framework import serializers
from .models import Order, User


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

  class Meta:
    model = Order
    fields = '__all__'


class OrderFilterEmailViewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'


class UserViewSerializer(serializers.ModelSerializer):

  def create(self, validate_data):
    return User.objects.create(**validate_data)

  def update(self, instance, validate_data):
    instance.name = validate_data.get('name', instance.name)
    instance.lastname = validate_data.get('lastname', instance.lastname)
    instance.patronymic = validate_data.get('patronymic', instance.patronymic)
    instance.full_name = validate_data.get('full_name', instance.full_name)
    instance.email = validate_data.get('email', instance.email)
    instance.save()
    return instance

  class Meta:
    model = User
    fields = '__all__' 







