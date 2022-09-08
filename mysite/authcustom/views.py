from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

# Create your views here.


def login(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            raise ValidationError("Wrong password or email")
    except KeyError:
        # Réaffiche le formulaire de vote
        return render(request, 'authcustom/login_page.html')
    except ValidationError as ex:
        return render(request, 'authcustom/login_page.html', {'error_message': ex.message})
