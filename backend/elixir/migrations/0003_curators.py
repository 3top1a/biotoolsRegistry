from django.db import migrations
from django.contrib.auth.models import Group, Permission

def create_curators_group(apps, schema_editor):
    curators_group, created = Group.objects.get_or_create(name='Curators')
class Migration(migrations.Migration):
    dependencies = [
        ('elixir', '0002_auto_20210510_1435'),
    ]

    operations = [
        migrations.RunPython(create_curators_group),
    ]
