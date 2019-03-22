from django.conf.urls import url, include
from todolist_rest import views

urlpatterns = [
    url(r'^todos/$', views.TodoList.as_view()),
    url(r'^todos/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view()),
]
