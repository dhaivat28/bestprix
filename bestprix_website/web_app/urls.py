from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^search',views.search, name='search'),
	url(r'^product',views.product, name='product'),
	url(r'^login',views.login, name="login"),
	url(r'^signup',views.signup, name='signup'),
	url(r'^wishlist',views.wishlist, name='wishlist'),
	url(r'^logout',views.logout,name='logout'),
	url(r'^deletemywish',views.delete_wish,name='deletemywish')
]
