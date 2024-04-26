from django.contrib.auth import logout as v_logout

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm, LoginForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user}")
            return redirect("app:index")

    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "userauths/login.html", context)


def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Registered as '{username}'. Now log in.")
            return redirect("userauths:login")
    else:
        form = SignupForm()
    return render(request, "userauths/register.html", {
        "form": form,
    })


#

def logout(request):
    v_logout(request)
    messages.warning(request, "Logged out.")
    return redirect("app:splash")
