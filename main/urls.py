from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Product', views.ProductView)
router.register('Certificate', views.CertificateView)
router.register('Service', views.ServiceView)

urlpatterns = [
    path('', include(router.urls))
    #path('', views.index, name='index'),
    #path('registration/', views.registration, name='registration')
    #path('product/', views.product, name='product')
]