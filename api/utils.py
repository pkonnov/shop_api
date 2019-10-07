from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class InstanceGetListMxixin:

  model = None
  name_model = None
  name_instance = None
  serializer_class = None
  name_data_from_req = None
  
  def get(self, request, *args, **kwargs):
    self.name_instance = self.model.objects.all()
    serializer = self.serializer_class(self.name_instance, many=True)
    return Response({f'{self.name_model}': serializer.data})


class InstanceCreateMixin:

  name_model = None
  name_instance = None
  serializer_class = None
  name_data_from_req = None

  def post(self, request):
    self.name_instance = request.data.get(self.name_data_from_req)
    serializer = self.serializer_class(data=self.name_instance)
    print(serializer)
    if serializer.is_valid():
      validate_data = serializer.save()
      return Response({'success': f'{self.name_model} create'})
    return Response({'error': '¯\＿(ツ)＿/¯'})
  

class InstanceUpdateMixin:

  model = None
  name_model = None
  name_instance = None
  serializer_class = None
  name_data_from_req = None
  
  def put(self, request, pk):
    self.name_instance = get_object_or_404(self.model.objects.all(), pk=pk)
    data = request.data.get(self.name_data_from_req)
    serializer = self.serializer_class(instance=self.name_instance, data=data, partial=True)
    print(serializer.is_valid())
    if serializer.is_valid():
      validate_data = serializer.save()
      return Response({'success': f'{self.name_model} update'})
    return Response({'error': '¯\＿(ツ)＿/¯'})


class InstanceDeleteMixin:
  
  model = None
  name_model = None
  name_instance = None
  serializer_class = None
  name_data_from_req = None

  def delete(self, request, pk):
    self.name_instance = get_object_or_404(self.model.objects.all(), pk=pk)
    self.name_instance.delete()
    return Response({'success': f'{self.name_model} with id={pk} delete'})


def replace_rus_to_eng(string):
	dic = {'Ь':'', 'ь':'', 'Ъ':'', 'ъ':'', 'А':'A', 'а':'a', 'Б':'B', 'б':'b', 'В':'V', 'в':'v',
	'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Е':'E', 'е':'e', 'Ё':'E', 'ё':'e', 'Ж':'Zh', 'ж':'zh',
	'З':'Z', 'з':'z', 'И':'I', 'и':'i', 'Й':'I', 'й':'i', 'К':'K', 'к':'k', 'Л':'L', 'л':'l',
	'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o', 'П':'P', 'п':'p', 'Р':'R', 'р':'r', 
	'С':'S', 'с':'s', 'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f', 'Х':'Kh', 'х':'kh',
	'Ц':'Tc', 'ц':'tc', 'Ч':'Ch', 'ч':'ch', 'Ш':'Sh', 'ш':'sh', 'Щ':'Shch', 'щ':'shch', 'Ы':'Y',
	'ы':'y', 'Э':'E', 'э':'e', 'Ю':'Iu', 'ю':'iu', 'Я':'Ia', 'я':'ia'}
       
	alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о','П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч','Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']
	len_st = len(string)
	result = ''
	for i in range(0,len_st):
		if string[i] in alphabet:
			simb = dic[string[i]]
		else:
			simb = string[i]
		result = result + simb
	return result