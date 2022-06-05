

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useraccount', '0013_alter_followers_following_remove_followers_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followers',
            name='following',
        ),
        migrations.AddField(
            model_name='followers',
            name='following',
            field=models.ManyToManyField(to='useraccount.profile'),
        ),
        migrations.RemoveField(
            model_name='followers',
            name='user_id',
        ),
        migrations.AddField(
            model_name='followers',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
