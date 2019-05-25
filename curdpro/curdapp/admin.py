from django.contrib import admin
from .models import ProductData
class AdminProductData(admin.ModelAdmin):
    list_display = ['product_id',
                    'product_name',
                    'product_cost',
                    'product_color',
                    'product_class',
                    'customer_name',
                    'customer_mobile',
                    'customer_email'
                    ]
admin.site.register(ProductData,AdminProductData)#indentation in this line