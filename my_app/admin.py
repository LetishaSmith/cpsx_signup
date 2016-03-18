from django.contrib import admin
from my_app.models import Room, Participant


# Register your models here.
class roomInlines(admin.TabularInline):
    model = Room
    extra = 3

class RoomAdmin(admin.ModelAdmin):
    fields = ['room','key']
    list_display = ('room','key')
    #inlines = [roomInlines]

# associates user room with admin
#admin.site.register(Room,RoomAdmin)
admin.site.register(Room,RoomAdmin)

# hashed out til decide if room in participant or participant in room
#class roomInline(admin.TabularInline): #or StackedInline
    #readonly_fields = ('time_since_last_update',)
    #model = room #The model connected
    #extra = 3 #enough space for three extra Rates

from my_app.models import Participant, Room

# hashed til decide if room in participant or participant in room

    #connects room to participant
#class ParticipantAdmin(admin.ModelAdmin):
    #inlines = [roomInlines]

admin.site.register(Participant)
    # participantAdmin out of () til decide if room in participant or participant in room


