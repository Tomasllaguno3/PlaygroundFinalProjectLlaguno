from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='id_chat',
            new_name='chat',
        ),
    ]