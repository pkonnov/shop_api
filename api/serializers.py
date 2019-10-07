from rest_framework import serializers
from .models import Order, User, CategoryProduct, Product, UserWallet


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


class CategoryProductViewSerializer(serializers.ModelSerializer):

  def create(self, validate_data):
    return CategoryProduct.objects.create(**validate_data)

  def update(self, instance, validate_data):
    instance.category_name = validate_data.get('category_name', instance.category_name)
    instance.category_url = validate_data.get('category_url', instance.category_url)
    instance.save()
    return instance

  class Meta:
    model = CategoryProduct 
    fields = '__all__'


class ProductViewSerializer(serializers.ModelSerializer):

  def create(self, validate_data):
    return Product.objects.create(**validate_data)

  def update(self, instance, validate_data):
    instance.manufacturer = validate_data.get('manufacturer', instance.manufacturer)
    instance.product_name_model = validate_data.get('product_name_model', instance.product_name_model)
    instance.manufacturer_date = validate_data.get('manufacturer_date', instance.manufacturer_date)
    instance.product_color = validate_data.get('product_color', instance.product_color)
    instance.cost = validate_data.get('cost', instance.cost)
    instance.full_name_product = validate_data.get('full_name_product', instance.full_name_product)
    instance.currency = validate_data.get('currency', instance.currency)
    instance.category = validate_data.get('category', instance.category)
    # for key in validate_data:
    #   print(instance['manufacturer'])
    #   instance[key] = validate_data.get(i, instance[key])
    #   instance.save()
    instance.save()
    return instance

  class Meta:
    model = Product
    fields = '__all__'


class UserWalletViewSerializer(serializers.ModelSerializer):

  def update(self, instance, validate_data):
    instance.state_wallet = validate_data.get('state_wallet', instance.state_wallet)
    instance.currency = validate_data.get('currency', instance.currency)
    instance.save()
    return instance

  class Meta:
    model = UserWallet
    fields = '__all__'