from django.db import models

class TsDeutClients(models.Model):
    dateAdded = models.DateField(auto_now_add=True, blank=False, null=False)
    compId = models.CharField(max_length=64, blank=False, null=False)
    name = models.CharField("Description", max_length=128, blank=False, null=False)
    def __str__(self):
        return u"%s (%s)"%(self.name, self.compId)
    class Meta:
        db_table = u'ts_deut_clients'
        ordering = ['dateAdded']
        unique_together = ( "compId", )
        verbose_name='Ts deut client'
        verbose_name_plural='Ts deut clients'

class TsDeutRoute(models.Model):
    dateAdded = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_client = models.ForeignKey(TsDeutClients, on_delete=False)
    routeId = models.CharField(max_length=64, blank=False, null=False)
    routingStatus  = models.CharField(max_length=5, blank=False, null=True, choices=[('relay', 'relay'),('proxy', 'proxy'),('both', 'both')])
    
    def __str__(self):
        return u"%s (%s)"%(self.routeId, self.dateAdded)
    class Meta:
        db_table = u'ts_deut_routes'
        ordering = ['dateAdded']
        unique_together = ( "routeId", )


class TsDeutIpRule(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_client = models.ForeignKey(TsDeutClients, on_delete=False)
    host_ip = models.CharField(max_length=30, null=False)
    comment = models.CharField(max_length=2000, null=True,blank=True)

    def __str__(self):
        return u"%s | %s"%( self.fk_client.name, self.host_ip)
    class Meta:
        db_table = u'ts_deut_ip_rule'
        ordering = ['host_ip']

class TsDeutNote(models.Model):
    """A change note against an entry in the client table. We
    use this so that we can clearly indicate who is making
    which change."""
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_client = models.ForeignKey(TsDeutClients, on_delete=False)

    notes = models.CharField(max_length=10000, blank=True, null=True)
    def __str__(self):
        return u"[%s] %s"%(self.date_added, self.notes)
    class Meta:
        db_table = u'ts_deut_note'
        ordering = ['-date_added']


class TsDeutTargetServer(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    targetserver_ip = models.CharField(max_length=100, null=False,blank = False)
    targetserver_port = models.CharField(max_length=100, null=False,blank = False)
	
    def __str__(self):
        return u"%s => %s"%(self.targetserver_ip, self.targetserver_port)
    class Meta:
        db_table = u'ts_deut_targetserver'
        ordering = ['-date_added']
        verbose_name='Ts deut targetserver'
        verbose_name_plural='Ts deut targetserver'


