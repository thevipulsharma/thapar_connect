# Generated by Django 2.0.3 on 2018-06-21 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20180618_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='attendance.UserInfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='attendance.UserInfo'),
            preserve_default=False,
        ),
    ]
