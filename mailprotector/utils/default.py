import re, random


# based on http://djangosnippets.org/snippets/1284/
def protect(email, link_text, css_class):
    emailArrayContent = ''
    textArrayContent = ''
    r = lambda c: '"' + str(ord(c)) + '",'

    for c in email: emailArrayContent += r(c)
    for c in link_text: textArrayContent += r(c)

    the_id = "_tyjsdfss-" + str(random.randint(1000, 999999999999999999))

    # omit document.write to make it ajax safe!
    result = """<span id='%s'></span><script language="javascript" type="text/javascript">
                <!--
                var _tyjsdf = [%s], _qplmks = [%s];
                var content = ('<a class="%s" href="&#x6d;&#97;&#105;&#x6c;&#000116;&#111;&#x3a;');
                for(_i=0;_i<_tyjsdf.length;_i++){ content += ('&#'+_tyjsdf[_i]+';');}
                content += ('">');
                for(_i=0;_i<_qplmks.length;_i++){ content += ('&#'+_qplmks[_i]+';');}
                content += ('</a>');
                document.getElementById('%s').innerHTML = content;
                -->
                </script>""" % (the_id,
                                re.sub(r',$', '', emailArrayContent),
                                re.sub(r',$', '', textArrayContent),
                                css_class,
                                the_id,)
    return result