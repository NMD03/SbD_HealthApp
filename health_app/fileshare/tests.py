import base64
import io
from django.test import Client, RequestFactory, TestCase, TransactionTestCase
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse
from django.core import *
from users.models import *
from fileshare.models import *
from io import StringIO
import uuid
from django.contrib.auth.models import Group
from fileshare.views import *
from reportlab.pdfgen import canvas
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.credentials = [
            (uuid.uuid4().hex + '@mail.com', uuid.uuid4().hex) for _ in range(10)]
    #Test_ID 1
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
    #Test_ID 2
    def test_inactive_user(self):
        """Test inactive user"""
        for email, password in self.credentials:
            user = User.objects.create(email = email, password = password, is_active=False)
            self.assertFalse(user.is_active)
            user.delete()
            self.assertFalse(User.objects.filter(email=email).exists())
    #Test_ID 3
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
    #Test_ID 4
    def test_user_creation_with_role_and_group(self):
        """Test patient and doctor creation with group"""
        for email, password in self.credentials[:2]:
            user = User.objects.create(email = email, password = password, is_active=True)
            patient = Patient.objects.create(user = user)
            new_group, created = Group.objects.get_or_create(name='patient')
            user.groups.add(new_group)
            self.assertTrue(user.patient)
            self.assertTrue(user.groups.filter(name='patient').exists())
            user.delete()
            self.assertFalse(User.objects.filter(email=email).exists())

        for email, password in self.credentials[2:4]:
            user = User.objects.create_user(email, password)
            doctor = Doctor.objects.create(user = user)
            new_group, created = Group.objects.get_or_create(name='doctor')
            user.groups.add(new_group)
            self.assertTrue(user.doctor)
            self.assertTrue(user.groups.filter(name='doctor').exists())
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
    #Test_ID 5
    def test_login(self):
        """Test login and logout"""
        for email, password, username in self.credentials:
            self.client.login(password=password, username=username)
            self.assertTrue(self.client.session.get('_auth_user_id'))
            self.client.logout()
            self.assertFalse(self.client.session.get('_auth_user_id'))
    #Test_ID 6
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

class RouteTestCase(TestCase):
    def setUp(self):
        self.credentials = [(uuid.uuid4().hex + '@mail.com', uuid.uuid4().hex, uuid.uuid4().hex) for _ in range(10)]
        self.users = []
        for email, password, username in self.credentials:
            user = User.objects.create(email = email, username = username, is_active=True)
            user.set_password(password)
            user.save()
            self.assertTrue(User.objects.filter(email=email).exists())
            self.users.append(user)
            self.client.login(password=password, username=username)
            self.factory = RequestFactory()
    #Test_ID 7
    def test_get_profile_view_without_patient(self):
        """Test get profile without patient"""
        for user in self.users:
            try:
                response = self.client.get('/profile/')
                self.assertTrue(False) 
            except:
                self.assertFalse(False)
    #Test_ID 8
    def test_get_profile_view_with_patient(self):
        """Test get profile with patient"""
        for user in self.users:
            patient = Patient.objects.create(user = user)
            self.assertTrue(user.patient)
            new_group, created = Group.objects.get_or_create(name='patient')
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            self.assertTrue(user.groups.filter(name='patient').exists())
            request = self.factory.get('/profile/')
            request.user = user
            response = profile(request)
            self.assertEqual(response.status_code, 200)
    #Test_ID 9
    def test_get_login_view(self):
        """Test get login view"""
        response = self.client.get('/users/login/', follow=True)
        self.assertEqual(response.status_code, 200)
    #Test_ID 10
    def test_get_myfiles_view_without_patient(self):
        """Test get myfiles without patient"""
        for user in self.users:
            try:
                response = self.client.get('/myfiles/')
                self.assertTrue(False) 
            except:
                self.assertFalse(False)
    #Test_ID 11
    def test_get_myfiles_view_with_patient(self):
        """Test get myfiles with patient"""
        for user in self.users:
            patient = Patient.objects.create(user = user)
            self.assertTrue(user.patient)
            new_group, created = Group.objects.get_or_create(name='patient')
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            self.assertTrue(user.groups.filter(name='patient').exists())
            request = self.factory.get('/myfiles/')
            request.user = user
            response = myfiles(request)
            self.assertEqual(response.status_code, 200)
    #Test_ID 12
    def test_get_sharedfiles_view_without_patient(self):
        """Test get sharedfiles without patient"""
        for user in self.users:
            try:
                response = self.client.get('/shared_files/')
                self.assertTrue(False) 
            except:
                self.assertFalse(False)
    #Test_ID 13
    def test_get_sharedfiles_view_with_patient(self):
        """Test get sharedfiles with patient"""
        for user in self.users:
            patient = Patient.objects.create(user = user)
            self.assertTrue(user.patient)
            new_group, created = Group.objects.get_or_create(name='patient')
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            self.assertTrue(user.groups.filter(name='patient').exists())
            request = self.factory.get('/shared_files/')
            request.user = user
            response = shared_files(request)
            self.assertEqual(response.status_code, 200)
    #Test_ID 14
    def test_get_alldoctors_view_without_patient(self):
        """Test get alldoctors without patient"""
        for user in self.users:
            try:
                response = self.client.get('/all_doctors/')
                self.assertTrue(False) 
            except:
                self.assertFalse(False)
    #Test_ID 15
    def test_get_alldoctors_view_with_patient(self):
        """Test get alldoctorss with patient"""
        for user in self.users:
            patient = Patient.objects.create(user = user)
            self.assertTrue(user.patient)
            new_group, created = Group.objects.get_or_create(name='patient')
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            self.assertTrue(user.groups.filter(name='patient').exists())
            request = self.factory.get('/all_doctors/')
            request.user = user
            response = all_doctors(request)
            self.assertEqual(response.status_code, 200)
    #Test_ID 16
    def test_get_mydoctors_view_without_patient(self):
        """Test get mydoctors without patient"""
        for user in self.users:
            try:
                response = self.client.get('/my_doctors/')
                self.assertTrue(False) 
            except:
                self.assertFalse(False)
    #Test_ID 17
    def test_get_mydoctors_view_with_patient(self):
        """Test get mydoctors with patient"""
        for user in self.users:
            patient = Patient.objects.create(user = user)
            self.assertTrue(user.patient)
            new_group, created = Group.objects.get_or_create(name='patient')
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            self.assertTrue(user.groups.filter(name='patient').exists())
            request = self.factory.get('/my_doctors/')
            request.user = user
            response = my_doctors(request)
            self.assertEqual(response.status_code, 200)
    #Test_ID 18
    def test_get_patientdata_view_without_doctor(self):
        """Test get patientdata without patient"""
        for user in self.users:
            try:
                response = self.client.get('/patient_data/')
                self.assertTrue(False) 
            except:
                self.assertFalse(False)
    #Test_ID 19
    def test_get_patientrequest_view_without_doctor(self):
        """Test get patientrequest without patient"""
        for user in self.users:
            try:
                response = self.client.get('/get_patient_requests/')
                self.assertTrue(False) 
            except:
                self.assertFalse(False)

class FileTestCase(TestCase):
    def setUp(self):
        self.credentials = [(uuid.uuid4().hex + '@mail.com', uuid.uuid4().hex, uuid.uuid4().hex) for _ in range(10)]
        self.users = []
        for email, password, username in self.credentials:
            user = User.objects.create(email = email, username = username, is_active=True)
            user.set_password(password)
            user.save()
            self.assertTrue(User.objects.filter(email=email).exists())
            self.users.append(user)
            # self.client = Client()
            self.client.login(password=password, username=username)
            self.factory = RequestFactory()

    def test_file_upload_successfully_on_text_file(self):
         for user in self.users:
            # patient = Patient.objects.create(user = user)
            # self.assertTrue(user.patient)
            # new_group, created = Group.objects.get_or_create(name='patient')
            # group = Group.objects.get(name='patient')
            # user.groups.add(group)
            # self.assertTrue(user.groups.filter(name='patient').exists())
            test_file = SimpleUploadedFile("file.txt", b"file_content", content_type="text/txt")
            request = self.factory.post('/create_file/', {'name':'sdfd',"description":"descrr", "form": test_file})
            request.user = user
            response = create_file(request)
            self.assertEqual(response.status_code, 302)

