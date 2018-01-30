from django.conf.urls import url
app_name='content'

from .views import (SchoolView,
                             SchoolClassView,
                             StudentInfo,
                             GradesView,
                             StudentSearchView,
                             EditView,
                             DeleteView,
StudentAddView
                    )


urlpatterns = [
    url(r'^$', SchoolView.as_view(), name="all"),
    url(r'^class/(?P<school_class_id>(\d)+)', SchoolClassView.as_view(),
        name="school-class" ),
    url(r'^student/(?P<student_id>(\d)+)', StudentInfo.as_view(),name="student"),
    url(r'^grades/(?P<student_id>(\d)+)/(?P<subject_id>(\d)+)', GradesView.as_view(), name="grades"),
    url(r'^search/', StudentSearchView.as_view(), name="search"),
    url(r'^add/', StudentAddView.as_view(), name="add"),
    url(r"edit/(?P<pk>\d+)/$",EditView.as_view(), name="edit"),
    url(r"delete/(?P<pk>\d+)/$",DeleteView.as_view(), name="delete"),

    ]