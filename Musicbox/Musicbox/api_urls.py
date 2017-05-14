from django.conf.urls import url,include
from django.contrib import admin
#from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token,refresh_jwt_token
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title="Goodreads Clone API")

urlpatterns = [
    url(r'^artists/', include("modules.Artists.urls")),
    url(r'^songs/', include("modules.Songs.urls")),
    url(r'^albums/', include("modules.Albums.urls")),
    #url(r'^auth/', obtain_jwt_token),
    #url(r'^auth/refresh', refresh_jwt_token),
    #url(r'^auth/verify', verify_jwt_token),
    #url(r'^docs/', schema_view),
]
