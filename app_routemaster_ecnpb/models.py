from django.db import models

# Create your models here.



#done
class TsECNPBEcn(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    ecnName = models.CharField("ECN NAME", max_length=64, blank=False, null=False)
    
    def __str__(self):
        return u"%s"%(self.ecnName)
    class Meta:
        db_table = u'ts_ecnpb_ecn'
        ordering = ['date_added']
        unique_together = ( "ecnName", )

#done
class TsECNPBPrimeBroker(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    pbName = models.CharField("PB NAME", max_length=64, blank=False, null=False)
    def __str__(self):
        return u"%s"%(self.pbName)
    class Meta:
        db_table = u'ts_ecnpb_primebroker'
        ordering = ['date_added']
        unique_together = ( "pbName", )
	

#done
class TsECNPBClients(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_ecn = models.ForeignKey(TsECNPBEcn, on_delete=False)
    fk_pb = models.ForeignKey(TsECNPBPrimeBroker, on_delete=False)
    incomingValue = models.CharField(max_length=64, blank=False, null=False)
    mappedValue = models.CharField(max_length=64, blank=False, null=False)
    name = models.CharField("Name", max_length=128, blank=True, null=False)

    def __str__(self):
        return u"%s"%(self.name)
    class Meta:
        db_table = u'ts_ecnpb_client'
        ordering = ['date_added']
        unique_together = ( "name", )
        verbose_name='Ts ecnpb client'
        verbose_name_plural='Ts ecnpb clients'



#done
class TsECNPBExecutingBroker(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_ecn = models.ForeignKey(TsECNPBEcn, on_delete=False)
    fk_pb = models.ForeignKey(TsECNPBPrimeBroker, on_delete=False)
    incomingValue = models.CharField(max_length=64, blank=False, null=False)
    mappedValue = models.CharField(max_length=64, blank=False, null=False)
    name = models.CharField("EB Name", max_length=128, blank=True, null=False)
    def __str__(self):
        return u"%s"%(self.name)
    class Meta:
        db_table = u'ts_ecnpb_executingbroker'
        ordering = ['date_added']
        #unique_together = ( "fk_ecn","fk_pb", )
