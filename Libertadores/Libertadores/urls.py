from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('copa/',include('copa.urls')),
    path('accounts/', include('sesion.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',TemplateView.as_view(template_name='home.html'), name='home'),
   

]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.urls import include, path
from rest_framework import routers
from quickstart import views


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
