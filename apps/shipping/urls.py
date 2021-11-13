from django.urls import path

from apps.shipping.views import ShippingList, ShippingProductDetail, Cart


# -------------------------------------------------------->
# Path Routers API

app_name = 'shipping'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Gallery
    
    path('', ShippingList.as_view(), name='shipping_list'),
    path('product/<pk>', ShippingProductDetail.as_view(), name='product-detail'),
    path('cart', Cart.as_view(), name='cart'),

]
