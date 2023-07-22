from django.urls import path


from .views import (
    ApplicantUserLoginView,
    ApplicantUserCreateView,
    OfferCreateView,
    OfferUpdateView,
    CompanyCreateView,
    PostulationCreateView,
)

urlpatterns = [
    path("login/", ApplicantUserLoginView.as_view(), name="user-login"),
    path("register/", ApplicantUserCreateView.as_view(), name="user-register"),
    path("create-company/", CompanyCreateView.as_view(), name="company-create"),
    path("create-offer/", OfferCreateView.as_view(), name="offer-create"),
    path("update-offer/<int:pk>/", OfferUpdateView.as_view(), name="offer-update"),
    path("create-postulation/", PostulationCreateView.as_view(), name="postulation-create"),
]
