from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^$', 'demo.views.view', name='demo_view'),
)
