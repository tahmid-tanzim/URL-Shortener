from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from api.models import TinyURL


def retrieve(request, code):
    try:
        url = TinyURL.objects.get(short_code=code)
        return redirect(url.main_url)
    except TinyURL.DoesNotExist:
        return HttpResponse("Sorry! Invalid Tiny URL Code")



