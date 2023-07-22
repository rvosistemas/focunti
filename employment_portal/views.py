from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ApplicantUser, Company, Offer, Postulation
from .serializers import ApplicantUserSerializer, CompanySerializer, OfferSerializer, PostulationSerializer
from .utils import send_registration_email


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


class ApplicantUserCreateView(CreateAPIView):
    """
    View for creating an ApplicantUser.

    This view allows creating a new ApplicantUser object and associating it with an existing User object.
    Unauthenticated users have permission to access this view.
    A registration email is sent to the newly created user.

    Supported HTTP methods:
    - POST: Creates a new ApplicantUser and associates it with an existing User object.

    Attributes:
    - queryset (QuerySet): A QuerySet that defines the set of ApplicantUsers available for the view.
    - serializer_class (Serializer): The serializer used to convert input data
        into ApplicantUser instances and vice versa.
    - authentication_classes (list): List of authentication classes used to verify the user's identity.
        In this case, authentication is omitted.
    - permission_classes (list): List of permission classes used to control access to the view.
        In this case, any unauthenticated user is allowed to access the view.

    Methods:
    - perform_create(serializer): A method that is executed during the creation of a new ApplicantUser.
        It saves the new ApplicantUser object and sends a registration email to the newly created user.

    """

    queryset = ApplicantUser.objects.all()
    serializer_class = ApplicantUserSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        fake_email = send_registration_email(user.username, user.email)
        response = {"message": "User created successfully", "data": serializer.data, "email": fake_email}
        return Response(response, status=status.HTTP_201_CREATED)
