# Generated by Django 4.2.5 on 2023-10-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('members', '0001_initial'), ('members', '0002_alter_date_date'), ('members', '0003_member_slug'), ('members', '0004_alter_member_slug')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='members')),
                ('dates', models.ManyToManyField(blank=True, related_name='activity', to='members.date')),
                ('specializations', models.ManyToManyField(related_name='member', to='members.specialization')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
