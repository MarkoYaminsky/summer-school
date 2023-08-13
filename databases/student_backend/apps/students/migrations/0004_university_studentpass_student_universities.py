# Generated by Django 4.2.4 on 2023-08-13 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
        ('students', '0003_alter_student_country_alter_student_sex_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.country')),
            ],
        ),
        migrations.CreateModel(
            name='StudentPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.university')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='universities',
            field=models.ManyToManyField(to='students.university'),
        ),
    ]
