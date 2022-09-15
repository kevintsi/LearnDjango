from django.urls import path

from . import views

app_name = "authcustom"  # Espace de nom utilisée

# pk (primary key) pour les vues générique
# <type:name_variable> pour autres vues

urlpatterns = [path("login/", views.login, name="login")]
