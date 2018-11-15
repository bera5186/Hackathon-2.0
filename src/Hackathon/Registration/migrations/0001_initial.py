# Generated by Django 2.1 on 2018-11-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('ContactAddress', models.CharField(max_length=100)),
                ('EmailId', models.EmailField(max_length=100)),
                ('CompanyName', models.CharField(max_length=200)),
                ('SecurityQuestion', models.CharField(max_length=200)),
                ('SecurityAnswer', models.CharField(max_length=200)),
                ('UserImage', models.ImageField(upload_to='')),
            ],
        ),
    ]