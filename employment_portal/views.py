from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
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


class CompanyCreateView(CreateAPIView):
    """
    View for creating a Company.

    This view allows creating a new Company object.

    Supported HTTP methods:
    - POST: Creates a new Company.

    Attributes:
    - queryset (QuerySet): A QuerySet that defines the set of Company objects available for the view.
    - serializer_class (Serializer): The serializer used to convert input data into Company instances and vice versa.

    Methods:
    - perform_create(serializer): A method that is executed during the creation of a new Company.
        It saves the new Company object.

    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class OfferCreateView(CreateAPIView):
    """
    View for creating an Offer.

    This view allows creating a new Offer object.

    Supported HTTP methods:
    - POST: Creates a new Offer.

    Attributes:
    - queryset (QuerySet): A QuerySet that defines the set of Offer objects available for the view.
    - serializer_class (Serializer): The serializer used to convert input data into Offer instances and vice versa.

    Methods:
    - perform_create(serializer): A method that is executed during the creation of a new Offer.
        It saves the new Offer object.

    """

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class OfferUpdateView(UpdateAPIView):
    """
    View for updating an Offer.

    This view allows updating an existing Offer object.

    Supported HTTP methods:
    - PUT: Updates an existing Offer.
    - PATCH: Partially updates an existing Offer.

    Attributes:
    - queryset (QuerySet): A QuerySet that defines the set of Offer objects available for the view.
    - serializer_class (Serializer): The serializer used to convert input data into Offer instances and vice versa.

    Methods:
    - perform_update(serializer): A method that is executed during the update of an existing Offer.
        It saves the updated Offer object.

    """

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class PostulationCreateView(CreateAPIView):
    """
    View for creating a Postulation.

    This view allows creating a new Postulation object.

    Supported HTTP methods:
    - POST: Creates a new Postulation.

    Attributes:
    - queryset (QuerySet): A QuerySet that defines the set of Postulation objects available for the view.
    - serializer_class (Serializer): The serializer used to convert input data into Postulation instances and vice versa.

    Methods:
    - perform_create(serializer): A method that is executed during the creation of a new Postulation.
        It saves the new Postulation object.

    """

    queryset = Postulation.objects.all()
    serializer_class = PostulationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
