from . import views
from django.urls import path

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('', views.index),
#     path('success', views.success),
#     path('register', views.register),
#     path('success', views.success),
# ]

# for reg
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success)
]