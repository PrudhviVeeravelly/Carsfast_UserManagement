# user_management/models.py
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords
    # Other user-related fields

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pii_data = EncryptedCharField(max_length=255)  # Encrypted PII data
    # Other user data fields

