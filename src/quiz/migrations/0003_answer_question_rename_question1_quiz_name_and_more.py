# Generated by Django 4.2.4 on 2023-09-26 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0002_quiz_iden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('creation', models.DateField(auto_now_add=True)),
                ('value', models.IntegerField(default=1)),
            ],
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='Question1',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Question2',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Question3',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Question4',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='iden',
        ),
        migrations.AlterModelTable(
            name='quiz',
            table=None,
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizattempt')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.answer')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question'),
        ),
    ]
