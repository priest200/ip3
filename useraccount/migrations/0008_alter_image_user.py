

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0007_alter_image_user_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='useraccount.profile'),
        ),
    ]
