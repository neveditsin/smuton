# Generated by Django 2.1 on 2018-09-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180831_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hack_id', models.IntegerField(verbose_name='Hack')),
                ('round_no', models.IntegerField(verbose_name='Round')),
                ('round_id', models.IntegerField(verbose_name='RID')),
                ('judge_id', models.IntegerField(verbose_name='Judge')),
                ('team_name', models.CharField(max_length=128, verbose_name='Team Name')),
                ('team_id', models.IntegerField(verbose_name='Team Id')),
                ('critera', models.CharField(max_length=256, verbose_name='Criteria Name')),
                ('mark_weight', models.IntegerField(verbose_name='Weight')),
            ],
            options={
                'db_table': 'core_resonses_vw',
                'managed': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='judgeresponse',
            unique_together={('round', 'judge', 'team', 'criterion')},
        ),
    ]
