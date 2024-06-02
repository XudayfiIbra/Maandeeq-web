from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('api/product/', views.Products, name='api_product'),
    path('api/product/<int:id>/', views.Product_info, name='product_info'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)