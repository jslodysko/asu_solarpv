from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Certificate, Service
from .serializers import ProductSerializer, CertificateSerializer, ServiceSerializer

# Create your views here.
#def index(request):
#    return render(request, 'main/index.html')

#def registration(request):
#    return render(request, 'main/registration.html')

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer