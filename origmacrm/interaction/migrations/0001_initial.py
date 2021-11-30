# Generated by Django 3.2.8 on 2021-11-30 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.CharField(choices=[('bundle', 'Bundle'), ('overstock', 'Overstock'), ('closeout', 'Closeout'), ('special price', 'Special Price')], max_length=50, verbose_name='Campaign')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('description', models.TextField(verbose_name='Description')),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('negotiating', 'Negotiating'), ('won', 'Won'), ('lost', 'Lost')], max_length=50, verbose_name='Status')),
                ('origin', models.CharField(choices=[('promotion', 'Promotion'), ('email', 'Email'), ('outbound call', 'Outbound Call'), ('referral', 'Referral'), ('inbound call', 'Inbound Call'), ('event', 'Event')], max_length=50, verbose_name='Origin')),
                ('expected_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Expected Sales')),
                ('realized_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Realized Sales')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('notes', models.TextField(verbose_name='')),
                ('expected_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Expected Sales')),
                ('realized_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Realized Sales')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_business_client', to='customer.customer', verbose_name='Business')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_direct_contact', to='customer.contact', verbose_name='Contact')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interaction.initiative', verbose_name='Initiative')),
                ('involved_contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_additional_contacts', to='customer.customer', verbose_name='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('notes', models.TextField(verbose_name='')),
                ('expected_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Expected Sales')),
                ('realized_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Realized Sales')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_business_client', to='customer.customer', verbose_name='Business')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interaction_direct_contact', to='customer.contact', verbose_name='Contact')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interaction.initiative', verbose_name='Initiative')),
                ('involved_contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_additional_contacts', to='customer.customer', verbose_name='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
