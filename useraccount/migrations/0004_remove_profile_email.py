

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0003_rename_profile_avatar_profile_profile_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
