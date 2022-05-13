# based on http://djangosnippets.org/snippets/1284/
import re
import random

from ..conf import settings
from ..minifier import minify


def protect_email(email, link_text, css_class, **kwargs):
    # href_start = '&#x6d;&#97;&#105;&#x6c;&#000116;&#111;&#x3a;'
    link = 'mailto:%s' % email
    return protect(link, link_text, css_class, **kwargs)


def protect_phone(phone, link_text, css_class, **kwargs):
    # href_start = '&#x74;&#101;&#108;&#x3a;'
    link = 'tel:%s' % phone
    return protect(link, link_text, css_class, **kwargs)


def protect(link, link_text, css_class, **attributes):
    # link_text = link_text.replace('.', ' . ')  # noqa
    link_text = link_text.replace('@', ' ( at ) ')
    link_array = ''
    link = link.replace(' ', '')
    for c in link:
        link_array += "'%s', " % c
    attributes_html = ''
    if attributes.get('href', None):
        del(attributes['href'])
    for key, value in attributes.items():
        attributes_html += '{}="{}" '.format(key, value)
    the_id = "%s%s" % (
        settings.MAILPROTECTOR_FUNCTION_PREFIX,
        str(random.randint(1000, 999999999999999999)),
    )
    result = """
        <a href="javascript:{id}()" {attributes_html} class="{css_class}">{link_text}</a>
        <script>
            function {id} () {{
                var value = '';
                var _tyjsdf = [{value_array}];
                for(_i=0;_i<_tyjsdf.length;_i++) {{ value += _tyjsdf[_i]; }}
                window.location.href = value;
                return true;
            }}
        </script>
    """.format(
        id=the_id,
        value_array=re.sub(r',$', '', link_array),
        link_text=link_text,
        css_class=css_class,
        attributes_html=attributes_html,
    )
    return minify(result)
