


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='profile_avatar',
        ),
    ]
