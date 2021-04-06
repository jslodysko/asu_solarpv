from rest_framework import serializers
from .models import Product, Certificate, Service

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('cell_manufacturer','cell_technology','encapsulation_manufacturer','encapsulation_type','frame_adhesive','frame_type','junction_box_manufacturer','junction_box_type','model_number','number_of_cells','number_of_cells_in_series','number_of_diodes','number_of_series_strings','product_length','product_name','product_weight','product_width','substrate_type','substrate_manufacturer','superstrate_type','superstrate_type')

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('certification_number','cert_id','issue_date','model_number','report_number','standard_id','userID')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('description','FI_frequency','is_FI_required','service_id','service_name','standard_id')