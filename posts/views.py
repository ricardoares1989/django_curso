"""Posts views"""

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# utilities
from datetime import datetime

# Create your views here.

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name':'Yesica Cortes',
            'picture': 'https://i.picsum.photos/id/1036/200/200.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/1036/200/200.jpg',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name':'C. Vander',
            'picture': 'https://picsum.photos/200/200/?image=903',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name':'Thespianartist',
            'picture': 'https://picsum.photos/200/200/?image=1076',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1076',
    }
]
@login_required
def list_posts(request):
    """list existing posts."""
    
    return render(request, 'posts/feed.html', {'posts': posts})
