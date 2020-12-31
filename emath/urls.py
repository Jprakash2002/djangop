from django.urls import path
from . import views
app_name='emath'
urlpatterns=[
    path('',views.index,name='index'),
    path('root',views.root,name='root'),
    path('quadratic',views.quadratic,name='quadratic'),
    path('cubic',views.cubic,name='cubic')
]