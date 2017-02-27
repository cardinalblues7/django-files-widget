from django.conf.urls import url

import topnotchdev.files_widget.views as widget_views

urlpatterns = [
    url(u'^upload/$', widget_views.upload, name="files_widget_upload"),
    url(u'^thumbnail-url/$', widget_views.thumbnail_url, name="files_widget_get_thumbnail_url"),
]
