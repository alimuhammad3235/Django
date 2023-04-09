from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from products.serializer import ProductSerializer
from products.models import product

# Create your views here.
class ListproductAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class CreateproductAPIView(CreateAPIView):
    """This endpoint allows for creation of a product"""
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class UpdateproductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific product by passing in the id of the product to update"""
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class DeleteproductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific product from the database"""
    queryset = product.objects.all()
    serializer_class = ProductSerializer
def index(request):
    htmlpage='''<table>
  <tr>
    <th>Firstname</th>
    <td>Jill</td>
    <td>Eve</td>
  </tr>
  <tr>
    <th>Lastname</th>
    <td>Smith</td>
    <td>Jackson</td>
  </tr>
  <tr>
    <th>Age</th>
    <td>94</td>
    <td>50</td>
  </tr>
</table>'''
    return HttpResponse(htmlpage)
