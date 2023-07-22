from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import ApplicantUserListView, ApplicantUserLoginView

router = DefaultRouter()
router.register("users", ApplicantUserListView, basename="users")

urlpatterns = [
    # users
    path("", include(router.urls)),
    # path("register/", UserRegistrationView.as_view(), name="user-registration"),
    path("login/", ApplicantUserLoginView.as_view(), name="user-login"),
]
