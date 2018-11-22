from django.contrib import admin
from django import forms

from .models import *


# --------------------------------------------------------
#   Model Admin Pages
# --------------------------------------------------------
    

class TsSTDIpRuleAdmin(admin.ModelAdmin):
    model = TsSTDIpRule
    extra = 1
    fieldsets = [
        (None, {'fields': [ 'fk_client'
			  ,'host_ip'
                          , 'comment'
                          ]
               }
        )
    ]

    list_display = ('host_ip', 'fk_client', 'comment', 'date_added')
    #Note: to search for a value in a related table - use the 'follow' (double underscrore) notation as in 'fk_client__client_id'
    search_fields = ['host_ip', 'fk_client__compId' ]

    
class TsSTDRouteAdmin(admin.ModelAdmin):
    model = TsSTDRoute
    extra = 1

    fieldsets = [
        (None,  {'fields': [ 'route_id'
                            ,'fk_vendor'
                            ,'fk_client'
                           ]
                }
         )
    ]
    list_display = ('route_id', 'fk_client', 'fk_vendor', 'date_added')
    search_fields = ['route_id', 'fk_client__compId']
    list_filter = ( 'fk_vendor', 'fk_client')


class TsSTDPermissionAdmin(admin.ModelAdmin):
    model = TsSTDPermission
    extra = 1
    fieldsets = [
        (None, {'fields': [ 'fk_client'
			  , 'permission_type'
			  , 'permission_value'
                          ]
               }
        )
    ]

    list_display = ( 'fk_client','get_client_type','permission_type', 'permission_value')
    #Note: to search for a value in a related table - use the 'follow' (double underscrore) notation as in 'fk_client__client_id'
    search_fields = ['permission_value', 'fk_client__compId' ]
    list_filter = ( 'permission_type','fk_client')

    def get_client_type(self, obj):
        return obj.fk_client.client_type
    get_client_type.admin_order_field  = 'fk_client'  #Allows column order sorting
    get_client_type.short_description = 'Client Type'  #Renames column head


# --------------------------------------------------------
#   Model Inline pages
# --------------------------------------------------------
    
class TsSTDRouteInlineFormset(forms.models.BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
       super(TsSTDRouteInlineFormset, self).__init__(*args, **kwargs)   
       for form in self.forms:
            for key in form.fields:
                if (key == 'route_id' or key == 'fk_vendor') and form.data.get('client_type')=='contributor':
                    form.fields[key].required = False
              
    def clean(self):
        # get forms that actually have valid data
        for form in self.forms:
            fk_vendor = form.data.get('tsstdroute_set-0-fk_vendor')
            route_id = form.data.get('tsstdroute_set-0-route_id')
            try:
                if form.data.get('client_type')=='contributor':
                    if ((fk_vendor==None or fk_vendor=='') and (route_id==None or route_id=='')):
                        pass
                    else:
                        raise forms.ValidationError('Routes cannot be added if client Type is Contributor')
                    
            except AttributeError:
                # annoyingly, if a subform is invalid Django explicity raises
                # an AttributeError for cleaned_data
                pass
        

class TsSTDRouteInline(admin.TabularInline):
    model = TsSTDRoute
    formset = TsSTDRouteInlineFormset
    extra = 1 

class TsSTDIpRuleInline(admin.TabularInline):
    model = TsSTDIpRule
    extra = 1

class TsSTDNoteInline(admin.TabularInline):
    model = TsSTDNote
    extra = 1

class TsSTDVendorInline(admin.TabularInline):
    model = TsSTDVendor
    extra = 1

class TsSTDPermissionInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        # get forms that actually have valid data
        
        for form in self.forms:
            for key in form.fields:
               #print 'form.fields[key] --> ' + form.fields[key]
              
                if key == 'permission_type' and form.data.get('client_type')=='consumer':
                    try:
                        val = form.cleaned_data[key]
                        if val == 'ip-address':
                                pass
                        else:
                                raise forms.ValidationError('%s Permission type cannot be added if Client Type is consumer' %val)
			
                    except (KeyError, AttributeError) as e:
 		     # annoyingly, if a subform is invalid Django explicity raises
                     # an AttributeError for cleaned_data
                        pass	

class TsSTDPermissionInline(admin.TabularInline):
    formset = TsSTDPermissionInlineFormset
    model = TsSTDPermission
    extra = 1

class TsSTDClientAdmin(admin.ModelAdmin):
      #list_per_page = 5
      fieldsets = [
        (None, {'fields': [ 'compId'
                          , 'name'
			  , 'client_type'
                          ]
               }
        )
      ]

      list_display = ('compId', 'name', 'client_type', 'date_added')
      #Note: to search for a value in a related table - use the 'follow' (double underscrore) notation as in 'fk_client__client_id'
      search_fields = ['compId', 'name' ]
      inlines = [TsSTDRouteInline, TsSTDIpRuleInline, TsSTDPermissionInline, TsSTDNoteInline]	
      list_filter=['client_type','name']
      	

class TsSTDTargetServerAdmin(admin.ModelAdmin):
    model = TsSTDTargetServer
    extra = 1
    fieldsets = [
        (None, {'fields': [ 'client_type'
			  , 'targetserver_ip'
			  , 'targetserver_port'
                          ]
               }
        )
    ]

    list_display = ( 'client_type','targetserver_ip','targetserver_port')
    #Note: to search for a value in a related table - use the 'follow' (double underscrore) notation as in 'fk_client__client_id'
    #search_fields = ['permission_value', 'targetserver_ip' ]

    
# --------------------------------------------------------
#   Direct entity administration
# --------------------------------------------------------
admin.site.register(TsSTDClient, TsSTDClientAdmin)
admin.site.register(TsSTDIpRule,TsSTDIpRuleAdmin)
admin.site.register(TsSTDRoute,TsSTDRouteAdmin)
admin.site.register(TsSTDNote)
admin.site.register(TsSTDVendor)
admin.site.register(TsSTDPermission,TsSTDPermissionAdmin)
admin.site.register(TsSTDTargetServer, TsSTDTargetServerAdmin)


