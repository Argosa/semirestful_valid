from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('addshow', views.addshow),
    path('process_show', views.process_show),
    path('<int:my_int>', views.show_detail),
    path('<int:my_int>/delete', views.delete_record),
    path('<int:my_int>/edit', views.edit_record),
    path('<int:my_int>/process_edit',views.process_edit),
]