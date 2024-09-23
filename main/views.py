from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from main.models import Keyboard, Mouse
from main.forms import KeyboardForm, MouseForm
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse


# Create your views here.
@login_required(login_url="/login")
def show_main(request):
    context = {
        "title": "KMStore",
        "name": "Tristan Agra Yudhistira",
        "npm": "2306245112",
        "class": "PBP D",
        "keyboards": Keyboard.objects.all(),
        "mouse": Mouse.objects.all(),
    }

    return render(request, "main.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url="/login")
def create_keyboard(request):
    form = KeyboardForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    return render(request, "keyboard_form.html", {"form": form})


@login_required(login_url="/login")
def create_mouse(request):
    form = MouseForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    return render(request, "mouse_form.html", {"form": form})


def show_xml_keyboard(request):
    data = Keyboard.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_xml_mouse(request):
    data = Mouse.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_keyboard(request):
    data = Keyboard.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_json_mouse(request):
    data = Mouse.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_xml_by_id_keyboard(request, id):
    data = Keyboard.objects.get(id=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_xml_by_id_mouse(request, id):
    data = Mouse.objects.get(id=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_by_id_keyboard(request, id):
    data = Keyboard.objects.get(id=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_json_by_id_mouse(request, id):
    data = Mouse.objects.get(id=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )
