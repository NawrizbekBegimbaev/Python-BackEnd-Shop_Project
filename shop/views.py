from django.shortcuts import render
from shop.models import Shop
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy

    def form_valid(self, form):
        form.save()
        return render(self.success_url)

def shop_list(request):
    shops = Shop.objects.all()
    context = {
        'shops' : shops
    }
    return render(request,'list.html',context)

    def shop_cart(request):
        return self.cart

def shop_index(request,pk):
    shop = Shop.objects.get(id=pk)
    context = {
        'shop' : shop
    }
    return render(request,'index.html',context)

def cart_list(request):
    shops = Shop.objects.all()
    context = {
        'shops' : shops
    }
    return render(request,'cart.html',context)
def home(request):
    return render(request,'base.html',{})

def aboutus(request):
    return render(request,'aboutus.html',{})

def contact(request):
    return render(request,'contact.html',{})

def payment(request):
    return render(request,'payment.html',{})

class SearchView(ListView):
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Shop.objects.filter(
            Q(type__icontains=query) | Q(model__icontains=query)
        )
        return object_list