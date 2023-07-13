# Generated by Django 3.2 on 2023-07-12 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Last change date')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_as_markdown', models.BooleanField(default=False, verbose_name='As markdown')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Cost')),
                ('cover', models.CharField(default='no_image.svg', max_length=25, verbose_name='Cover')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'Many news'},
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Last change date')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('num', models.PositiveIntegerField(verbose_name='Lesson number')),
                ('title', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_as_markdown', models.BooleanField(default=False, verbose_name='As markdown')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.courses')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
                'ordering': ('course', 'num'),
            },
        ),
    ]
