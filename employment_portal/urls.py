from django.urls import path


from .views import ApplicantUserLoginView, ApplicantUserCreateView

urlpatterns = [
    path("login/", ApplicantUserLoginView.as_view(), name="user-login"),
    path("register/", ApplicantUserCreateView.as_view(), name="user-register"),
]
