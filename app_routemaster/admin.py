from django.contrib import admin

from .models import *

# --------------------------------------------------------
#   Vendor admin system
# --------------------------------------------------------
class TsTransformPrefixInline(admin.TabularInline):
    model = TsTransformPrefix
    extra = 1
class TsVendorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [ 'name','is_payg' ,'is_multi_adapter']})
    ]
    inlines = [TsTransformPrefixInline]
    list_display = ('name', 'is_payg', 'date_added')
    search_fields = ['name']


# --------------------------------------------------------
#   Client admin system
# --------------------------------------------------------
#
# This section is the magic that allows us to have the
# funky all-in-one page for client editing.
#
class TsRouteInline(admin.TabularInline):
    model = TsRoute
    extra = 1 
class TsAuNoteInline(admin.TabularInline):
    model = TsAuNote
    extra = 1
class TsIpRuleInline(admin.TabularInline):
    model = TsIpRule
    extra = 1
    fieldsets = [
        (None, {'fields': [ 'host_ip'
                          , 'comment'
                          ]
               }
        )
    ]
class TsAggUserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': [ 'client_id'
			   , 'fk_customer'
                           , 'password'
                           , 'account_type'
                           , 'is_enabled'
                           , 'use_tokens'
                           , 'allow_publishing'
                           , 'pb_workflow_client'
                           , 'zero_footprint_client'
                           , 'isDR'
                           , 'notes'
                           ]
                }
        )
    ]
    inlines = [TsIpRuleInline,TsRouteInline,TsAuNoteInline]
    list_display = ('client_id', 'fk_customer', 'is_enabled', 'pb_workflow_client', 'zero_footprint_client')
    list_filter = ('is_enabled', 'use_tokens', 'isDR', 'pb_workflow_client','zero_footprint_client')
    search_fields = ['client_id','fk_customer__name' ]
    save_as=True


class TsCustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':   [ 'name'
                            , 'support_center_id'
                            , 'is_consumer'
                            ]
                }
        )
    ]
	
    list_display = ('name', 'support_center_id','is_consumer','date_added')
    search_fields = ['name','support_center_id' ]

class TsRouteAdmin(admin.ModelAdmin):
  
    fieldsets = [
        (None,  {'fields': [ 'route_id'
                            ,'fk_vendor'
                            ,'fk_client'
                           ]
                }
         )
    ]
    list_display = ('route_id','fk_client','fk_vendor','date_added')
    search_fields = ['route_id','fk_client__client_id' ]
    list_filter = ( 'fk_vendor', 'fk_client')
    save_as=True

class TsTransformPrefixAdmin(admin.ModelAdmin):
    fieldsets = [
		(None,  {'fields': [ 'value'
		                    ,'fk_vendor'
				    ,'generate_route_file'
		                   ]
		        }
		 )
    ]    
    search_fields = ['value','fk_vendor__name' ]
    list_display = ('value','fk_vendor','date_added')

   

class TsContactsAdmin(admin.ModelAdmin):
    fieldsets = [
		(None,  {'fields': [ 'email'
		                    ,'fk_customer'
		                   ]
		        }
		 )
    ]  
    list_display = ('email','fk_customer')
    

# --------------------------------------------------------
#   Ip admin system
# --------------------------------------------------------
class TsIpRuleAdmin(admin.ModelAdmin):
    model = TsIpRule
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
    search_fields = ['host_ip','fk_client__client_id' ]



# --------------------------------------------------------
#   Direct entity administration
# --------------------------------------------------------
admin.site.register(TsAggUser, TsAggUserAdmin)
admin.site.register(TsVendor, TsVendorAdmin)
admin.site.register(TsRoute, TsRouteAdmin)
admin.site.register(TsCustomer, TsCustomerAdmin)
admin.site.register(TsIpRule, TsIpRuleAdmin)
admin.site.register(TsTransformPrefix,TsTransformPrefixAdmin)
admin.site.register(TsContacts, TsContactsAdmin)
admin.site.register(TsAuNote)


