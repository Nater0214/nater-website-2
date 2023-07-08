from django import template

register = template.Library()


# Tags
@register.simple_tag(takes_context=True)
def static(context, location: str):
    request = context["request"]
    return f"{request.scheme}://static.{request.get_host()}/{location}"