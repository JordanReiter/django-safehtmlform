from django import forms
from .utils import sanitize_html, acceptable_elements
from django.utils.translation import ugettext as _

class SafeHTMLField(forms.CharField):
    widget=forms.widgets.Textarea()
    
    def __init__(self, *args, **kwargs):
        self.acceptable_elements = acceptable_elements
        additional_elements = kwargs.pop("additional_elements", None)
        if additional_elements:
            self.acceptable_elements += tuple(additional_elements)
        self.help_text=_("This field allows the use of the following HTML tags: %(tags)s." % {'tags': self.acceptable_elements})
        super(SafeHTMLField, self).__init__(*args, **kwargs)

    def clean(self, value):
        """
        Cleans non-allowed HTML from the input.
        """
        value = super(SafeHTMLField, self).clean(value)
        return sanitize_html(value, elements=self.acceptable_elements)
