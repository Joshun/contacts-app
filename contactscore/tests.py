from django.contrib.auth.models import User
from django.test import TestCase

from contactscore.models import ContactBook, Contact


# Create your tests here.

class ContactsAppTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser', email='testuser@test.com')
        cls.second_user = User.objects.create(username='testuser2', email='testuser2@test.com')

    def test_homepage_redirect_without_login(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)

    def test_homepage_login(self):
        self.client.force_login(self.user)
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.user.email)

    def test_contactbook_present(self):
        self.client.force_login(self.user)

        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertNotContains(resp, 'TEST CONTACT BOOK')

        contact_book = ContactBook.objects.create(name='TEST CONTACT BOOK', user=self.user)
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'TEST CONTACT BOOK')

    def test_contact_present(self):
        self.client.force_login(self.user)

        contact_book = ContactBook.objects.create(name='TEST CONTACT BOOK', user=self.user)
        contact = Contact.objects.create(contact_book=contact_book, name='Ellie')

        resp = self.client.get(f'/view-contactbook/{contact_book.pk}')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Ellie')

    def test_can_only_see_your_contactbooks(self):
        self.client.force_login(self.user)
        contact_book = ContactBook.objects.create(name='TEST CONTACT BOOK USER 1', user=self.user)
        contact_book2 = ContactBook.objects.create(name='TEST CONTACT BOOK USER 2', user=self.second_user)


        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'TEST CONTACT BOOK USER 1')
        self.assertNotContains(resp, 'TEST CONTACT BOOK USER 2')

        self.client.force_login(self.second_user)
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'TEST CONTACT BOOK USER 2')
        self.assertNotContains(resp, 'TEST CONTACT BOOK USER 1')
