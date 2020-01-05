# Generated by Django 2.0.6 on 2020-01-03 20:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashBoard', '0006_auto_20200103_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classworkmodel',
            old_name='repo',
            new_name='repoWithStudentsWork',
        ),
        migrations.RenameField(
            model_name='classworkmodel',
            old_name='rubricForProject',
            new_name='rubric',
        ),
        migrations.RenameField(
            model_name='classworkmodel',
            old_name='scorecard',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='lessonmodel',
            old_name='isProject',
            new_name='lessonIsProject',
        ),
        migrations.RenameField(
            model_name='lessonmodel',
            old_name='possiblePoint',
            new_name='possiblePoints',
        ),
        migrations.RenameField(
            model_name='scorecardmodel',
            old_name='student',
            new_name='studentUserModel',
        ),
        migrations.RenameField(
            model_name='scorecardmodel',
            old_name='studentName',
            new_name='studentsName',
        ),
        migrations.AlterField(
            model_name='attendacemodels',
            name='dateTimeRecord',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 3, 20, 42, 47, 491767, tzinfo=utc)),
        ),
    ]