# Generated by Django 2.2.6 on 2019-11-24 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('question_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Drop_option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField()),
                ('option_number', models.IntegerField()),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Drop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('question_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('question_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Multi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('question_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Multi_option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField()),
                ('option_number', models.IntegerField()),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Multi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Para',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('question_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('question_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Single_option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField()),
                ('option_number', models.IntegerField()),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Single')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('question_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Toggle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('question_type', models.IntegerField()),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Toggle_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Toggle')),
            ],
        ),
        migrations.CreateModel(
            name='Slider_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Slider')),
            ],
        ),
        migrations.AddField(
            model_name='slider',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey'),
        ),
        migrations.CreateModel(
            name='Single_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Single_option')),
                ('parent_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Single')),
            ],
        ),
        migrations.AddField(
            model_name='single',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey'),
        ),
        migrations.CreateModel(
            name='Para_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Para')),
            ],
        ),
        migrations.AddField(
            model_name='para',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey'),
        ),
        migrations.CreateModel(
            name='Multi_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Multi_option')),
                ('parent_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Multi')),
            ],
        ),
        migrations.AddField(
            model_name='multi',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey'),
        ),
        migrations.CreateModel(
            name='Line_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=250)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Line')),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey'),
        ),
        migrations.CreateModel(
            name='File_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.FileField(upload_to='')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.File')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey'),
        ),
        migrations.CreateModel(
            name='Drop_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Drop_option')),
                ('parent_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Drop')),
            ],
        ),
        migrations.AddField(
            model_name='drop',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey'),
        ),
    ]
