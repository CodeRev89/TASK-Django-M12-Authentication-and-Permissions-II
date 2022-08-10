from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserRegister
from django.contrib.auth import login, logout



def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")

def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("successful-signup")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect("success-page")