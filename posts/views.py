"""Posts views"""

# Django
# from django.shortcuts import render
from django.http import HttpResponse

# utilities
from datetime import datetime

# Create your views here.

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.picsum.photos/id/1036/200/200.jpg',
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]

def list_posts(requests):
    """list existing posts."""
    content = []
    for post in posts:
            content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
            """.format(**post)
            )
    return HttpResponse('<br>'.join(content))
    # Unimos toda nuestra etiqueta en un solo string.
