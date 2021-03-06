from django.db import models


# --------------------------------------------------------
#   current system
# --------------------------------------------------------
class TsVendor(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=True)

    name = models.CharField(max_length=120)
    is_multi_adapter = models.BooleanField(default=False)
    is_payg = models.BooleanField(default=False)
    def __str__(self):
        return u"%s"%self.name
    class Meta:
        db_table = u'ts_vendor'
        ordering = ['name']
        unique_together = ( ("name"), )

class TsCustomer(models.Model):
    "Represents any third-party (consumer or venue)."
    date_added = models.DateField(auto_now_add=True, blank=False, null=True)
    is_consumer = models.BooleanField(default=False, null=False)
    is_venue = models.BooleanField(default=False, null=False)
    name = models.CharField(max_length=200, null=False)
    notes = models.CharField(max_length=2000, blank=True, null=True)
    support_center_id = models.CharField(max_length=56, null=True)
    
    def __str__(self):
        return u"%s (C%s|V%s)"%(self.name, self.is_consumer, self.is_venue)
    class Meta:
        db_table = u'ts_customer'
        ordering = ['name']
        unique_together = ( ("name", "is_consumer", "is_venue"), )


class TsAggUser(models.Model):
    """A much better name for this would be 'TsAggregatorAccount'. Represents
    an aggregator accountname.
    """
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    client_id = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100, default='', null=True)
    notes = models.CharField(max_length=10000, blank=True, null=True)
    password = models.CharField(max_length=100, blank=False, null=True)
    account_type = models.CharField(default='API', max_length=10)
    is_enabled = models.BooleanField(default=True, null=False)
    use_tokens = models.BooleanField(default=True, null=False)
    allow_publishing = models.BooleanField(default=False, null=False)
    ip_range = models.CharField(max_length=256, blank=False, null=False)
    fk_customer = models.ForeignKey(TsCustomer, on_delete=False)
    pb_workflow_client = models.BooleanField(default=False, null=False) 
    zero_footprint_client = models.BooleanField(default=False, null=False) 
    isDR = models.BooleanField(default=False, null=False)

    def __str__(self):
        return u"%s"%(self.client_id)
    class Meta:
        db_table = u'ts_agg_user'
        ordering = ['client_id']
        unique_together = ( ("client_id"), )

class TsAuNote(models.Model):
    """A change note against an entry in the client table. We
    use this so that we can clearly indicate who is making
    which change."""
    date_added = models.DateField(auto_now_add=True, blank=False, null=True)
    fk_client = models.ForeignKey(TsAggUser, on_delete=False)
    notes = models.CharField(max_length=10000, blank=True, null=True)
    def __str__(self):
        return u"[%s] %s"%(self.date_added, self.notes)
    class Meta:
        db_table = u'ts_au_note'
        ordering = ['-date_added']

class TsContacts(models.Model):
    fk_customer = models.ForeignKey(TsCustomer, on_delete=False)
    email = models.EmailField(max_length=100, blank=False, unique=True, null=True)
    def __str__(self):
        return u"%s"%(self.email)
    class Meta:
        db_table = u'ts_contacts'
        ordering = ['email']
        verbose_name='Ts contact'
        verbose_name_plural='Ts contacts'

class TsRoute(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    fk_vendor = models.ForeignKey(TsVendor, on_delete=False)
    fk_client = models.ForeignKey(TsAggUser, on_delete=False)

    route_id = models.CharField(max_length=200, blank=False, null=False)
    def __str__(self):
        return u"%s (%s)"%(self.route_id, self.date_added)
    class Meta:
        db_table = u'ts_route'
        ordering = ['date_added']
        unique_together = ( ("route_id", "fk_vendor", "fk_client"), )

class TsIpRule(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    host_ip = models.CharField(max_length=1000, null=False)
    fk_client = models.ForeignKey(TsAggUser, on_delete=False)
    comment = models.CharField(max_length=256, null=True)
    def __str__(self):
        return u"%s"%(self.host_ip)
    class Meta:
        db_table = u'ts_ip_rule'
        ordering = ['fk_client']

class TsTransformPrefix(models.Model):
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)
    value = models.CharField(max_length=50, blank=True, null=True)
    generate_route_file = models.BooleanField(default=True, null=False)
    fk_vendor = models.ForeignKey(TsVendor, null=False, on_delete=False)
    def __str__(self):
        return u"%s"%self.value
    class Meta:
        db_table = u'ts_transform_prefix'
        ordering = ['value']
        # Having the value unique is quite deliberate - otherwise it will
        # break historical billing data.
        unique_together = ( ("value"), )
        verbose_name='Ts transform prefix'
        verbose_name_plural='Ts transform prefixes'
