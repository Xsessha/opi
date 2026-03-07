from django.shortcuts import render
from .models import User, Media


def home(request):

    user = User(
        first_name='Xseniia',
        last_name='Olkhovska',
        description='Designer'
    )

    context = {
        'user': user
    }

    return render(request, 'blog/home.html', context)


def media_page(request):

    media = Media(
        title='Dark Woods',
        description='A group of friends enters an old forest. Soon they realize something is watching them in the dark.',
        rating=9,
        studio_name='Nightmare Studio',
       

    )

    context = {
        'media': media
    }

    return render(request, 'blog/media.html', context)