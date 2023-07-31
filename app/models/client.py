from django.db import models
from app.utils.models import BaseModel

class Merchant(BaseModel):
    code=models.CharField(max_length=4, unique=True)
    name=models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = "app_accounts"