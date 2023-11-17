from django.urls import path
from django.conf.urls import include

from apiv1 import views

urlpatterns = [
    path('news/', include('apiv1.news.urls')),
    path('tmp-zoom-deauth-url/', views.TmpViewForTestingZoomDeauthorizationUrl.as_view(), name='tmp_zoom_deauth_url'),
]
