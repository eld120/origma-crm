# Generated by Django 3.2.8 on 2021-11-30 17:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.CharField(choices=[(0, 'Active'), (1, 'Inactive'), (2, 'Archived')], max_length=1, verbose_name='Activate Account')),
                ('role', models.CharField(choices=[('shipping', 'Shipping Address'), ('billing', 'Billing Address'), ('both', 'Billing/Shipping')], max_length=10, verbose_name='Role')),
                ('created_on', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('last_modified', models.DateTimeField(auto_now_add=True, verbose_name='Last Modified Date')),
                ('address_1', models.CharField(max_length=50, verbose_name='Address 1')),
                ('address_2', models.CharField(max_length=50, verbose_name='Address 2')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=50, verbose_name='State')),
                ('zip_code', models.CharField(max_length=50, verbose_name='Zip Code')),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^(\\d{10}$)', 'Please use numerical format without any spaces or special characters')], verbose_name='Phone')),
                ('country', models.CharField(max_length=2, verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('position', models.CharField(max_length=50, verbose_name='Position or Role')),
                ('description', models.TextField(verbose_name='Contact Notes')),
                ('phone_1', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^(\\d{10}$)', 'Please use numerical format without any spaces or special characters')], verbose_name='Phone 1')),
                ('phone_2', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^(\\d{10}$)', 'Please use numerical format without any spaces or special characters')], verbose_name='Phone 2')),
                ('email_1', models.EmailField(max_length=254, verbose_name='')),
                ('email_2', models.EmailField(max_length=254, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('customer', 'Customer'), ('client', 'Client'), ('vendor', 'Vendor'), ('employee', 'Employee')], max_length=50, verbose_name='Role')),
                ('dba', models.CharField(max_length=50, verbose_name='dba')),
                ('name', models.CharField(max_length=50, verbose_name='Legal Business Entity')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('active', models.CharField(choices=[(0, 'Active'), (1, 'Inactive'), (2, 'Archived')], max_length=1, verbose_name='Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('ein', models.CharField(max_length=50, verbose_name='EIN')),
                ('industry', models.CharField(choices=[('agriculture', 'Agriculture'), ('arts entertainment', 'Arts & Entertainment'), ('construction', 'Construction'), ('education', 'Education'), ('energy', 'Energy'), ('food', 'Food & Hospitality'), ('finance', 'Finance and Insurance'), ('healthcare', 'Healthcare'), ('manufacturing', 'Manufacturing'), ('mining', 'Mining'), ('other', 'Other Services'), ('services', 'Professional, Scientific, and Tech Services'), ('real estate', 'Real Estate'), ('retail', 'Retail'), ('transportation', 'Transportation & Logistics'), ('utilities', 'Utilities'), ('wholesale', 'Wholesale')], max_length=100, verbose_name='Industry')),
                ('website', models.URLField(verbose_name='Webiste')),
                ('account_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_Account', to=settings.AUTH_USER_MODEL, verbose_name='Account Manager')),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_billing', to='customer.address', verbose_name='Address')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_employee', to='customer.contact', verbose_name='Contact')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_by_customer', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_location', to='customer.address', verbose_name='Address')),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contact_employer', to='customer.customer', verbose_name='Employer'),
        ),
    ]
