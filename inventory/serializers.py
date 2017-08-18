from rest_framework import serializers
from .models import Product ,Location , Family , Transaction 

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location 
        fields = ('reference','title', 'description')


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family 
        fields = ('reference', 'title', 'description','unit','minQuantity')


class ProductSerializer(serializers.ModelSerializer):
     
    #location = serializers.HyperlinkedRelatedField(view_name="location_detail", read_only=True)
    #location = LocationSerializer()
    #family = serializers.HyperlinkedRelatedField(view_name="family_detail", read_only=True)
    #family = FamilySerializer()
    #location = serializers.HyperlinkedIdentityField(view_name="location_detail")
    #location = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Product 
        fields = ('id','url','sku','barcode', 'title', 'description' ,'unit','location','family')


class TransactionSerializer(serializers.ModelSerializer):
    
    #product = serializers.HyperlinkedRelatedField(view_name="product_detail", read_only=True)
    #product = ProductSerializer()
    class Meta:
        model = Transaction 
        fields = ('sku', 'barcode','product')
