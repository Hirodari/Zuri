from extensions import mail
from flask import render_template


def send_template_message(template=None, ctx=None, *args, **kwargs):
    

    if ctx is None:
        ctx = {}

    if template is not None:
        if 'body' in kwargs:
            raise Exception('You cannot have both a template and body arg.')
        elif 'html' in kwargs:
            raise Exception('You cannot have both a template and body arg.')

    kwargs['body'] = _try_renderer_template(template, **ctx)
    kwargs['html'] = _try_renderer_template(template, ext='html', **ctx)

    

    mail.send_message(*args, **kwargs)
    return None

def _try_renderer_template(template_path, ext='txt', **kwargs):
    """
    Attempt to render a template. We use a try/catch here to avoid having to
    do a path exists based on a relative path to the template.

    :param template_path: Template path
    :type template_path: str
    :param ext: File extension
    :type ext: str
    :return: str
    """
    print(f"printing the template_path: {template_path}")
    try:
        return render_template('{0}.{1}'.format(template_path, ext), **kwargs)
    except IOError:
        pass


