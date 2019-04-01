from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'home'),
    url(r'^awardo/profile$',views.profile,name='displayProfile'),
    url(r'^awards/prof/(\d+)',views.prof,name="prof"),
    url(r'^project',views.project,name="project"),
]