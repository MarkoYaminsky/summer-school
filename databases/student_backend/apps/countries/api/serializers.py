from rest_framework import serializers

from apps.countries.models import Country


class CountryCreateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


class CountryListCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class CountryRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


