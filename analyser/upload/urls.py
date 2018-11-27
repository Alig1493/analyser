from django.conf.urls import url

from .views import UploadView, FileListView


urlpatterns = [
    url(r'^$', FileListView.as_view(), name='files-list'),
    url(r'^upload/$', UploadView.as_view(), name='files-upload'),
]
