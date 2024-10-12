import uuid
from django.db import models

from django.contrib.auth.models import User

"""

This class definition defines a base model for tables in a database using Django's ORM (Object-Relational Mapping) system.

Here is a list explaining what each field does:

* `id`: A unique identifier for each table instance, automatically incremented by the database.
* `name`: A character field to store the name of the table, required and cannot be null.
* `descripion`: A character field to store a description of the table, optional and can be null.
* `is_active`: A boolean field to indicate whether the table is active, defaults to True and cannot be null.
* `is_deleted`: A boolean field to indicate whether the table is deleted, defaults to False and cannot be null.
* `user`: A foreign key field referencing the User model, required and cannot be null.
* `created_at`: A date/time field to store when the table instance was created, automatically set by the database.
* `updated_at`: A date/time field to store when the table instance was last updated, automatically updated by the database.

Note that this class does not have any methods, only fields. The `Meta` class is used to define metadata for the model, in this case, specifying that this model is abstract and cannot be instantiated directly.
"""
class TableBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False, related_name='%(class)s_user')
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False, editable=False)

    class Meta:
        abstract = True