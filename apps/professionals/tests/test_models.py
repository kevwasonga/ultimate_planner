from django.test import TestCase
from ..models import Category, Professional, Review, SiteStats
from ..forms import ReviewForm, InquiryForm
from ..selectors import professional_list, professional_get_featured

class ProfessionalTest(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name="Architect", slug="architect")
        self.pro = Professional.objects.create(
            name="John Doe",
            category=self.cat,
            specialty="Residential",
            location="Nairobi",
            bio="Test bio",
            price_per_hour=5000,
            experience_years=5,
            phone="0700000000",
            email="john@example.com",
            is_verified=True,
            is_featured=True
        )

    def test_featured_selector(self):
        # Testing the functional selector instead of manager
        featured = professional_get_featured(6)
        self.assertIn(self.pro, featured)

    def test_average_rating(self):
        Review.objects.create(professional=self.pro, client_name="A", rating=5, comment="G")
        Review.objects.create(professional=self.pro, client_name="B", rating=4, comment="G")
        self.assertEqual(self.pro.average_rating, 4.5)

class FormTest(TestCase):
    def test_review_form_valid(self):
        form = ReviewForm(data={
            'client_name': 'Test Client',
            'client_email': 'test@example.com',
            'rating': 5,
            'comment': 'Excellent service!'
        })
        self.assertTrue(form.is_valid())

    def test_inquiry_form_valid(self):
        cat = Category.objects.create(name="Engineer", slug="engineer")
        form = InquiryForm(data={
            'name': 'Project Owner',
            'email': 'owner@example.com',
            'phone': '0711111111',
            'service_category': cat.id,
            'location': 'Mombasa',
            'message': 'I need a bridge built.'
        })
        self.assertTrue(form.is_valid())
