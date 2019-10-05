from django.db import models


CURRENCY_VALUE = (
  ('RUB', 'rub'),
  ('EUR', 'eur'),
  ('USD', 'usd')
)

class User(models.Model):
  name = models.CharField('Имя', max_length=50)
  lastname = models.CharField('Фамилия', max_length=50)
  patronymic = models.CharField('Отчество', max_length=50)
  full_name = models.CharField('Полное имя', max_length=200)
  email = models.CharField('email', max_length=100) 
  create_date = models.DateTimeField('Дата создания', auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    db_table = 'shop_users'
    verbose_name = "Пользователь"
    verbose_name_plural = "Пользователи"
    ordering = ["-create_date", "create_date"]


class CategoryProduct(models.Model):
  category_name = models.CharField('Имя категории', max_length=50)
  category_url = models.SlugField(
        'ЧПУ',
        db_index=True,
        unique=True)

  def __str__(self):
    return self.category_name

  class Meta:
    db_table = 'categories'
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

  
class Product(models.Model):
  category = models.ForeignKey(
        'CategoryProduct', 
        verbose_name='Категория продукта',
        to_field='category_url',
        on_delete=models.CASCADE,
        related_name='products')
  manufacturer = models.CharField('Производитель', max_length=50)
  product_name_model = models.CharField('Имя модели', max_length=50)
  manufacturer_date = models.DateField('Дата производства', null=True)
  product_color = models.CharField('Цвет товара', max_length=50)
  cost = models.DecimalField('Стоимость', max_digits=8, decimal_places=2)
  full_name_product = models.CharField('Полное имя продукта', max_length=200)
  currency = models.CharField(max_length=3, choices=CURRENCY_VALUE)

  def __str__(self):
    return self.manufacturer + ' ' + self.product_name_model

  class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'


class Order(models.Model):
  ORDER_STATUS_VALUE = (
    (False, 'canceled'),
    (True, 'active')
  )
  user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
  product = models.ManyToManyField(Product)
  count = models.IntegerField('Количество товара')
  comment_to_order = models.CharField('Комментарий к заказу', max_length=300)
  place_of_order = models.DateTimeField('Дата и время оформления заказа', auto_now=False, auto_now_add=True)
  order_status = models.BooleanField('Статус заказа', default=False, choices=ORDER_STATUS_VALUE)
  total_cost = models.DecimalField('Стоимость', max_digits=8, decimal_places=2)

  def __str__(self):
    return self.id

  class Meta:
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'


class UserWallet(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  state_wallet = models.DecimalField('Состояние счета', max_digits=8, decimal_places=2)
  currency = models.CharField(max_length=3, choices=CURRENCY_VALUE)
  edit_date = models.DateTimeField('Дата изменения счета', auto_now=True)

  def __str__(self):
    return self.user.name

  class Meta:
    verbose_name = 'Кошелек'
    verbose_name_plural = 'Кошельки'