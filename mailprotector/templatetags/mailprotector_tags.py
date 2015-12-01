# based on http://djangosnippets.org/snippets/1284/
# TODO: add other methods
# TODO: add templatetag for html pieces

import random

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
import re

register = template.Library()

@register.filter()
@stringfilter
def mailprotector(email, text=None, autoescape=None):
    text = text or email

    if autoescape:
        email = conditional_escape(email)
        text = conditional_escape(text)

    emailArrayContent = ''
    textArrayContent = ''
    r = lambda c: '"' + str(ord(c)) + '",'

    for c in email: emailArrayContent += r(c)
    for c in text: textArrayContent += r(c)

    the_id = "_tyjsdfss-" + str(random.randint(1000, 999999999999999999))

    # omit document.write to make it ajax safe!
    result = """<span id='%s'></span><script language="javascript" type="text/javascript">
                <!--
                var _tyjsdf = [%s], _qplmks = [%s];
                var content = ('<a href="&#x6d;&#97;&#105;&#x6c;&#000116;&#111;&#x3a;');
                for(_i=0;_i<_tyjsdf.length;_i++){ content += ('&#'+_tyjsdf[_i]+';');}
                content += ('">');
                for(_i=0;_i<_qplmks.length;_i++){ content += ('&#'+_qplmks[_i]+';');}
                content += ('</a>');
                document.getElementById('%s').innerHTML = content;
                -->
                </script>""" % (the_id,
                                re.sub(r',$', '', emailArrayContent),
                                re.sub(r',$', '', textArrayContent),
                                the_id,)

    return mark_safe(result)

mailprotector.needs_autoescape = True


