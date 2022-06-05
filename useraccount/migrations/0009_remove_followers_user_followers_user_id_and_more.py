

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useraccount', '0008_alter_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followers',
            name='user',
        ),
        migrations.AddField(
            model_name='followers',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.profile'),
        ),
        migrations.AlterField(
            model_name='followers',
            name='following',
            field=models.ManyToManyField(to='useraccount.profile'),
        ),
    ]
