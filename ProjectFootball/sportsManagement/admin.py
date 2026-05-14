from django.contrib import admin
from .models import Player
from .models import Team
from .models import Finance

# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Finance)

