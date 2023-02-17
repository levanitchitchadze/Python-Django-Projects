from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns=[
    path('Registration',  views.RegPage),
    # path('',  auth_view.LoginView.as_view(template_name='HTML/LoginPage.html'),name="Login"),
    path('',  views.LoginPage),
    path('Account/',  views.ChatPage),
    path('About/',  views.AboutPage),
    path('Contact/',  views.ContactFunction),
    path('ProfileEdit/',  views.ProEditPage),
    path('test/',  views.TestHtml),

    path('Service/',  views.ServicesPage),

]