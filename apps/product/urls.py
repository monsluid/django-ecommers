from django.urls import path, include


from apps.product.views import CategoryList, CategoryNew, CategoryUpdate, CategoryDelete
from apps.product.views import BrandList, BrandNew, BrandUpdate, BrandDelete
from apps.product.views import StateList, StateNew, StateUpdate, StateDelete
from apps.product.views import ProductList, ProductNew, ProductUpdate, ProductDelete


# -------------------------------------------------------->
# Path Routers API

app_name = 'product'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Category

    path('brandList', BrandList.as_view(), name='brand_list'),
    path('brandNew', BrandNew.as_view(), name='brand_new'),
    path('brandUpdate/<int:pk>/', BrandUpdate.as_view(), name='brand_update'),
    path('brandDelete/<int:pk>/', BrandDelete.as_view(), name='brand_delete'),

    # -------------------------------------------------------->
    # Path Category

    path('categoryList', CategoryList.as_view(), name='category_list'),
    path('categoryNew', CategoryNew.as_view(), name='category_new'),
    path('categoryUpdate/<int:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('categoryDelete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),

    # -------------------------------------------------------->
    # Path State

    path('stateList', StateList.as_view(), name='state_list'),
    path('stateNew', StateNew.as_view(), name='state_new'),
    path('stateUpdate/<int:pk>/', StateUpdate.as_view(), name='state_update'),
    path('stateDelete/<int:pk>/', StateDelete.as_view(), name='state_delete'),

    # -------------------------------------------------------->
    # Path Product

    path('productList', ProductList.as_view(), name='product_list'),
    path('productNew', ProductNew.as_view(), name='product_new'),
    path('productUpdate/<str:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('productDelete/<str:pk>/', ProductDelete.as_view(), name='product_delete'),

]
