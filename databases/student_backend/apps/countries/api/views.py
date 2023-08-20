from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.countries.api.serializers import (
    CountryListCreateOutputSerializer,
    CountryCreateInputSerializer,
    CountryRetrieveUpdateSerializer
)
from apps.countries.selectors import get_all_countries
from apps.countries.services import create_country, update_country, delete_country
from ..models import Country


class CountryListCreateAPIView(APIView):
    def post(self, request):
        request_data = request.data  # {"name": "Україна"}

        serializer = CountryCreateInputSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        print("VALIDATED DATA")
        print(validated_data)

        country = create_country(validated_data)

        print("CREATED COUNTRY")
        print(country)

        country_dictionary = CountryListCreateOutputSerializer(country).data

        print("DESERIALIZED DICTIONARY")
        print(country_dictionary)

        return Response(country_dictionary, status=status.HTTP_201_CREATED)

    def get(self, request):
        countries = get_all_countries()
        serializer = CountryListCreateOutputSerializer(countries, many=True)
        countries_data = serializer.data
        return Response(countries_data, status=status.HTTP_200_OK)


class CountryRetrieveAPIView(APIView):
    def get(self, request, country_id):
        country = get_object_or_404(Country, id=country_id)
        serializer = CountryRetrieveUpdateSerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, country_id):
        country = get_object_or_404(Country, id=country_id)
        serializer = CountryRetrieveUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        update_country(country, validated_data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, country_id):
        country = get_object_or_404(Country, id=country_id)
        delete_country(country)
        return Response(status=status.HTTP_204_NO_CONTENT)
