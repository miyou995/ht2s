# Generated by Django 4.2.5 on 2024-06-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_about_image_breadcrumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='brochure',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='brochure'),
        ),
    ]
