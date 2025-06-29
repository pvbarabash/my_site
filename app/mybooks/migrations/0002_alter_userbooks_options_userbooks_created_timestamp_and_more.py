# Generated by Django 4.2.7 on 2024-12-23 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mybooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbooks',
            options={'verbose_name': 'Книги пользователя', 'verbose_name_plural': 'Книги пользователя'},
        ),
        migrations.AddField(
            model_name='userbooks',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userbooks',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.books', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='userbooks',
            name='status',
            field=models.CharField(choices=[('прочитано', 'Прочитано'), ('добавлено резюме', 'Добавлено резюме')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userbooks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
