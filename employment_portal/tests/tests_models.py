from django.test import TestCase
from employment_portal.models import ApplicantUser, Company, Offer, Postulation


class ApplicantUserModelTestCase(TestCase):
    def test_str_representation(self):
        user = ApplicantUser.objects.create(username="testuser", identification_number="1234567890")
        self.assertEqual(str(user), "testuser")

    def test_get_full_name(self):
        user = ApplicantUser.objects.create(username="testuser", first_name="John", last_name="Doe")
        self.assertEqual(user.get_full_name(), "testuser Doe")


class CompanyModelTestCase(TestCase):
    def test_str_representation(self):
        company = Company.objects.create(name="Test Company", nit="1234567890")
        self.assertEqual(str(company), "Test Company")


class OfferModelTestCase(TestCase):
    def test_str_representation(self):
        company = Company.objects.create(name="Test Company", nit="1234567890")
        offer = Offer.objects.create(
            title="Test Offer",
            description="Test Offer Description",
            salary=50000.0,
            company=company,
            skills="Python, Django",
        )
        self.assertEqual(str(offer), "Test Offer")

    def test_offer_attributes(self):
        company = Company.objects.create(name="Test Company", nit="1234567890")
        offer = Offer.objects.create(
            title="Test Offer",
            description="Test Offer Description",
            salary=50000.0,
            company=company,
            skills="Python, Django",
        )

        self.assertEqual(offer.title, "Test Offer")
        self.assertEqual(offer.description, "Test Offer Description")
        self.assertEqual(offer.salary, 50000.0)
        self.assertEqual(offer.company, company)
        self.assertEqual(offer.skills, "Python, Django")


class PostulationModelTestCase(TestCase):
    def test_str_representation(self):
        company = Company.objects.create(name="Test Company", nit="1234567890")
        offer = Offer.objects.create(
            title="Test Offer",
            description="Test Offer Description",
            salary=50000.0,
            company=company,
            skills="Python, Django",
        )
        user = ApplicantUser.objects.create(username="testuser", identification_number="1234567890")
        postulation = Postulation.objects.create(user=user, offer=offer)
        self.assertEqual(str(postulation), "testuser - Test Offer")

    def test_postulation_attributes(self):
        company = Company.objects.create(name="Test Company", nit="1234567890")
        offer = Offer.objects.create(
            title="Test Offer",
            description="Test Offer Description",
            salary=50000.0,
            company=company,
            skills="Python, Django",
        )
        user = ApplicantUser.objects.create(username="testuser", identification_number="1234567890")
        postulation = Postulation.objects.create(user=user, offer=offer)

        self.assertEqual(postulation.user, user)
        self.assertEqual(postulation.offer, offer)
