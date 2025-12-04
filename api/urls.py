from django.urls import path
from .views import StoreViewSets

urlpatterns = [
    path('store/',StoreViewSets.as_view({'get': 'list','post':'create'})),
    path('store/<int:pk>/',StoreViewSets.as_view({'get':'post','delete':'destroy','put':'update'}))
]
