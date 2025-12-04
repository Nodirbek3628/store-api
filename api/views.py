from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializer import ProductSerialer,FilterProductSerializer
from .models import Product


class StoreViewSets(ModelViewSet):
    serializer_class = ProductSerialer


    filter_backends = [SearchFilter]
    search_fields = ['name', 'category']


    def get_queryset(self):
        queryset = Product.objects.all()

       

        if self.action == 'list':
            filter_serializer = FilterProductSerializer(data=self.request.query_params)

            if filter_serializer.is_valid(raise_exception=True):
                min_price = filter_serializer.data.get('min_price')
                max_price = filter_serializer.data.get('max_price')
                stock = filter_serializer.data.get('stock')
                create_at = filter_serializer.data.get('cretae_at')

                if min_price is not None:
                    queryset = queryset.filter(price__gte=min_price)

                if max_price is not None:
                    queryset = queryset.filter(price__lte=max_price)

                if stock is not None:
                    queryset = queryset.filter(stock=stock)

                if create_at is not None:
                    queryset = queryset.filter(create_at__date=create_at)

        return queryset

