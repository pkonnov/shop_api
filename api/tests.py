from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from api.views import *
from api.models import CategoryProduct
import json


factory = APIRequestFactory()

class ProductTestCase(TestCase):

  # def test_get_list_product(self):
  #   request = self.client.get('/api/v1/products/')
  #   self.assertEqual(request.status_code, 200)

  # def test_create_product(self):
  #   data = {
  #     "product": {
  #           "manufacturer": "Nokia",
  #           "product_name_model": "6212",
  #           "product_color": "Green",
  #           "cost": "5645.00",
  #           "full_name_product": "Nokia 6312 Blue",
  #           "currency": "RUB",
  #           "category": "mobily"
  #       }
  #   }
  #   response = self.client.post('/api/v1/products/', json.dumps(data), content_type='application/json')
  #   self.assertEqual(response.data, {'success': 'product create'})


  def test_update_product(self):

    data = {
      "product": {
            "manufacturer": "Nokia",
            "product_name_model": "6212",
            "product_color": "Green",
            "cost": "545.00",
            "full_name_product": "Nokia 6312 Blue",
            "currency": "RUB",
            "category": "mobily"
      }
    }
    response = self.client.put('/api/v1/product/3', json.dumps(data), content_type='application/json')
    self.assertEqual(response.data, {'success': 'product update'})


  # def test_create_product(self):
  #   data = {
  #     "category": {
  #           "category_name": "newspaper",
  #           "category_url": "newspaper"
  #       }
  #   }
  #   response = self.client.post('/api/v1/categories/', json.dumps(data), content_type='application/json')
  #   self.assertEqual(response.data, {'success': 'category create'})