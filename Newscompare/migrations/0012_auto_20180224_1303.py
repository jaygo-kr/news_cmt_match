# Generated by Django 2.0.1 on 2018-02-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newscompare', '0011_auto_20180211_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_list',
            name='section',
            field=models.CharField(choices=[('정치', '정치'), ('경제', '경제'), ('생활', '생활'), ('사회', '사회'), ('기타', '기타'), ('문화', '문화'), ('IT', 'IT'), ('세계', '세계')], max_length=10),
        ),
    ]
