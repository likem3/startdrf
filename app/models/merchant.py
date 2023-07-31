from django.db import models
from app.utils.models import BaseModel
from django.contrib.auth.models import User

class Merchant(BaseModel):
    code=models.CharField(max_length=4, unique=True)
    name=models.CharField(max_length=30, null=True, blank=True)
    user_id=models.OneToOneField(User, on_delete=models.CASCADE, related_name="merchant")

    class Meta:
        db_table = "app_accounts"