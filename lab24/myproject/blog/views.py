from django.shortcuts import render
from .models import User

def home(request):

    user = User(
        first_name="Kseniia",
        last_name="Olkhovska",
        description="Designer and blogger"
    )

    context = {
        "user": user
    }

    return render(request, "blog/home.html", context)