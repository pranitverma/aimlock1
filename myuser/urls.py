from django.conf.urls import url
from myuser import views
from miscellaneous import otpgen
app_name = "myuser"
urlpatterns = [
    url(r'^$',views.userindex),
    url(r'^addrole/$',views.addrole),
    url(r'^signup/$',views.signup),
    url(r'^fetch/$',views.fetchdata),
    url(r'^fetch1/$',views.fetchdata1),
    url(r'^delete/$',views.deletedata),
    url(r'^edit/$', views.editdata),
    url(r'^login/$',views.login),
    url(r'^updateuserpassword/$',views.updatepassword)

]