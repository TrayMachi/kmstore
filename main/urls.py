from django.urls import path
from main.views import (
    show_main,
    create_keyboard,
    create_mouse,
    show_xml_keyboard,
    show_xml_mouse,
    show_json_keyboard,
    show_json_mouse,
    show_xml_by_id_keyboard,
    show_xml_by_id_mouse,
    show_json_by_id_keyboard,
    show_json_by_id_mouse,
    register,
    login_user,
    logout_user,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create/keyboard/", create_keyboard, name="create_keyboard"),
    path("create/mouse/", create_mouse, name="create_mouse"),
    path("xml/keyboard/", show_xml_keyboard, name="show_xml_keyboard"),
    path("xml/mouse/", show_xml_mouse, name="show_xml_mouse"),
    path("json/keyboard/", show_json_keyboard, name="show_json_keyboard"),
    path("json/mouse/", show_json_mouse, name="show_json_mouse"),
    path(
        "xml/keyboard/<str:id>/",
        show_xml_by_id_keyboard,
        name="show_xml_by_id_keyboard",
    ),
    path("xml/mouse/<str:id>/", show_xml_by_id_mouse, name="show_xml_by_id_mouse"),
    path(
        "json/keyboard/<str:id>/",
        show_json_by_id_keyboard,
        name="show_json_by_id_keyboard",
    ),
    path("json/mouse/<str:id>/", show_json_by_id_mouse, name="show_json_by_id_mouse"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
