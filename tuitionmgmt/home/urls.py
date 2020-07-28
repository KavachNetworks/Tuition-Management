from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home')
    '''
    path('contact',views.contact_us,name="contactus"),
    path('signup',views.signin,name='signup'),
    path('signin',views.signup,name='signin')
    '''
]