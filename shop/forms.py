from django.forms import ModelForm
from shop.models import Shop

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'