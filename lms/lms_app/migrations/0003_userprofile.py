# Generated by Django 4.0.1 on 2022-02-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.FileField(upload_to='documents/profile/')),
                ('citizenship_url', models.FileField(upload_to='documents/citizenship/')),
            ],
            options={
                'db_table': 'lms_user_document',
            },
        ),
    ]