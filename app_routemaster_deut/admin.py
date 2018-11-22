from django.contrib import admin

from .models import *


# --------------------------------------------------------
#   Model Inline pages
# --------------------------------------------------------

class TsDeutRouteInline(admin.TabularInline):
    model = TsDeutRoute
    extra = 1

class TsDeutIpRuleInline(admin.TabularInline):
    model = TsDeutIpRule
    extra = 1

class TsDeutNoteInline(admin.TabularInline):
    model = TsDeutNote
    extra = 1

class TsDeutClientsAdmin(admin.ModelAdmin):
      
      fieldsets = [
        (None, {'fields': [ 'compId'
                          , 'name'
			  ]
               }
        )
      ]
      inlines = [TsDeutRouteInline, TsDeutIpRuleInline,TsDeutNoteInline]
      list_display = ('compId', 'name','dateAdded')
      search_fields = ['compId']
      list_filter =  ['compId']
      

class TsDeutClientsAdminTest(admin.ModelAdmin):
      list_per_page = 5
      


# --------------------------------------------------------
#   Model Admin Pages
# --------------------------------------------------------
    

class TsDeutIpRuleAdmin(admin.ModelAdmin):
    model = TsDeutIpRule
    extra = 1
    fieldsets = [
        (None, {'fields': [ 'fk_client','host_ip'
                          , 'comment'
                          ]
               }
        )
    ]

    list_display = ('host_ip', 'fk_client', 'comment', 'date_added')
    #Note: to search for a value in a related table - use the 'follow' (double underscrore) notation as in 'fk_client__client_id'
    search_fields = ['host_ip', 'fk_client__compId' ]
    list_filter = ( 'fk_client',)
    
class TsDeutRouteAdmin(admin.ModelAdmin):
    model = TsDeutRoute
    extra = 1

    fieldsets = [
        (None,  {'fields': [ 'routeId',
			     'fk_client',
                             'routingStatus'
                           ]
                }
         )
    ]
    list_display = ('routeId', 'fk_client', 'dateAdded')
    search_fields = ['routeId', 'fk_client__compId']
    list_filter =  ['fk_client']

    
class TsDeutTargetServerAdmin(admin.ModelAdmin):
    model = TsDeutTargetServer
    extra = 1

    fieldsets = [
        (None,  {'fields': [ 'targetserver_ip'
			    , 'targetserver_port'
                           ]
                }
         )
    ]
    list_display = ('targetserver_ip', 'targetserver_ip', 'date_added')
    

# --------------------------------------------------------
#   Direct entity administration
# --------------------------------------------------------
admin.site.register(TsDeutRoute,TsDeutRouteAdmin)
admin.site.register(TsDeutClients, TsDeutClientsAdmin)
admin.site.register(TsDeutIpRule,TsDeutIpRuleAdmin)
admin.site.register(TsDeutNote)
admin.site.register(TsDeutTargetServer, TsDeutTargetServerAdmin)



