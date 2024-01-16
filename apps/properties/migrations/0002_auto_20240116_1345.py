# Generated by Django 3.2.7 on 2024-01-16 08:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.CreateModel(
            name='PropertyViews',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(max_length=250, verbose_name='IP Address')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_views', to='properties.property')),
            ],
            options={
                'verbose_name': 'Total Views on Property',
                'verbose_name_plural': 'Total Property Views',
            },
        ),
    ]