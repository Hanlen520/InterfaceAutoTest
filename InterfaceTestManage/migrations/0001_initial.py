# Generated by Django 2.0.7 on 2018-08-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('path_name', models.CharField(max_length=30, null=True, verbose_name='环境名称')),
                ('host', models.CharField(max_length=50, null=True, verbose_name='主机名称')),
                ('port', models.CharField(max_length=8, verbose_name='端口号')),
                ('envir_descript', models.TextField(verbose_name='环境简介')),
                ('status', models.IntegerField(default=1, verbose_name='启用状态码')),
                ('username', models.CharField(max_length=10, verbose_name='操作人')),
            ],
            options={
                'verbose_name': '环境配置表',
                'db_table': 'enviroment',
            },
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('projectName', models.CharField(max_length=10, verbose_name='项目名称')),
                ('projectdesc', models.TextField(verbose_name='项目说明')),
                ('username', models.CharField(max_length=10, verbose_name='操作人')),
            ],
            options={
                'verbose_name': '项目表',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=8, unique=True, verbose_name='用户名')),
                ('phone', models.CharField(max_length=11, verbose_name='联系手机号')),
                ('email', models.EmailField(max_length=11, verbose_name='邮箱')),
                ('role', models.IntegerField(null=True, verbose_name='用户角色')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户信息表',
                'db_table': 'userInfo',
            },
        ),
    ]
