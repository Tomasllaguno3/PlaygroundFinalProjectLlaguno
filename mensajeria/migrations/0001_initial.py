from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('user_chat_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user_1', to=settings.AUTH_USER_MODEL)),
                ('user_chat_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=255)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('id_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mensajeria.chat')),
            ],
        ),
    ]