import json

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request) -> HttpResponse:
    template = loader.get_template(f"root.html")
    with open("./root/pages.json", "r") as file:
        pages = json.load(file)
    
    context_values = {
        "name": "Home",
        "pages": pages
    }
    return HttpResponse(template.render(context_values, request))