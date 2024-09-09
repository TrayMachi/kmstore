from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title': 'KMStore',
        'name': 'Tristan Agra Yudhistira',
        'npm' : '2306245112',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)