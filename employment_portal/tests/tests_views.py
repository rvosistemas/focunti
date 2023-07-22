from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from employment_portal.models import Company, Offer, Postulation

User = get_user_model()


@override_settings(DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}})
class SQLiteMemoryTestCase(TestCase):
    pass


class ApplicantUserLoginViewTestCase(SQLiteMemoryTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_applicant_user_login_success(self):
        login_url = reverse("user-login")
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        token = response.data["token"]
        self.assertTrue(Token.objects.filter(key=token, user=self.user).exists())

    def test_applicant_user_login_failure_invalid_credentials(self):
        login_url = reverse("user-login")
        data = {
            "username": "testuser",
            "password": "invalidpassword",
        }
        response = self.client.post(login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", response.data)


class ApplicantUserCreateViewTestCase(SQLiteMemoryTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()

    def test_applicant_user_create_success(self):
        register_url = reverse("user-register")
        data = {
            "username": "testuser",
            "password": "testpassword",
            "identification_number": "1234567890",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "profile_description": "Test profile",
            "phone_number": "1234567890",
        }
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("username", response.data)

        user = User.objects.get(username="testuser")
        self.assertEqual(user.identification_number, "1234567890")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.profile_description, "Test profile")
        self.assertEqual(user.phone_number, "1234567890")

    def test_applicant_user_create_failure_missing_required_fields(self):
        register_url = reverse("user-register")
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("identification_number", response.json())
        self.assertEqual("['This field is required.']", str(response.json()["identification_number"]))


class CompanyCreateViewTestCase(SQLiteMemoryTestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.company_data = {
            "name": "Test Company",
            "nit": "1234567890",
        }

    def test_company_create_success(self):
        create_company_url = reverse("company-create")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post(create_company_url, self.company_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("name", response.data)
        self.assertIn("nit", response.data)

        company = Company.objects.get(pk=response.data["id"])
        self.assertEqual(company.name, self.company_data["name"])
        self.assertEqual(company.nit, self.company_data["nit"])

    def test_company_create_failure_missing_required_fields(self):
        create_company_url = reverse("company-create")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        data = {"name": "Test Company"}
        response = self.client.post(create_company_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("nit", response.data)


class OfferCreateViewTestCase(SQLiteMemoryTestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.company = Company.objects.create(name="Test Company", nit="1234567890")
        self.offer_data = {
            "title": "Test Offer",
            "description": "This is a test offer",
            "salary": "1000.00",
            "company": self.company.id,
            "skills": "Python, Django",
        }

    def test_offer_create_success(self):
        create_offer_url = reverse("offer-create")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post(create_offer_url, self.offer_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("title", response.data)
        self.assertIn("description", response.data)
        self.assertIn("salary", response.data)
        self.assertIn("company", response.data)
        self.assertIn("skills", response.data)

        offer = Offer.objects.get(pk=response.data["id"])
        self.assertEqual(offer.title, self.offer_data["title"])
        self.assertEqual(offer.description, self.offer_data["description"])
        self.assertEqual(str(offer.salary), self.offer_data["salary"])
        self.assertEqual(offer.company.id, self.offer_data["company"])
        self.assertEqual(offer.skills, self.offer_data["skills"])

    def test_offer_create_failure_missing_required_fields(self):
        create_offer_url = reverse("offer-create")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        data = {
            "title": "Test Offer",
            "description": "This is a test offer",
            # Missing 'salary', 'company', and 'skills'
        }
        response = self.client.post(create_offer_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("salary", response.data)
        self.assertIn("company", response.data)
        self.assertIn("skills", response.data)


class OfferUpdateViewTestCase(SQLiteMemoryTestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.company = Company.objects.create(name="Test Company", nit="1234567890")
        self.offer = Offer.objects.create(
            title="Test Offer",
            description="This is a test offer",
            salary="1000.00",
            company=self.company,
            skills="Python, Django",
        )
        self.update_offer_url = reverse("offer-update", args=[self.offer.id])
        self.updated_offer_data = {
            "title": "Updated Test Offer",
            "description": "This is an updated test offer",
            "salary": "2000.00",
            "company": self.company.id,
            "skills": "Python, Django, React",
        }

    def test_offer_update_success(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.patch(self.update_offer_url, self.updated_offer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.data)
        self.assertIn("title", response.data)
        self.assertIn("description", response.data)
        self.assertIn("salary", response.data)
        self.assertIn("company", response.data)
        self.assertIn("skills", response.data)

        updated_offer = Offer.objects.get(pk=response.data["id"])
        self.assertEqual(updated_offer.title, self.updated_offer_data["title"])
        self.assertEqual(updated_offer.description, self.updated_offer_data["description"])
        self.assertEqual(str(updated_offer.salary), self.updated_offer_data["salary"])
        self.assertEqual(updated_offer.company.id, self.updated_offer_data["company"])
        self.assertEqual(updated_offer.skills, self.updated_offer_data["skills"])

    def test_offer_update_failure_invalid_authentication_token(self):
        response = self.client.patch(self.update_offer_url, self.updated_offer_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PostulationCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.company = Company.objects.create(name="Test Company", nit="1234567890")
        self.offer = Offer.objects.create(
            title="Test Offer",
            description="Test Offer Description",
            salary=50000.0,
            company=self.company,
            skills="Python, Django",
        )

    def test_postulation_create_success(self):
        create_postulation_url = reverse("postulation-create")

        data = {
            "user": self.user.id,
            "offer": self.offer.id,
        }

        response = self.client.post(create_postulation_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        postulation = Postulation.objects.get(id=response.data["id"])
        self.assertEqual(postulation.user, self.user)
        self.assertEqual(postulation.offer, self.offer)

    def test_postulation_create_failure_invalid_offer(self):
        create_postulation_url = reverse("postulation-create")

        data = {
            "user": self.user.id,
            "offer": 99999,
        }

        response = self.client.post(create_postulation_url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("offer", response.data)

    def test_postulation_create_failure_invalid_user(self):
        create_postulation_url = reverse("postulation-create")

        data = {
            "user": 99999,
            "offer": self.offer.id,
        }

        response = self.client.post(create_postulation_url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("user", response.data)
