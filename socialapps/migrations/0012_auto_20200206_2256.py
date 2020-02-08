# Generated by Django 3.0 on 2020-02-07 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapps', '0011_auto_20200203_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_url', models.URLField()),
                ('status_type', models.CharField(default='SOME STRING', max_length=100)),
                ('status_source', models.CharField(default='SOME STRING', max_length=100)),
                ('caption', models.CharField(default='SOME STRING', max_length=100)),
                ('post_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='image_file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
