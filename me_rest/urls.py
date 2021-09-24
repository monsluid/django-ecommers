from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView

from me_rest.views import HomeView, IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('staff/', include('apps.staff.urls')),
    path('product/', include('apps.product.urls')),
    path('shipping/', include('apps.shipping.urls')),

]


if settings.DEBUG:
	from django.conf.urls.static import static

	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

