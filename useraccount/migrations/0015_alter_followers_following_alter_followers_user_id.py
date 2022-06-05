

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useraccount', '0014_remove_followers_following_followers_following_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followers',
            name='user_id',
            field=models.ManyToManyField(to='useraccount.profile'),
        ),
    ]
