from django import forms
from utils import sanitize_html, acceptable_elements
from django.utils.translation import ugettext as _

class SafeHTMLField(forms.CharField):
    help_text=_("This field allows the use of the following HTML tags: %(tags)s." % {'tags': acceptable_elements})
    widget=forms.widgets.Textarea()

    def clean(self, value):
        """
        Cleans non-allowed HTML from the input.
        """
        value = super(SafeHTMLField, self).clean(value)
        return sanitize_html(value)