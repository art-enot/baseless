from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),

    path('add_product', views.add_product, name="add_product"),

    path('product/<str:product_id>', views.product, name="product"),

    path('edit_product', views.edit_product, name="edit_product"),

    path('delete_product/<str:product_id>', views.delete_product, name="delete_product"),
]
