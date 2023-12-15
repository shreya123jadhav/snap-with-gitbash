from django.contrib import admin
from .models import User
from .models import Event
from .models import Ticket
from .models import Admin
from .models import User_Event_Organiser
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Admin)
admin.site.register(User_Event_Organiser)

