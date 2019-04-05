from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'home'),
    url(r'^awardo/profile$',views.profile,name='displayProfile'),
    url(r'^awards/prof/(\d+)',views.prof,name="prof"),
    url(r'^project',views.project,name="project"),
    url(r'^awards/more/(\d+)',views.more,name="more"),
    url(r'^awards/vote/(\d+)',views.vote,name="vote"),
    url(r'^search/', views.search,name='search_project'),
    url(r'^api/merch/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)