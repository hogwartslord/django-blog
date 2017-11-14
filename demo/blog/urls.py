from django.conf.urls import url
from .views import *

app_name = 'blog'

urlpatterns = [
    url(r'^post/(?P<postid>\d+)/$',post,name='url_post'),
    url(r'^category/(?P<cid>\d+)/$',category_post,name='url_category_post'),
    url(r'^category/$',category,name='url_category'),
    url(r'^tag/(?P<tid>\d+)/$',tag_post,name='url_tag_post'),
    url(r'^tag/$',tag,name='url_tag'),
    url(r'^$', index,name='url_index'),
]



