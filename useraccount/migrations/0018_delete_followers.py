
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0017_alter_followers_following_alter_followers_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Followers',
        ),
    ]
