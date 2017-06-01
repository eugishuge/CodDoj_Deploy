from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^quotes$', views.quotes, name = 'quotes'),
    url(r'^contribute$', views.contribute, name = 'contribute'),
    url(r'^favorites/(?P<_qid>\d+)$', views.favorites, name = 'favorites'),
    url(r'^user_info/(?P<_id>\d+)$', views.user_info, name = 'user_info'),
    # url(r'^go_add$', views.go_add, name = 'go_add'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^remove/(?P<_qid>\d+)$', views.remove, name = 'remove'),
]
