from django.conf.urls import url


from .views import index, tracking

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^static/main/white.jpg', tracking, name='tracking')
]