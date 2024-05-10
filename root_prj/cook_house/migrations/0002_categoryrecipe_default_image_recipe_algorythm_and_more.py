# Generated by Django 5.0.6 on 2024-05-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook_house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryrecipe',
            name='default_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='algorythm',
            field=models.TextField(default='not set', max_length=1000),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.TextField(default='anonimus', max_length='100'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preview',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='review',
            field=models.TextField(db_comment='отсекаем на 100 знаков', default='not set'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_estimate',
            field=models.IntegerField(default=999),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default='not set', max_length=100),
        ),
        migrations.AlterField(
            model_name='categoryrecipe',
            name='title',
            field=models.CharField(choices=[('snacks', 'Салаты и Закуски'), ('first_dishes', 'Супы'), ('main_dishes', 'Второе'), ('baking', 'Хлеб и Выпечка'), ('desserts', 'Десерты'), ('drinks', 'Безалкогольные напитки'), ('alco', 'Пойло'), ('later', 'уточняем')], default='later', max_length=20),
        ),
    ]
