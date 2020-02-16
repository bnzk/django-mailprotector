import re
import random


# originally based on http://djangosnippets.org/snippets/1284/

def protect_email(email, link_text, css_class, **kwargs):
    href_start = '&#x6d;&#97;&#105;&#x6c;&#000116;&#111;&#x3a;'
    return protect(href_start, email, link_text, css_class, **kwargs)


def protect_phone(phone, link_text, css_class, **kwargs):
    href_start = '&#x74;&#101;&#108;&#x3a;'
    return protect(href_start, phone, link_text, css_class, **kwargs)


def protect(href_start, value, link_text, css_class, **kwargs):
    value_array_content = ''
    text_array_content = ''
    r = lambda c: '"' + str(ord(c)) + '",'  # noqa

    for c in value:
        value_array_content += r(c)
    for c in link_text:
        text_array_content += r(c)

    the_id = "_tyjsdfss-" + str(random.randint(1000, 999999999999999999))

    # omit document.write to make it ajax safe!
    result = """<span id='{id}'></span><script language="javascript" type="text/javascript">
        <!--
        var _tyjsdf = [{value_array}], _qplmks = [{text_array}];
        var content = ('<a class="{css_class}" href="{href_start}');
        for(_i=0;_i<_tyjsdf.length;_i++){{ content += ('&#'+_tyjsdf[_i]+';');}}
        content += ('">');
        for(_i=0;_i<_qplmks.length;_i++){{ content += ('&#'+_qplmks[_i]+';');}}
        content += ('</a>');
        document.getElementById('{id}').innerHTML = content;
        -->
        </script>"""\
    .format(
        id=the_id,
        href_start=href_start,
        value_array=re.sub(r',$', '', value_array_content),
        text_array=re.sub(r',$', '', text_array_content),
        css_class=css_class,
    )
    return result
