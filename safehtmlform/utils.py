try:
    from bs4 import BeautifulSoup, Comment
except ImportError:
    from BeautifulSoup import BeautifulSoup, Comment

import re

acceptable_elements = ('a', 'abbr', 'acronym', 'address', 'b', 'blockquote', 'br', 'cite', 'code', 
                       'dd', 'del', 'dfn', 'div', 'dl', 'dt', 'em', 'i', 'img', 'ins', 'kbd', 'li', 
                       'ol', 'p', 'pre', 'q', 's', 'small', 'span', 'strike', 'strong', 'sub', 
                       'sup', 'tt', 'u', 'ul' )
acceptable_attributes = ('abbr', 'cite', 'href', 'rel', 'rev', 'src', 'title') 
acceptable_protocols = ('http://', 'https://', 'mailto:')
protocols_regex = "(%s)" % "|".join([re.escape(p) for p in acceptable_protocols])


def sanitize_attrs(attrs):
    sanitized_attrs = {}
    for (key, value) in [(key, val) for key, val in attrs.items() if (key in acceptable_attributes)]:
        if key != 'href':
            sanitized_attrs[key] = value
        else:
            if re.search(r'^([a-z]+):', value):
                value = value.replace(':80/', '/').replace(':443/', '/')
                if re.match(r'^%s[^:]+$' % protocols_regex, value):
                    sanitized_attrs[key] = value
    return sanitized_attrs


def sanitize_html(value, elements=acceptable_elements):
    soup = BeautifulSoup(value)
    for comment in soup.findAll(
        text=lambda text: isinstance(text, Comment)):
        comment.extract()
    for tag in soup.findAll(True):
        if tag.name not in elements:
            tag.hidden = True
        tag.attrs = sanitize_attrs(tag.attrs)
    return soup.renderContents().decode('utf8').replace('javascript:', '')
