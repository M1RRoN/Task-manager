# Generated by Django 4.1.4 on 2023-01-26 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alter_label_name'),
        ('statuses', '0002_alter_status_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_rename_label_relations_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.Relations', to='labels.label', verbose_name='Метки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='statuses.status', verbose_name='Статус'),
        ),
    ]
