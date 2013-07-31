from django.conf.urls import patterns, include, url
import usermanager.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'codefellows.views.home', name='home'),
	# url(r'^codefellows/', include('codefellows.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),
	url(r'^$', usermanager.views.ListUserView.as_view(),
		name='user-list',),

	url(r'^new$', usermanager.views.CreateUserView.as_view(),
		name='user-new',),

	url(r'^edit/(?P<pk>\d+)/$', usermanager.views.UpdateUserView.as_view(),
		name='user-edit',),

    url(r'^delete/(?P<pk>\d+)/$', usermanager.views.DeleteUserView.as_view(),
        name='user-delete',),
)
