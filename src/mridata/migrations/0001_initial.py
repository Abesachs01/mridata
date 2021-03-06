# Generated by Django 2.0.3 on 2018-03-27 23:52

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mridata.models
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
                ('anatomy', models.CharField(default='Unknown', max_length=100)),
                ('fullysampled', models.NullBooleanField()),
                ('protocol_name', models.CharField(blank=True, default='', max_length=100)),
                ('series_description', models.TextField(blank=True, default='')),
                ('system_vendor', models.CharField(blank=True, default='', max_length=100)),
                ('system_model', models.CharField(blank=True, default='', max_length=100)),
                ('system_field_strength', models.FloatField(default=-1, verbose_name='Field Strength [T]')),
                ('relative_receiver_noise_bandwidth', models.FloatField(default=-1)),
                ('number_of_channels', models.IntegerField(default=-1)),
                ('coil_name', models.CharField(blank=True, default='', max_length=100)),
                ('institution_name', models.CharField(blank=True, default='', max_length=100)),
                ('station_name', models.CharField(blank=True, default='', max_length=100)),
                ('h1_resonance_frequency', models.FloatField(default=-1, verbose_name='H1 Resonance Frequency [Hz]')),
                ('matrix_size_x', models.IntegerField(default=-1)),
                ('matrix_size_y', models.IntegerField(default=-1)),
                ('matrix_size_z', models.IntegerField(default=-1)),
                ('field_of_view_x', models.FloatField(default=-1, verbose_name='Field of View x [mm]')),
                ('field_of_view_y', models.FloatField(default=-1, verbose_name='Field of View y [mm]')),
                ('field_of_view_z', models.FloatField(default=-1, verbose_name='field of View z [mm]')),
                ('number_of_averages', models.IntegerField(default=-1)),
                ('number_of_slices', models.IntegerField(default=-1)),
                ('number_of_repetitions', models.IntegerField(default=-1)),
                ('number_of_contrasts', models.IntegerField(default=-1)),
                ('number_of_phases', models.IntegerField(default=-1)),
                ('number_of_sets', models.IntegerField(default=-1)),
                ('number_of_segments', models.IntegerField(default=-1)),
                ('trajectory', models.CharField(blank=True, default='', max_length=100)),
                ('parallel_imaging_factor_y', models.FloatField(default=-1)),
                ('parallel_imaging_factor_z', models.FloatField(default=-1)),
                ('echo_train_length', models.IntegerField(default=-1)),
                ('tr', models.FloatField(default=-1, verbose_name='Repetition Time [ms]')),
                ('te', models.FloatField(default=-1, verbose_name='Echo Time [ms]')),
                ('ti', models.FloatField(default=-1, verbose_name='Inversion Time [ms]')),
                ('flip_angle', models.FloatField(default=-1, verbose_name='Flip Angle [degree]')),
                ('sequence_type', models.CharField(blank=True, default='', max_length=100)),
                ('echo_spacing', models.FloatField(default=-1, verbose_name='Echo Spacing [ms]')),
                ('references', models.TextField(blank=True, default='')),
                ('comments', models.TextField(blank=True, default='')),
                ('thumbnail_file', models.ImageField(upload_to='')),
                ('thumbnail_horizontal_flip', models.BooleanField(default=False)),
                ('thumbnail_vertical_flip', models.BooleanField(default=False)),
                ('thumbnail_rotate_90_degree', models.BooleanField(default=False)),
                ('ismrmrd_file', models.FileField(upload_to=mridata.models.save_ismrmrd_file, verbose_name='ISMRMRD File')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TempData',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('anatomy', models.CharField(default='Unknown', max_length=100)),
                ('fullysampled', models.NullBooleanField()),
                ('references', models.TextField(blank=True, default='')),
                ('comments', models.TextField(blank=True, default='')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumbnail_horizontal_flip', models.BooleanField(default=False)),
                ('thumbnail_vertical_flip', models.BooleanField(default=False)),
                ('thumbnail_rotate_90_degree', models.BooleanField(default=False)),
                ('failed', models.NullBooleanField(default=False)),
                ('error_message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refresh', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GeData',
            fields=[
                ('tempdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridata.TempData')),
                ('ge_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridata.models.save_ge_file)),
            ],
            bases=('mridata.tempdata',),
        ),
        migrations.CreateModel(
            name='IsmrmrdData',
            fields=[
                ('tempdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridata.TempData')),
                ('ismrmrd_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridata.models.save_ismrmrd_file)),
            ],
            bases=('mridata.tempdata',),
        ),
        migrations.CreateModel(
            name='PhilipsData',
            fields=[
                ('tempdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridata.TempData')),
                ('philips_raw_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridata.models.save_philips_raw_file)),
                ('philips_sin_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridata.models.save_philips_sin_file)),
                ('philips_lab_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridata.models.save_philips_lab_file)),
            ],
            bases=('mridata.tempdata',),
        ),
        migrations.CreateModel(
            name='SiemensData',
            fields=[
                ('tempdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mridata.TempData')),
                ('siemens_dat_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/temp/', location='/src/temp'), upload_to=mridata.models.save_siemens_dat_file)),
            ],
            bases=('mridata.tempdata',),
        ),
        migrations.AddField(
            model_name='tempdata',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mridata.Uploader'),
        ),
        migrations.AddField(
            model_name='data',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mridata.Uploader'),
        ),
    ]
