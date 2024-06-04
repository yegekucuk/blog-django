# Generated by Django 5.0.6 on 2024-06-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('post_date', models.DateField()),
                ('image', models.ImageField(upload_to='static/img_uploaded/')),
                ('paragraph', models.TextField(max_length=300)),
            ],
        ),
    ]
