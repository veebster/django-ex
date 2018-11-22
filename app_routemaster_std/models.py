from django.db import models

# Create your models here.

class TsSTDClient(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    compId = models.CharField(max_length=64, blank=False, null=False)
    name = models.CharField(verbose_name='Client name', max_length=128, blank=False, null=False)
    client_type  = models.CharField(max_length=15, blank=False, null=True, choices=[('contributor', 'contributor'),('consumer', 'consumer')])

    def __str__(self):
        return u" %s => %s"%(self.name, self.compId)
    class Meta:
        db_table = u'ts_std_clients'
        ordering = ['date_added']
        unique_together = ( "name", "compId")

class TsSTDVendor(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return u"%s"%self.name
    class Meta:
        db_table = u'ts_std_vendor'
        ordering = ['name']
        unique_together = ( ("name"), )


class TsSTDRoute(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_vendor = models.ForeignKey(TsSTDVendor, on_delete=False)
    fk_client = models.ForeignKey(TsSTDClient, on_delete=False)
    route_id = models.CharField(max_length=64, blank=False, null=False)
    
    def __str__(self):
        return u"%s (%s)"%(self.route_id, self.date_added)
    class Meta:
        db_table = u'ts_std_route'
        ordering = ['date_added']
        unique_together = ( "route_id","fk_vendor","fk_client" )


class TsSTDIpRule(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_client = models.ForeignKey(TsSTDClient, on_delete=False)
    host_ip = models.CharField(max_length=30, null=False,blank = False)
    comment = models.CharField(max_length=2000, null=True,blank=True)

    def __str__(self):
        return u"%s | %s"%( self.fk_client.name, self.host_ip)
    class Meta:
        db_table = u'ts_std_ip_rule'
        ordering = ['host_ip']
        unique_together = ( ("host_ip", "fk_client"), )

class TsSTDNote(models.Model):
    """A change note against an entry in the client table. We
    use this so that we can clearly indicate who is making
    which change."""
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_client = models.ForeignKey(TsSTDClient, on_delete=False)
    notes = models.CharField(max_length=10000, blank=True, null=True)

    def __str__(self):
        return u"[%s] %s"%(self.date_added, self.notes)
    class Meta:
        db_table = u'ts_std_note'
        ordering = ['-date_added']


class TsSTDPermission(models.Model):
     date_added = models.DateField(auto_now_add=True, blank=False, null=False)
     fk_client = models.ForeignKey(TsSTDClient, on_delete=False)
     permission_type = models.CharField(max_length=20, null=True, blank = False, choices=[('cn-name', 'cn-name'),('ip-address', 'ip-address'),('executing-system', 'executing-system')])
     permission_value = models.CharField(max_length=100, null=False,blank = False)
     #notes = models.CharField(max_length=10000, blank=True, null=True)
	
     def __str__(self):
        return u"%s => %s"%(self.permission_type, self.permission_value)
     class Meta:
        db_table = u'ts_std_permission'
        ordering = ['-date_added']


class TsSTDTargetServer(models.Model):
     date_added = models.DateField(auto_now_add=True, blank=False, null=False)
     client_type  = models.CharField(max_length=15, blank=False, null=True, choices=[('contributor', 'contributor'),('consumer', 'consumer')])
     targetserver_ip = models.CharField(max_length=100, null=False,blank = False)
     targetserver_port = models.CharField(max_length=100, null=False,blank = False)
	
     def __str__(self):
        return u"%s => %s"%(self.targetserver_ip, self.targetserver_port)
     class Meta:
        db_table = u'ts_std_targetserver'
        ordering = ['-date_added']




