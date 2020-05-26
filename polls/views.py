from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request):
    return HttpResponse("Hello World. This is the polls index.")


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}")


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("Results page")


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("Vote Page")
