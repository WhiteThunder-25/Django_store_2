from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy

from .forms import ProductForm
from .models import Product


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо за обращение, {name}!")

    return render(request,'contacts.html')


#def product_list(request):
    #products = Product.objects.all()
    #context = {'products': products}
    #return render(request, template_name='product_list.html', context=context)


#def product_details(request, pk):
    #product = get_object_or_404(Product, pk=pk)
    #context = {'product': product}
    #return render(request, template_name='product_detail.html', context=context)

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")