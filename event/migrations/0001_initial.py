# Generated by Django 3.2.13 on 2022-07-05 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150)),
                ('event_tag', models.CharField(max_length=250)),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('event_location', models.CharField(max_length=150)),
                ('event_venue', models.CharField(max_length=150)),
                ('venue_details', models.TextField()),
                ('venue_location', models.TextField()),
                ('venue_directions', models.TextField()),
                ('accomodations', models.TextField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise_code', models.CharField(max_length=20, unique=True)),
                ('expertise_desc', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Expertise',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=250)),
                ('web_address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=10)),
                ('bio', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('active', models.BooleanField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.country')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=10)),
                ('credentials', models.TextField()),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to=None)),
                ('active', models.BooleanField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.country')),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.expertise')),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.BooleanField()),
                ('guest_first_name', models.CharField(max_length=100, null=True)),
                ('guest_last_name', models.CharField(max_length=100, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_title', models.CharField(max_length=250)),
                ('offer_subtitle', models.CharField(max_length=250, null=True)),
                ('offer_details', models.TextField()),
                ('active', models.BooleanField()),
                ('event', models.ManyToManyField(to='event.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(to='event.Speaker'),
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(to='event.Sponsor'),
        ),
    ]