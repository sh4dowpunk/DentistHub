# Generated by Django 4.2.3 on 2024-03-23 16:44

import DentistBook.dentist.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dentistsoffice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), DentistBook.dentist.validators.validate_name])),
                ('about', models.TextField()),
                ('dentist_picture', models.ImageField(blank=True, null=True, upload_to='dentist-profile-pictures', validators=[DentistBook.dentist.validators.validate_dentist_picture_file_size])),
                ('dentistsoffice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dentistsoffice.dentistsofficeprofile')),
            ],
        ),
    ]
