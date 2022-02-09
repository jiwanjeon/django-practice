from django.urls import path

from .views import ProductListView

#product/urls.py 위치
#http://127.0.0.1:8000/products

urlpatterns = [
	#http://127.0.0.1:8000/products
	path("", ProductListView.as_view())
]
