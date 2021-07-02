from django.urls import path
from .views import get_photos_album

urlpatterns = [
    path('album-photos/<slug:pk>', get_photos_album, name='album_photos'),
]
