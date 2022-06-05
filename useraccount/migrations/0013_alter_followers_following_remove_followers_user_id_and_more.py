

import django.contrib.auth.models
from django.db import migrations, models
import useraccount.models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0012_alter_followers_following_remove_followers_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='following',
            field=models.IntegerField(default=useraccount.models.Profile),
        ),
        migrations.RemoveField(
            model_name='followers',
            name='user_id',
        ),
        migrations.AddField(
            model_name='followers',
            name='user_id',
            field=models.IntegerField(default=django.contrib.auth.models.User),
        ),
    ]
