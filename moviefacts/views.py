import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


def citizen_kane(request):
    content = """{{movie}} was released in {{year}}."""
    template = Template(content)
    context = Context({"movie": "Citizen Kane", "year": 1941})
    result = template.render(context)
    return HttpResponse(result)


def casablanca(request):
    return render(request, "simple.txt", {"movie": "Casablanca", "year": 1942})


def maltese_falcon(request):
    return render(
        request,
        "falcon.html",
        {"movie": "Maltese Falcon", "year": 1941},
    )


def psycho(request):
    data = {
        "movie": "Psycho",
        "year": 1960,
        "is_scary": True,
        "color": False,
        "tomato_meter": 96,
        "tomato_audience": 95,
    }
    return render(request, "psycho.html", data)


def listing(request):
    data = {
        "movies": [
            (
                "Citizen Kane",  # Movie name
                1941,  # Year
                datetime.date.today(),  # Release date
                datetime.datetime.now(),  # Watched date
            ),
            (
                "Casablanca",
                1942,
                datetime.date.today(),
                datetime.datetime.now(),
            ),
            (
                "Psycho",
                1960,
                datetime.date.today(),
                datetime.datetime.now(),
            ),
        ]
    }
    return render(request, "listing.html", data)
