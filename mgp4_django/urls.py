from django.core.urlresolvers import reverse_lazy
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    # Examples:
    # url(r'^$', 'mgp4_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^transport/', include('transport.urls', namespace='transport')),
    url(r'^places/', include('places.urls', namespace='places')),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('transport:map'))),
]
