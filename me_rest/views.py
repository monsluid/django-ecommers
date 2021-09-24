from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView
from apps.product.models import Category, Brand, State, Product


# -----------------------------------------------------------------
# Admin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "./home/home.html"


# -----------------------------------------------------------------
# Web

class IndexView(TemplateView):
    template_name = "./web/index.html"



