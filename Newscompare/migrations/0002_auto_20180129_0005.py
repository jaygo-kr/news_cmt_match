# Generated by Django 2.0.1 on 2018-01-29 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newscompare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_analyze',
            name='portal',
            field=models.CharField(choices=[('Daum', 'Daum'), ('Naver', 'Naver')], max_length=10),
        ),
        migrations.AlterField(
            model_name='news_list',
            name='section',
            field=models.CharField(choices=[('문화', '문화'), ('세계', '세계'), ('IT', 'IT'), ('기타', '기타'), ('생활', '생활'), ('사회', '사회'), ('정치', '정치'), ('경제', '경제')], max_length=10),
        ),
    ]
