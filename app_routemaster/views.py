from django.http import HttpResponse

#from ls_warehouse.app_routemaster.models import TsCollection, TsRoute

def index(request):
    sb_out = []
    sb_out.append( '<html><body>' )

    sb_out.append( 'nothing here atm - speak to craig if you want something.' )

    #c_lst = TsCollection.objects.all().order_by('name')
    #sb_out.append( "collections: %s"%', '.join( [c.name for c in c_lst] ) )

    #r_lst = TsRoute.objects.all().order_by('route_id')
    #sb_out.append( "routes: %s"%', '.join( [r.route_id for r in r_lst] ) )

    sb_out.append( '</body></html>' )

    return HttpResponse( '\n<br />\n<br />'.join(sb_out) )

