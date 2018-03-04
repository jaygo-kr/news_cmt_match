# Generated by Django 2.0.1 on 2018-01-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newscompare', '0002_auto_20180129_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_buffer',
            name='cmt_date',
        ),
        migrations.AlterField(
            model_name='news_analyze',
            name='portal',
            field=models.CharField(choices=[('Naver', 'Naver'), ('Daum', 'Daum')], max_length=10),
        ),
        migrations.AlterField(
            model_name='news_list',
            name='section',
            field=models.CharField(choices=[('생활', '생활'), ('세계', '세계'), ('문화', '문화'), ('IT', 'IT'), ('기타', '기타'), ('경제', '경제'), ('정치', '정치'), ('사회', '사회')], max_length=10),
        ),
    ]