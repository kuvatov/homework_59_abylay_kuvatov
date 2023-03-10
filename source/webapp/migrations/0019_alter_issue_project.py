# Generated by Django 4.1.7 on 2023-03-10 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0018_alter_issue_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issues",
                to="webapp.project",
                verbose_name="Проект",
            ),
        ),
    ]
