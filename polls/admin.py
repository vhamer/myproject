from polls.models import Poll
from django.contrib import admin

admin.site.register(Poll)
    
class PollAdmin(admin.ModelAdmin):
    # list the details of each Poll
    list_display = ('question', 'pub_date', 'was_published_today')
    #list a search field
    search_fields = ['question']
    #add drill-down by date
    date_hierarchy = 'pub_date'