from django.contrib import admin
from Thekillers.gestion.Gestionjuegos.models import (usuario,consola,room)

# Register your models here.

admin.site.register(usuario)
admin.site.register(consola)
admin.site.register(room)
