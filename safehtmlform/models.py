from django.db import models
from fields import SafeHTMLField as SafeHTMLFormField

class SafeHTMLField(models.CharField):
    formfield = SafeHTMLFormField