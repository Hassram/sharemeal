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
    path('/newmeal',views.newmeal),
    path('/mealregister',views.mealregister),
    path('/<int:id>/delete', views.delete),
    path('/<int:id>/add', views.add),
    path('/<int:id>/remove', views.remove),
    path('/mylist',views.mylist),


]