# Generated by Django 4.2.1 on 2023-06-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_remove_applications_email_remove_applications_prenom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serveurs',
            old_name='type_serveur',
            new_name='types_serveurs',
        ),
        migrations.AlterField(
            model_name='applications',
            name='logo',
            field=models.ImageField(default='static/administration/defaut.png', upload_to='static/administration/logo/'),
        ),
    ]
