from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage),
    path('about/',views.aboutPage,name="aboutus"),
    path('contact/',views.contactPage,name="contactus"),
    path('dashboard/',views.dashboardPage,name="dashboardus"),
    path('login/',views.loginPage,name="loginus"),
    path('signup/',views.signupPage,name="signupus"),
    path('logout/',views.logoutPage,name="logoutus"),
    path('addpost/',views.addpost,name="addpostus"),
    path('updatepost/<int:id>',views.updatepost,name="updatepostus"),
    path('deletepost/<int:id>',views.deletepost,name="deletepostus"),
]
