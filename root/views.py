import json

from django import http
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import loader

from . import forms

def index(request: http.HttpRequest) -> http.HttpResponse:
    """The main website page"""
    
    # Load the template
    template = loader.get_template("root.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Load newest thingies
    with open("./root/newest_thingies.json", 'r') as file:
        newest_thingies = json.load(file)
    
    # Set context values
    context_values = {
        "name": "Home",
        "pages": pages,
        "user": user,
        "newest_thingies": newest_thingies
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request))


def user(request: http.HttpRequest) -> http.HttpResponse:
    """The user page"""
    
    # Check for post
    if request.method == "POST":
        # Try to get action and return error if none
        try:
            action = request.POST["action"]
        except KeyError:
            return error400(request)
        
        # Match the action
        match action:
            # Login
            case "login":
                form = forms.LoginForm(request.POST)
                user = auth.authenticate(username=form.data["username"], password=form.data["password"])
                if user is None:
                    user = User.objects.create_user(username=form.data["username"], password=form.data["password"])
                auth.login(request, user)
                form_valid = form.is_valid()
            
            # Logout
            case "logout":
                auth.logout(request)
                form = forms.LoginForm()
                form_valid = None
            
            # Some other invalid action
            case _:
                return error400(request)
    
    else:
        form = forms.LoginForm()
        form_valid = None
    
    # Load the template
    template = loader.get_template("user.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Set context values
    context_values = {
        "name": "User Page",
        "pages": pages,
        "user": user,
        "form": form,
        "form_valid": form_valid
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request))


def about_me(request: http.HttpRequest) -> http.HttpResponse:
    """The about me page"""
    
    # Load the template
    template = loader.get_template("about_me.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Set context values
    context_values = {
        "name": "About Me",
        "pages": pages,
        "user": user
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request))


def about_site(request: http.HttpRequest) -> http.HttpResponse:
    """The about site page"""
    
    # Load the template
    template = loader.get_template("about_site.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Set context values
    context_values = {
        "name": "About Site",
        "pages": pages,
        "user": user,
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request))


def tools(request: http.HttpRequest) -> http.HttpResponse:
    """The tools index"""
    
    # Load the template
    template = loader.get_template("tools.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Set context values
    context_values = {
        "name": "Tools",
        "pages": pages,
        "user": user,
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request))


def popup_maker(request: http.HttpRequest) -> http.HttpResponse:
    """The popup maker page"""
    
    # Load the template
    template = loader.get_template("tools/popup_maker.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Set context values
    context_values = {
        "name": "Popup Maker",
        "pages": pages,
        "user": user,
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
    
    return http.HttpResponse(template.render(context_values, request))


def shrek_fanpage(request: http.HttpRequest) -> http.HttpResponse:
    """The Shrek Fanpage"""
    
    # Load the template
    template = loader.get_template("shrek_fanpage.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Set context values
    context_values = {
        "name": "Shrek Fanpage",
        "pages": pages,
        "user": user,
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request))


def computing_innovation(request: http.HttpRequest) -> http.HttpResponse:
    """The Computing Innovation page"""
    
    # Load the template
    template = loader.get_template("computing_innovation.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Set context values
    context_values = {
        "name": "Computing Innovation",
        "pages": pages,
        "user": user,
        "onloads": [
            "(() => {document.getElementById(\"myTrackpointImage\").style.maxHeight = document.getElementById(\"descriptionDiv\").clientHeight})"
        ],
        "onresizes": [
            "(() => {document.getElementById(\"myTrackpointImage\").style.maxHeight = document.getElementById(\"descriptionDiv\").clientHeight})"
        ]
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request))


def congo_act_now(request: http.HttpRequest) -> http.HttpResponse:
    """The Congo Act Now page"""
    
    # Load the template
    template = loader.get_template("congo_act_now.html")
    
    # Load pages
    with open("./root/pages.json", 'r') as file:
        pages = json.load(file)
    
    # Get user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    # Set context values
    context_values = {
        "name": "Congo Act Now",
        "pages": pages,
        "user": user,
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request))


# Error views
def error400(request: http.HttpRequest) -> http.HttpResponse:
    """The 400 error page"""
    
    # Load the template
    template = loader.get_template("error.html")
    
    # Set context values
    context_values = {
        "number": "400",
        "message": "That's not a valid request >:("
    }
    
    # Return response
    return http.HttpResponseBadRequest(template.render(context_values, request))


def error404(request: http.HttpRequest, exception) -> http.HttpResponse:
    """The 404 error page"""
    
    # Load the template
    template = loader.get_template("error.html")
    
    # Set context values
    context_values = {
        "number": "404",
        "message": "I can't find that page :/"
    }
    
    # Return response
    return http.HttpResponseNotFound(template.render(context_values, request))


def error500(request: http.HttpRequest) -> http.HttpResponse:
    """The 500 error page"""
    
    # Load the template
    template = loader.get_template("error.html")
    
    # Set context values
    context_values = {
        "number": "500",
        "message": "Something went wrong :("
    }
    
    # Return response
    return http.HttpResponseServerError(template.render(context_values, request))


def error503(request: http.HttpRequest) -> http.HttpResponse:
    """The 503 error page"""
    
    # Load the template
    template = loader.get_template("error.html")
    
    # Set context values
    context_values = {
        "number": "503",
        "message": "This page is unavailable for some reason :/ (probably working on it)"
    }
    
    # Return response
    return http.HttpResponse(template.render(context_values, request), status=503)