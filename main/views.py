from django.http import HttpResponse
from django.shortcuts import redirect, render
from main.models import Keyboard, Mouse
from main.forms import KeyboardForm, MouseForm
from django.core import serializers

# Create your views here.
def show_main(request):
    context = {
        'title': 'KMStore',
        'name': 'Tristan Agra Yudhistira',
        'npm' : '2306245112',
        'class': 'PBP D',
        "keyboards": Keyboard.objects.all(),
        "mouse": Mouse.objects.all(),
    }

    return render(request, "main.html", context)

def create_keyboard(request):
    form = KeyboardForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    
    return render(request, "keyboard_form.html", {"form": form}) 

def create_mouse(request):
    form = MouseForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    
    return render(request, "mouse_form.html", {"form": form})

def show_xml_keyboard(request):
    data = Keyboard.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_mouse(request):
    data = Mouse.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_keyboard(request):
    data = Keyboard.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_mouse(request):
    data = Mouse.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id_keyboard(request, id):
    data = Keyboard.objects.get(id=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id_mouse(request, id):
    data = Mouse.objects.get(id=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id_keyboard(request, id):
    data = Keyboard.objects.get(id=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id_mouse(request, id):
    data = Mouse.objects.get(id=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")