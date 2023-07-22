from rest_framework import serializers
from .models import ApplicantUser, Company, Offer, Postulation


class ApplicantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantUser
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "identification_number",
            "profile_description",
            "phone_number",
        ]

    extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = ApplicantUser.objects.create_user(password=password, **validated_data)
        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "nit"]


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ["id", "title", "description", "salary", "company", "skills", "created_at", "updated_at"]


class PostulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = ["id", "user", "offer"]
