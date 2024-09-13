from django.forms import ModelForm
from main.models import Keyboard, Mouse


class KeyboardForm(ModelForm):
    class Meta:
        model = Keyboard
        fields = ["name", "price", "stock", "switch", "brand", "image", "description"]
        labels = {
            "name": "Name",
            "price": "Price",
            "description": "Description",
            "stock": "Stock",
            "switch": "Switch",
            "brand": "Brand",
            "image": "Image",
        }

class MouseForm(ModelForm):
    class Meta:
        model = Mouse
        fields = ["name", "price", "stock", "dpi", "weight", "brand", "image", "description"]
        labels = {
            "name": "Name",
            "price": "Price",
            "description": "Description",
            "stock": "Stock",
            "dpi": "DPI",
            "weight": "Weight",
            "brand": "Brand",
            "image": "Image",
        }

