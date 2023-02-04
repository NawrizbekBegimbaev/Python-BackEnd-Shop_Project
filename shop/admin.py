from django.contrib import admin
from shop.models import Shop

#@admin.register(Quote)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','type','price','description','digital','cart')
    list_display_links = ('type',)

admin.site.register(Shop,ShopAdmin)
