from django.shortcuts import render

# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Models
from inventory.models import Supplier as SupplierModel

# Serializers
from inventory.serializers import SupplierSerializer

@api_view(['GET'])
def get_suppliers(request):

    if request.method == 'GET':
        suppliers = SupplierModel.objects.all()

        serialized_suppliers = SupplierSerializer(suppliers, many=True)
        return Response(serialized_suppliers.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_suppliers_name(request, name):
    try:
        name_supplier = SupplierModel.objects.get(name=name)
    except SupplierModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        supplier = SupplierSerializer(name_supplier)
        return Response(supplier.data)

@api_view(['POST'])
def create_suppliers(request):

    if request.method == 'POST':
        serializer_supplier = SupplierSerializer(data=request.data)
        if serializer_supplier.is_valid():
            serializer_supplier.save()
            return Response(serializer_supplier.data, status=status.HTTP_201_CREATED)
    return Response(serializer_supplier.errors, status=status.HTTP_400_BAD_REQUEST)