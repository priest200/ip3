

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0010_remove_followers_following_followers_following_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='following',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='followers',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
