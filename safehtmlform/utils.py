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
    sanitized_attrs = []
    for (key, value) in [a for a in attrs if (a[0] in acceptable_attributes)]:
        if key != 'href':
            sanitized_attrs.append((key, value))
        else:
            if re.search(r'^([a-z]+):', value):
                if re.match(r'^%s[^:]+$' % protocols_regex, value):
                    sanitized_attrs.append((key, value))
    return sanitized_attrs


def sanitize_html(value):
    soup = BeautifulSoup(value)
    for comment in soup.findAll(
        text=lambda text: isinstance(text, Comment)):
        comment.extract()
    for tag in soup.findAll(True):
        if tag.name not in acceptable_elements:
            tag.hidden = True
        tag.attrs = sanitize_attrs(tag.attrs)
    return soup.renderContents().decode('utf8').replace('javascript:', '')
