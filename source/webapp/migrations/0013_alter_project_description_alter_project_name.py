# Generated by Django 4.1.7 on 2023-03-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0012_project_alter_issue_deleted_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(
                blank=True, max_length=2000, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Название"),
        ),
    ]
