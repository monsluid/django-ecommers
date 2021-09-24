from apps.product.models import Category, Brand, State, Product
from apps.product.forms import CategoryForm, BrandForm, StateForm, ProductForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

# ------------------------------------------------------------------------------------>
# view Brand

class BrandList(ListView):
    model = Brand
    template_name = 'product/brand/brand_list.html'
    context_object_name = 'brand_list'
    queryset = Brand.objects.all()


class BrandNew(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'product/brand/brand_form.html'
    success_url = reverse_lazy('product:brand_list')


class BrandUpdate(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'product/brand/brand_form.html'
    success_url = reverse_lazy('product:brand_list')


class BrandDelete(DeleteView):
    model = Brand
    form_class = BrandForm
    template_name = 'product/brand/brand_confirm_delete.html'
    success_url = reverse_lazy('product:brand_list')


# ------------------------------------------------------------------------------------>
# view Category

class CategoryList(ListView):
    model = Category
    template_name = 'product/category/category_list.html'
    context_object_name = 'category_list'
    queryset = Category.objects.all()


class CategoryNew(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/category/category_form.html'
    success_url = reverse_lazy('product:category_list')


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/category/category_form.html'
    success_url = reverse_lazy('product:category_list')


class CategoryDelete(DeleteView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/category/category_confirm_delete.html'
    success_url = reverse_lazy('product:category_list')


# ------------------------------------------------------------------------------------>
# view State

class StateList(ListView):
    model = State
    template_name = 'product/state/state_list.html'
    context_object_name = 'state_list'
    queryset = State.objects.all()


class StateNew(CreateView):
    model = State
    form_class = StateForm
    template_name = 'product/state/state_form.html'
    success_url = reverse_lazy('product:state_list')


class StateUpdate(UpdateView):
    model = State
    form_class = StateForm
    template_name = 'product/state/state_form.html'
    success_url = reverse_lazy('product:state_list')


class StateDelete(DeleteView):
    model = State
    form_class = StateForm
    template_name = 'product/state/state_confirm_delete.html'
    success_url = reverse_lazy('product:state_list')


# ------------------------------------------------------------------------------------>
# view product

class ProductList(ListView):
    model = Product
    template_name = 'product/product/product_list.html'
    context_object_name = 'product_list'
    queryset = Product.objects.all()


class ProductNew(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product/product_form.html'
    success_url = reverse_lazy('product:product_list')


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product/product_form.html'
    success_url = reverse_lazy('product:product_list')


class ProductDelete(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product/product_confirm_delete.html'
    success_url = reverse_lazy('product:product_list')



