from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    """
    This model is used to change primary key with uuid
    to secure the data.
    """
    id = models.UUIDField(default=uuid.uuid4,
    primary_key=True,
    unique=True,
    editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True