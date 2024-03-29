# Generated by Django 5.0 on 2023-12-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolycysticOvarySyndromeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folicle_no_R', models.CharField(max_length=50)),
                ('folicle_no_L', models.CharField(max_length=50)),
                ('cycle_r_i', models.CharField(max_length=50)),
                ('cycle_len_days', models.CharField(max_length=50)),
                ('amh_ng_ml', models.CharField(max_length=50)),
                ('fsh_lh', models.CharField(max_length=50)),
                ('prl_ng_ml', models.CharField(max_length=50)),
                ('waist_hip_ratio', models.CharField(max_length=50)),
                ('skin_d_Y', models.BooleanField(default=False)),
                ('skin_d_N', models.BooleanField(default=False)),
                ('hair_g_Y', models.BooleanField(default=False)),
                ('hair_g_N', models.BooleanField(default=False)),
                ('fastFood_Y', models.BooleanField(default=False)),
                ('fastFood_N', models.BooleanField(default=False)),
                ('weight_Y', models.BooleanField(default=False)),
                ('weight_N', models.BooleanField(default=False)),
            ],
        ),
    ]
