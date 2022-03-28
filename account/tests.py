from django.test import TestCase,Client
from django.urls import reverse , resolve
from django.contrib.auth.models import User
from .forms import Registerforms , Loginforms
# Create your tests here.
class TestViews(TestCase):

	def setUp(self):

		# User.objects.create(usernmae = ... , password = "123")
		# (Continue to the top line)This is then compared to the hash stored in the database, and the client is denied access because 'adkfh5lkad438....' != '12345' 
		# So we use set_password
		
		client = Client()
		user = User.objects.create(username = 'admin')
		user.set_password("admin")
		user.save()

	def test_login_and_register(self):
		response = self.client.get(reverse("login_view"))
		self.assertTemplateUsed(response , "dist/index.html")
		register_form_data = {"username":"admin123" , "password":"123456789" , "re_password":"123456789"}
		login_form_data = {"username":"admin" , "password":"admin"}
		register_form = Registerforms(data = register_form_data)
		login_form = Loginforms(data = login_form_data)
		self.assertTrue(register_form.is_valid())
		self.assertTrue(login_form.is_valid())
		self.assertIsNotNone(User.objects.get(username="admin"))
		logged_in = self.client.login(username = "admin" ,password = "admin")
		self.assertTrue(logged_in)