from django.urls import path

from products.views import ProductsView

pages_urls = [

]

api_urls = [
    path('get-for-select', ProductsView.as_view(), name='Получить все продукты для select'),
]
