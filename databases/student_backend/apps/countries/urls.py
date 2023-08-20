from django.urls import path

from apps.countries.api.views import CountryListCreateAPIView, CountryRetrieveAPIView

urlpatterns = [
    path("", CountryListCreateAPIView.as_view(), name="country-list-create"),
    path("<int:country_id>/", CountryRetrieveAPIView.as_view(), name="country-retrieve")
]
