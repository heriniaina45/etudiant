from django.contrib import admin
from django.urls import path
from etudiant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.affiche, name = "afficher"),
    path('delete/<int:id>', views.delete, name = "deletedata"),
    path('<int:id>/', views.modifier, name = "modifierdata")
]
