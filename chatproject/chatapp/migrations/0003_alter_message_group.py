# Generated by Django 4.1.3 on 2022-11-23 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='group',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='chatapp.groupname'),
        ),
    ]
