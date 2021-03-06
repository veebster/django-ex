# Generated by Django 2.1.3 on 2018-11-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TsAggUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('client_id', models.CharField(max_length=100)),
                ('ip_address', models.CharField(default='', max_length=100, null=True)),
                ('notes', models.CharField(blank=True, max_length=10000, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('account_type', models.CharField(default='API', max_length=10)),
                ('is_enabled', models.BooleanField(default=True)),
                ('use_tokens', models.BooleanField(default=True)),
                ('allow_publishing', models.BooleanField(default=False)),
                ('ip_range', models.CharField(max_length=256)),
                ('pb_workflow_client', models.BooleanField(default=False)),
                ('zero_footprint_client', models.BooleanField(default=False)),
                ('isDR', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ts_agg_user',
                'ordering': ['client_id'],
            },
        ),
        migrations.CreateModel(
            name='TsAuNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=10000, null=True)),
                ('fk_client', models.ForeignKey(on_delete=False, to='app_routemaster.TsAggUser')),
            ],
            options={
                'db_table': 'ts_au_note',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='TsContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Ts contact',
                'verbose_name_plural': 'Ts contacts',
                'db_table': 'ts_contacts',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='TsCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True, null=True)),
                ('is_consumer', models.BooleanField(default=False)),
                ('is_venue', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('notes', models.CharField(blank=True, max_length=2000, null=True)),
                ('support_center_id', models.CharField(max_length=56, null=True)),
            ],
            options={
                'db_table': 'ts_customer',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TsIpRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('host_ip', models.CharField(max_length=1000)),
                ('comment', models.CharField(max_length=256, null=True)),
                ('fk_client', models.ForeignKey(on_delete=False, to='app_routemaster.TsAggUser')),
            ],
            options={
                'db_table': 'ts_ip_rule',
                'ordering': ['fk_client'],
            },
        ),
        migrations.CreateModel(
            name='TsRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('route_id', models.CharField(max_length=200)),
                ('fk_client', models.ForeignKey(on_delete=False, to='app_routemaster.TsAggUser')),
            ],
            options={
                'db_table': 'ts_route',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='TsTransformPrefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('value', models.CharField(blank=True, max_length=50, null=True)),
                ('generate_route_file', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Ts transform prefix',
                'verbose_name_plural': 'Ts transform prefixes',
                'db_table': 'ts_transform_prefix',
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='TsVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('is_multi_adapter', models.BooleanField(default=False)),
                ('is_payg', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ts_vendor',
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='tsvendor',
            unique_together={('name',)},
        ),
        migrations.AddField(
            model_name='tstransformprefix',
            name='fk_vendor',
            field=models.ForeignKey(on_delete=False, to='app_routemaster.TsVendor'),
        ),
        migrations.AddField(
            model_name='tsroute',
            name='fk_vendor',
            field=models.ForeignKey(on_delete=False, to='app_routemaster.TsVendor'),
        ),
        migrations.AlterUniqueTogether(
            name='tscustomer',
            unique_together={('name', 'is_consumer', 'is_venue')},
        ),
        migrations.AddField(
            model_name='tscontacts',
            name='fk_customer',
            field=models.ForeignKey(on_delete=False, to='app_routemaster.TsCustomer'),
        ),
        migrations.AddField(
            model_name='tsagguser',
            name='fk_customer',
            field=models.ForeignKey(on_delete=False, to='app_routemaster.TsCustomer'),
        ),
        migrations.AlterUniqueTogether(
            name='tstransformprefix',
            unique_together={('value',)},
        ),
        migrations.AlterUniqueTogether(
            name='tsroute',
            unique_together={('route_id', 'fk_vendor', 'fk_client')},
        ),
        migrations.AlterUniqueTogether(
            name='tsagguser',
            unique_together={('client_id',)},
        ),
    ]
