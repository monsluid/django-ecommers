from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.staff.views import StaffList, StaffNew, StaffUpdate, StaffDelete, StaffDetail

from apps.staff.views import UserList, UserCreate, UserUpdate, UserDelete


app_name = 'staff'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Staff

    path('staffList', StaffList.as_view(), name='staff_list'),
    path('staffNew', StaffNew.as_view(), name='staff_new'),
    path("staffEdit/<str:pk>/", StaffUpdate.as_view(), name='staff_update'),
    path('staffDelete/<str:pk>/', StaffDelete.as_view(), name='staff_delete'),
    path('staffDetail/<str:pk>/', StaffDetail.as_view(), name='staff_detail'),

    # -------------------------------------------------------->
    # Path User

    path('userList/', UserList.as_view(), name='user_list'),
    path('userNew/', UserCreate.as_view(), name='user_new'),
    path('userEdit/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('userDelete/<int:pk>/', UserDelete.as_view(), name='user_delete'),

]
