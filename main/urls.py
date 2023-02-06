from django.conf.urls import url

from .views import index, PixelView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^main/white.jpg', PixelView.as_view(), name='tracking')
]
