from django.contrib.auth.models import AnonymousUser, User, Group
from django.test import RequestFactory, TestCase
from . import views


class WebsiteViewsTestes(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Testes')
        self.group.user_set.add(self.user)

    def test_index_anonimo(self):
        request = self.factory.get('')
        request.user = AnonymousUser()

        response = views.index(request)
        self.assertEqual(response.status_code, 200)
