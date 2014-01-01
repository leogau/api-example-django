from django.shortcuts import render

# FIXME rename docs.html tutorial.html
def tutorial(request, template_name="docs.html", extra_context=None):
    return render(request, template=template_name, extra_context=extra_context)