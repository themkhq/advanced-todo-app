from django.urls import path


from .views import (
    register,
    user_login,
    user_logout,
    home,
    task_create,
    task_detail,
    task_delete,
)


urlpatterns = [
    # Authentication
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    # Tasks
    path("", home, name="home"),
    path("tasks/<int:task_id>/", task_detail, name="task_detail"),
    path("delete/<int:task_id>/", task_delete, name="delete"),
    path("create/", task_create, name="create"),
]
