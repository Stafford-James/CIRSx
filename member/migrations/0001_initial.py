# Generated by Django 3.2.13 on 2022-06-15 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aud_name', models.CharField(max_length=50, unique=True)),
                ('aud_desc', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctyp_name', models.CharField(max_length=50, unique=True)),
                ('doctyp_desc', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150)),
                ('event_start_dt', models.DateField()),
                ('event_end_dt', models.DateField()),
                ('event_location', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_path', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=250)),
                ('pub_dt', models.DateField()),
                ('doc_abs', models.TextField()),
                ('doc_txt', models.TextField()),
                ('aud_num', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.audience')),
                ('doctyp_num', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.documenttype')),
            ],
        ),
    ]