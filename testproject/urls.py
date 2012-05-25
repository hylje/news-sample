from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from news.views import NewsApp

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r"^", include(NewsApp().urls)),
)
