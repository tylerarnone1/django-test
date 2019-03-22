from django.conf.urls import url
from main_app import views

# SET THE NAMESPACE!
app_name = 'main_app'

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
