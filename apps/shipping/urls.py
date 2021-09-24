from django.urls import path

from apps.shipping.views import ShippingList, ShippingNew, Shipping


# -------------------------------------------------------->
# Path Routers API

app_name = 'shipping'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Gallery
    
    path('shippingList', ShippingList.as_view(), name='shipping_list'),
    path('shippingNew', ShippingNew.as_view(), name='shipping_new'),
    path('shippin/<int:pk>/', Shipping.as_view(), name='shipping'),
]
