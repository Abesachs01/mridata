# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 23:00
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mridatabase.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('anatomy', models.CharField(default='N/A', max_length=100)),
                ('sequence_name', models.CharField(default='N/A', max_length=100)),
                ('trajectory', models.CharField(default='N/A', max_length=100)),
                ('fullysampled', models.BooleanField()),
                ('scanner_vendor', models.CharField(default='N/A', max_length=100)),
                ('scanner_model', models.CharField(blank=True, default='N/A', max_length=100)),
                ('scanner_field', models.FloatField(blank=True, default=-1, verbose_name='Field Strength [T]')),
                ('matrix_size_x', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('matrix_size_y', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('matrix_size_z', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('number_of_channels', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('number_of_slices', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('number_of_repetitions', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('number_of_contrasts', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('resolution_x', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Resolution x [mm]')),
                ('resolution_y', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Resolution y [mm]')),
                ('resolution_z', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Resolution z [mm]')),
                ('flip_angle', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Flip Angle [degree]')),
                ('te', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Echo Time [ms]')),
                ('tr', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Repetition Time [ms]')),
                ('ti', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Inversion Time [ms]')),
                ('ismrmrd_file', models.FileField(upload_to=mridatabase.models.save_ismrmrd_file, validators=[mridatabase.models.validate_ismrmrd_file], verbose_name='ISMRMRD File')),
                ('thumbnail_file', models.ImageField(upload_to='')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TempData',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('anatomy', models.CharField(max_length=100)),
                ('fullysampled', models.BooleanField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('failed', models.BooleanField(default=False)),
                ('error_message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CflData',
            fields=[
                ('data_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridatabase.Data')),
                ('cfl_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_cfl_file, validators=[mridatabase.models.validate_cfl_file])),
                ('hdr_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_hdr_file, validators=[mridatabase.models.validate_hdr_file])),
            ],
            bases=('mridatabase.data',),
        ),
        migrations.CreateModel(
            name='GeData',
            fields=[
                ('tempdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridatabase.TempData')),
                ('ge_pfile', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_ge_pfile)),
            ],
            bases=('mridatabase.tempdata',),
        ),
        migrations.CreateModel(
            name='IsmrmrdData',
            fields=[
                ('tempdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridatabase.TempData')),
                ('ismrmrd_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_ismrmrd_file, validators=[mridatabase.models.validate_ismrmrd_file])),
            ],
            bases=('mridatabase.tempdata',),
        ),
        migrations.CreateModel(
            name='PhilipsData',
            fields=[
                ('tempdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridatabase.TempData')),
                ('philips_raw_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_philips_raw_file, validators=[mridatabase.models.validate_philips_raw_file])),
                ('philips_sin_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_philips_sin_file, validators=[mridatabase.models.validate_philips_sin_file])),
                ('philips_lab_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_philips_lab_file, validators=[mridatabase.models.validate_philips_lab_file])),
            ],
            bases=('mridatabase.tempdata',),
        ),
        migrations.CreateModel(
            name='RaData',
            fields=[
                ('data_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridatabase.Data')),
                ('ra_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_ra_file, validators=[mridatabase.models.validate_ra_file])),
            ],
            bases=('mridatabase.data',),
        ),
        migrations.CreateModel(
            name='SiemensData',
            fields=[
                ('tempdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridatabase.TempData')),
                ('siemens_dat_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridatabase.models.save_siemens_dat_file, validators=[mridatabase.models.validate_siemens_dat_file])),
            ],
            bases=('mridatabase.tempdata',),
        ),
        migrations.AddField(
            model_name='tempdata',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='data',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
