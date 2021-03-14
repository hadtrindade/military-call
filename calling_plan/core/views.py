from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from calling_plan.decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("pages:home")

    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("core:login")


@login_required(login_url="core:login")
@allowed_users(allowed_roles=["admin"])
def register_view(request):

    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"forms": form}
    return render(request, "registration/register.html", context=context)
