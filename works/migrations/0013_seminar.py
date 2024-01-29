# Generated by Django 4.2.9 on 2024-01-19 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import works.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('works', '0012_postdocreport_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit', models.IntegerField(blank=True, default=1)),
                ('write_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.CharField(blank=True, null=True)),
                ('file1', models.FileField(blank=True, null=True, upload_to='seminar/')),
                ('file2', models.FileField(blank=True, null=True, upload_to='seminar/')),
                ('title', models.CharField(max_length=500, null=True)),
                ('ref', models.CharField(blank=True, max_length=100)),
                ('tcp_ip', models.CharField(blank=True, max_length=100)),
                ('writer', models.ForeignKey(default=works.models.get_default_user, on_delete=django.db.models.deletion.DO_NOTHING, related_name='seminar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]