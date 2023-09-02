from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares/'),
        ),
    ]
