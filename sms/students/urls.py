from django.conf.urls import url, include

from .views import (under_contruction,
                    StudentListView,
                    StudentDetailView,
                    StudentCreateView,
                    ParentCreateView,
                    )

urlpatterns = [
    url(r'^$', StudentListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name="detail"),
    url(r'^create/$', StudentCreateView.as_view(), name="create"),
    url(r'^createparent/$', ParentCreateView.as_view(), name="createp"),
]