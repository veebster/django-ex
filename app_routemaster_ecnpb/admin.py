from django.contrib import admin

from .models import *


# --------------------------------------------------------
#   Model Admin Pages
# --------------------------------------------------------
class TsECNPBClientsAdmin(admin.ModelAdmin):
  list_display = ('incomingValue','mappedValue','fk_ecn', 'fk_pb','date_added')
  search_fields = ['fk_ecn__ecnName','fk_pb__pbName' ]
  list_filter = ( 'fk_ecn','fk_pb','mappedValue')


class TsECNPBExecutingBrokerAdmin(admin.ModelAdmin):
  list_display = ('incomingValue','mappedValue','fk_ecn', 'fk_pb','date_added')
  search_fields = ['fk_ecn__ecnName','fk_pb__pbName' ]
  list_filter = ( 'fk_ecn','fk_pb','mappedValue')


# --------------------------------------------------------
#   Direct entity administration
# --------------------------------------------------------
admin.site.register(TsECNPBClients, TsECNPBClientsAdmin)
admin.site.register(TsECNPBEcn)
admin.site.register(TsECNPBPrimeBroker)
admin.site.register(TsECNPBExecutingBroker,TsECNPBExecutingBrokerAdmin)





