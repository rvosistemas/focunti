from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ApplicantUser, Company, Offer, Postulation
from .serializers import ApplicantUserSerializer, CompanySerializer, OfferSerializer, PostulationSerializer


# Create your views here.
class ApplicantUserListView(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = ApplicantUser.objects.all().order_by("-date_joined")
    serializer_class = ApplicantUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class ApplicantUserLoginView(ObtainAuthToken):
    """
    Custom authentication view for obtaining the auth token.
    """

    def post(self, request, *args, **kwargs) -> Response:
        """
        Handle POST requests to obtain an authentication token.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response object with 'token' and 'user_id' upon successful authentication.
        """
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key, "user_id": token.user_id}, status=status.HTTP_200_OK)
