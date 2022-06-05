

from django.conf import settings
from django.db import migrations, models
import useraccount.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useraccount', '0011_alter_followers_following_alter_followers_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='following',
            field=models.IntegerField(verbose_name=useraccount.models.Profile),
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
