import json

from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.contrib import auth

from . import forms

def index(request: HttpRequest) -> HttpResponse:
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


def user(request: HttpRequest) -> HttpResponse:
    """The user page"""
    
    # Check for post
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        user = auth.authenticate(username=form.data["username"], password=form.data["password"])
        if user is not None:
            auth.login(request, user)
        form_valid = form.is_valid()
    else:
        form = forms.LoginForm()
        form_valid = None
    
    # Load the template
    template = loader.get_template("user.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Set context values
    context_values = {
        "name": "User Page",
        "pages": pages,
        "form": form,
        "form_valid": form_valid
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request))


def about_me(request: HttpRequest) -> HttpResponse:
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


def about_site(request: HttpRequest) -> HttpResponse:
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


def tools(request: HttpRequest) -> HttpResponse:
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


def popup_maker(request: HttpRequest) -> HttpResponse:
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


def shrek_fanpage(request: HttpRequest) -> HttpResponse:
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


def computing_innovation(request: HttpRequest) -> HttpResponse:
    """The Computing Innovation page"""
    
    # Load the template
    template = loader.get_template("computing_innovation.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Set context values
    context_values = {
        "name": "Computing Innovation",
        "pages": pages,
        "onloads": [
            "(() => {document.getElementById(\"myTrackpointImage\").style.maxHeight = document.getElementById(\"descriptionDiv\").clientHeight})"
        ],
        "onresizes": [
            "(() => {document.getElementById(\"myTrackpointImage\").style.maxHeight = document.getElementById(\"descriptionDiv\").clientHeight})"
        ]
    }
    
    # Return response
    return HttpResponse(template.render(context_values, request))


# Error views
def error404(request: HttpRequest, exception) -> HttpResponse:
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


def error500(request: HttpRequest) -> HttpResponse:
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


def error503(request: HttpRequest) -> HttpResponse:
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