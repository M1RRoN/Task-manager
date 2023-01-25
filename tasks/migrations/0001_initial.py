# Generated by Django 4.1.4 on 2023-01-02 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statuses', '0001_initial'),
        ('labels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelForTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labels', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='labels.label')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL)),
                ('labels', models.ManyToManyField(blank=True, through='tasks.LabelForTask', to='labels.label')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='statuses.status')),
            ],
        ),
        migrations.AddField(
            model_name='labelfortask',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]