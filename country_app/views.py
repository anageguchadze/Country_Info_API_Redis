from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Country
from .serializers import CountrySerializer

CACHE_TTL = 60 * 60 

class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        if 'countries' in cache:
            data = cache.get('countries')
            return Response(data, status=status.HTTP_200_OK)
        
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        cache.set('countries', serializer.data, timeout=CACHE_TTL)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        country_id = kwargs.get('id')
        cache_key = f'country_{country_id}'

        if cache_key in cache:
            return Response(cache.get(cache_key), status=status.HTTP_200_OK)

        country = get_object_or_404(Country, id=country_id)
        serializer = self.get_serializer(country)
        cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountryByNameView(generics.RetrieveAPIView):
    serializer_class = CountrySerializer

    def get(self, request, name, *args, **kwargs):
        cache_key = f'country_name_{name.lower()}'
        
        if cache_key in cache:
            return Response(cache.get(cache_key), status=status.HTTP_200_OK)

        country = get_object_or_404(Country, name__iexact=name)
        serializer = self.get_serializer(country)
        cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
        return Response(serializer.data, status=status.HTTP_200_OK)
