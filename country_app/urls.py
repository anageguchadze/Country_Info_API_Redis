from django.urls import path
from .views import CountryListCreateView, CountryRetrieveUpdateDeleteView, CountryByNameView

urlpatterns = [
    path('countries/', CountryListCreateView.as_view(), name='country-list'),
    path('countries/<int:id>/', CountryRetrieveUpdateDeleteView.as_view(), name='country-detail'),
    path('countries/name/<str:name>/', CountryByNameView.as_view(), name='country-by-name'),
]
