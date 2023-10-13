from django.urls import path

from maps.views import AdminMapsView

pages_urls = [

]

api_urls = [
    path('', AdminMapsView.as_view(), name='Получить все метки'),
    path('add-marker', AdminMapsView.as_view(), name='Добавить метку'),
]

