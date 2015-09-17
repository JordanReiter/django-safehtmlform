from django.db import models
from .fields import SafeHTMLField as SafeHTMLFormField

class SafeHTMLField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.additional_elements = kwargs.pop("additional_elements", None)
        super(SafeHTMLField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'additional_elements': self.additional_elements}
        defaults.update(kwargs)
        return SafeHTMLFormField(**defaults)
