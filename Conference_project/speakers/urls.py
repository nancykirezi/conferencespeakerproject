from django.urls import path
from . import views
app_name = 'speaker'
urlpatterns = [
      path('admin/', admin.site.urls),
    path('', views.view_speakers, name='view_speakers'),
    path('create/', views.create_speaker, name='create_speaker'),
    path('<int:speaker_id>/', views.view_one_speaker, name='view_one_speaker'),
    path('<int:speaker_id>/update/', views.update_speaker, name='update_speaker'),
    path('<int:speaker_id>/delete/', views.delete_speaker, name='delete_speaker'),
]
