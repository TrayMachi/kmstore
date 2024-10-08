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
from itertools import chain
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url="/login")
def show_main(request):
    keyboard_mouse_all = list(chain(Keyboard.objects.all(), Mouse.objects.all()))
    context = {
        "title": "KMStore",
        "name": "Tristan Agra Yudhistira",
        "npm": "2306245112",
        "class": "PBP D",
        "current_user": request.user.username,
        "last_login": request.COOKIES["last_login"],
        "keyboard_mouse_all": keyboard_mouse_all,
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
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response


@login_required(login_url="/login")
def create_keyboard(request):
    form = KeyboardForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        keyboard = form.save(commit=False)
        keyboard.author = request.user
        keyboard.save()
        return redirect("main:show_main")

    return render(request, "keyboard_form.html", {"form": form})

@csrf_exempt
@require_POST
def create_keyboard_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    stock = request.POST.get("stock")
    switch = request.POST.get("switch")
    brand = request.POST.get("brand")
    image = request.POST.get("image")
    author = request.user

    keyboard = Keyboard(
        name=name,
        price=price,
        description=description,
        stock=stock,
        switch=switch,
        brand=brand,
        image=image,
        author=author,
    )

    keyboard.save()

    return HttpResponse("Keyboard has been created successfully!", status=201)

@csrf_exempt
@require_POST
def create_mouse_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    stock = request.POST.get("stock")
    dpi = request.POST.get("dpi")
    weight = request.POST.get("weight")
    brand = request.POST.get("brand")
    image = request.POST.get("image")
    author = request.user

    mouse = Mouse(
        name=name,
        price=price,
        description=description,
        stock=stock,
        dpi=dpi,
        weight=weight,
        brand=brand,
        image=image,
        author=author,
    )

    mouse.save()

    return HttpResponse("Mouse has been created successfully!", status=201)

@login_required(login_url="/login")
def create_mouse(request):
    form = MouseForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mouse = form.save(commit=False)
        mouse.author = request.user
        mouse.save()
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
    data = Keyboard.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_xml_by_id_mouse(request, id):
    data = Mouse.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_by_id_keyboard(request, id):
    data = Keyboard.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_json_by_id_mouse(request, id):
    data = Mouse.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )

@login_required(login_url="/login")
def show_json_by_author(request):
    keyboard_listings = Keyboard.objects.filter(author=request.user)
    mouse_listings = Mouse.objects.filter(author=request.user)
    data = list(chain(keyboard_listings, mouse_listings))
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )

@login_required(login_url="/login")
def delete_keyboard(request, id):
    keyboard = Keyboard.objects.get(pk=id)
    keyboard.delete()
    return redirect("main:show_main")

@login_required(login_url="/login")
def delete_mouse(request, id):
    mouse = Mouse.objects.get(pk=id)
    mouse.delete()
    return redirect("main:show_main")

def edit_keyboard(request, id):
    keyboard = Keyboard.objects.get(pk=id)
    form = KeyboardForm(request.POST or None, instance=keyboard)

    if form.is_valid() and request.method == "POST":
        keyboard = form.save(commit=False)
        keyboard.author = request.user
        keyboard.save()
        return redirect("main:show_main")

    return render(request, "keyboard_form.html", {"form": form})

def edit_mouse(request, id):
    mouse = Mouse.objects.get(pk=id)
    form = MouseForm(request.POST or None, instance=mouse)

    if form.is_valid() and request.method == "POST":
        mouse = form.save(commit=False)
        mouse.author = request.user
        mouse.save()
        return redirect("main:show_main")

    return render(request, "mouse_form.html", {"form": form})