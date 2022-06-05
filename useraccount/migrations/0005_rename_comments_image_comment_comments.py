

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0004_remove_profile_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='comments',
            new_name='comment',
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('desc', models.TextField(max_length=200)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.image')),
            ],
        ),
    ]
