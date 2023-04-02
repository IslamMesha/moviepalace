from django.urls import path

from moviefacts.views import citizen_kane, casablanca, maltese_falcon, psycho, listing

urlpatterns = [
    path("citizen-kane/", citizen_kane),
    path("casablanca/", casablanca),
    path("maltese-falcon/", maltese_falcon),
    path("psycho/", psycho),
    path("listing/", listing),
]
