import base64
from django.test import Client, TestCase, TransactionTestCase
from users.models import *
from fileshare.models import *
import uuid

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.credentials = [
            (uuid.uuid4().hex + '@mail.com', uuid.uuid4().hex) for _ in range(10)]

    def test_user_creation(self):
        """Test user can be created and deleted"""
        for email, password in self.credentials:
            user = User.objects.create(email = email, password = password, is_active=True)
            self.assertTrue(User.objects.filter(email=email).exists())
            self.assertEqual(user.email, email)
            self.assertTrue(user.is_active)
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_superuser)
            user.delete()
            self.assertFalse(User.objects.filter(email=email).exists())

    def test_inactive_user(self):
        """Test inactive user"""
        for email, password in self.credentials:
            user = User.objects.create(email = email, password = password, is_active=False)
            self.assertFalse(user.is_active)
            user.delete()
            self.assertFalse(User.objects.filter(email=email).exists())

    def test_user_creation_with_role(self):
        """Test patient and doctor creation"""
        for email, password in self.credentials[:2]:
            user = User.objects.create(email = email, password = password, is_active=True)
            patient = Patient.objects.create(user = user)
            self.assertTrue(user.patient)
            user.delete()
            self.assertFalse(User.objects.filter(email=email).exists())

        for email, password in self.credentials[2:4]:
            user = User.objects.create_user(email, password)
            doctor = Doctor.objects.create(user = user)
            self.assertTrue(user.doctor)
            user.delete()
            self.assertFalse(User.objects.filter(email=email).exists())

class LoginTestCase(TransactionTestCase):
    def setUp(self):
        self.credentials = [
            (uuid.uuid4().hex + '@mail.com', uuid.uuid4().hex, uuid.uuid4().hex) for _ in range(10)]
        self.users = []
        for email, password, username in self.credentials:
            user = User.objects.create(email = email, username = username, is_active=True)
            user.set_password(password)
            user.save()
            self.assertTrue(User.objects.filter(email=email).exists())
            self.users.append(user)

    def test_login(self):
        """Test login and logout"""
        for email, password, username in self.credentials:
            self.client.login(password=password, username=username)
            self.assertTrue(self.client.session.get('_auth_user_id'))
            self.client.logout()
            self.assertFalse(self.client.session.get('_auth_user_id'))

    def test_mail_verification_with_wrong_token(self):
        """Test mail verification with wrong token"""
        for user in self.users:
            user.is_active = False
            user.save()
            user = User.objects.get(email=user.email)
            self.assertFalse(user.is_active)
            token = uuid.uuid4().hex
            user_id_b64 = base64.b64encode((user.pk).to_bytes(1, "big"))
            response = self.client.get(
                f"/verification/user/verify-email/{token}/{user_id_b64}")
            self.assertEqual(response.status_code, 301)
            user = User.objects.get(email=user.email)
            self.assertFalse(user.is_active)

# class FileTestCase(TestCase):
#     def setUp(self):
#         self.credentials = [(uuid.uuid4().hex + '@mail.com', uuid.uuid4().hex, uuid.uuid4().hex) for _ in range(10)]
#         self.users = []
#         for email, password, username in self.credentials:
#             user = User.objects.create(email = email, username = username, is_active=True)
#             user.set_password(password)
#             user.save()
#             self.assertTrue(User.objects.filter(email=email).exists())
#             self.users.append(user)
#             self.client = Client()
#             self.client.login(password=password, username=username)

#     def get_myFiles_without_patient(self):
#         """Test myFiles without_patient"""
#         for user in self.users:
#             print()

#     def test_get_profile_view_without_patient(self):
#         """Test get profile without patient"""
#         for user in self.users:
#             try:
#                 response = self.client.get('/profile/')
                
#             except:
                