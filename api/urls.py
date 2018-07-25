from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('project', views.ProjectViewSet)
router.register('task_list', views.TaskListViewSet)
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
