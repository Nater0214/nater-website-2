import json

from django.http import HttpResponse
from django.template import loader

def index(request) -> HttpResponse:
    """The main website page"""
    
    # Load the template
    template = loader.get_template("root.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Load newest thingies
    with open("./root/newest_thingies.json", 'r') as file:
        newest_thingies = json.load(file)
    
    # Set context values
    context_values = {
        "name": "Home",
        "pages": pages,
        "newest_thingies": newest_thingies
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request))


def about_me(request) -> HttpResponse:
    """The about me page"""
    
    # Load the template
    template = loader.get_template("about_me.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Set context values
    context_values = {
        "name": "About Me",
        "pages": pages
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request))


def about_site(request) -> HttpResponse:
    """The about site page"""
    
    # Load the template
    template = loader.get_template("about_site.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Set context values
    context_values = {
        "name": "About Site",
        "pages": pages
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request))


def tools(request) -> HttpResponse:
    """The tools index"""
    
    # Load the template
    template = loader.get_template("tools.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Set context values
    context_values = {
        "name": "Tools",
        "pages": pages
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request))


def popup_maker(request) -> HttpResponse:
    """The popup maker page"""
    
    # Load the template
    template = loader.get_template("tools/popup_maker.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Set context values
    context_values = {
        "name": "Popup Maker",
        "pages": pages,
        "imports": [
            {
                "from": "root/popup-maker/popup.js",
                "as": "Popup"
            }
        ],
        "onloads": [
            "Popup.setup"
        ]
    }
    
    return HttpResponse(template.render(context_values, request))


def shrek_fanpage(request) -> HttpResponse:
    """The Shrek Fanpage"""
    
    # Load the template
    template = loader.get_template("shrek_fanpage.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Set context values
    context_values = {
        "name": "Shrek Fanpage",
        "pages": pages
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request))


# Error views
def error404(request, exception) -> HttpResponse:
    """The 404 error page"""
    
    # Load the template
    template = loader.get_template("error.html")
    
    # Set context values
    context_values = {
        "number": "404",
        "message": "I can't find that page :/"
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request), status=404)


def error500(request) -> HttpResponse:
    """The 500 error page"""
    
    # Load the template
    template = loader.get_template("error.html")
    
    # Set context values
    context_values = {
        "number": "500",
        "message": "Something went wrong :("
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request), status=500)


def error503(request) -> HttpResponse:
    """The 503 error page"""
    
    # Load the template
    template = loader.get_template("error.html")
    
    # Set context values
    context_values = {
        "number": "503",
        "message": "This page is unavailable for some reason :/ (probably working on it)"
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request), status=503)