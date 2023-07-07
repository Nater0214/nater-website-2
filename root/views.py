import json

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request) -> HttpResponse:
    """The main website page"""
    
    # Get the template
    template = loader.get_template("root.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Load newest thingies
    with open("./root/newest_thingies.json", 'r') as file:
        newest_thingies = json.load(file)
    
    context_values = {
        "name": "Home",
        "pages": pages,
        "newest_thingies": newest_thingies
    }
    return HttpResponse(template.render(context_values, request))


# Error views
def error404(request, exception) -> HttpResponse:
    template = loader.get_template("error.html")
    
    context_values = {
        "number": "404",
        "message": "I can't find that page :/"
    }
    return HttpResponse(template.render(context_values, request), status=404)


def error500(request) -> HttpResponse:
    template = loader.get_template("error.html")
    
    context_values = {
        "number": "500",
        "message": "Something went wrong :("
    }
    return HttpResponse(template.render(context_values, request), status=500)