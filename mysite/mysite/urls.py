from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # include() lie toutes les urls se trouvant dans l'application 'polls' à la route 'polls/'
    path('polls/', include('polls.urls')),
    path('auth/', include('authcustom.urls')),
    path('admin/', admin.site.urls),
]
