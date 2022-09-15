from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as logging
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

from authcustom.forms import LoginForm

# Create your views here.


def login(request):
    try:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    logging(request, user)
                    return HttpResponseRedirect(reverse("polls:index"))
                else:
                    raise ValidationError("Wrong password or email")
        else:
            form = AuthenticationForm()
            return render(request, "authcustom/login_page.html", {"form": form})
    except ValidationError as ex:
        return render(
            request,
            "authcustom/login_page.html",
            {"error_message": ex.message, "form": form},
        )
