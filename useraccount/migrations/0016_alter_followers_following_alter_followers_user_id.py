

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useraccount', '0015_alter_followers_following_alter_followers_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='following',
            field=models.ManyToManyField(to='useraccount.profile'),
        ),
        migrations.AlterField(
            model_name='followers',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
