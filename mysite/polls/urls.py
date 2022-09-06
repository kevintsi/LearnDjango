from django.urls import path

from . import views

app_name = 'polls'  # Espace de nom utilisée

# pk (primary key) pour les vues générique
# <type:name_variable> pour autres vues

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
