from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

import notifications.urls


admin.site.site_header = 'Administration'                    # default: "Django Administration"
admin.site.index_title = 'administration'                 # default: "Site administration"
admin.site.site_title = 'Analysis admin' # default: "Django site admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path("misc/", include("misc.urls")),

    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# add media support
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
