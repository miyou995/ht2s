# Generated by Django 4.2.5 on 2024-06-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0011_remove_business_about_ar_remove_business_about_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='buttons_color',
            field=models.CharField(blank=True, default='#011627', max_length=9, null=True, verbose_name='Button color'),
        ),
        migrations.AddField(
            model_name='business',
            name='buttons_text_color',
            field=models.CharField(blank=True, default='#ffffff', max_length=9, null=True, verbose_name='Button text color'),
        ),
        migrations.AddField(
            model_name='business',
            name='footer_color',
            field=models.CharField(blank=True, default='#011627', max_length=9, null=True, verbose_name='Footer color'),
        ),
        migrations.AddField(
            model_name='business',
            name='footer_text_color',
            field=models.CharField(blank=True, default='#ffffff', max_length=9, null=True, verbose_name='Footer text color'),
        ),
        migrations.AddField(
            model_name='business',
            name='header_color',
            field=models.CharField(blank=True, default='#011627', max_length=9, null=True, verbose_name='Navigation bar color'),
        ),
        migrations.AddField(
            model_name='business',
            name='header_text_color',
            field=models.CharField(blank=True, default='#ffffff', max_length=9, null=True, verbose_name='Navigation bar text color'),
        ),
        migrations.AddField(
            model_name='business',
            name='theme_color',
            field=models.CharField(blank=True, default='#011627', max_length=9, null=True, verbose_name='Theme color'),
        ),
        migrations.AddField(
            model_name='business',
            name='theme_text_color',
            field=models.CharField(blank=True, default='#ffffff', max_length=9, null=True, verbose_name='Text color'),
        ),
    ]
