# Generated by Django 3.0.5 on 2021-08-31 05:27

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('isDoctor', models.BooleanField(verbose_name='Is User a Doctor?')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('username', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=500, verbose_name='Password')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('activated', models.BooleanField(default=False, verbose_name='Is User activated?')),
                ('age', models.PositiveIntegerField(default=None, validators=[django.core.validators.MaxValueValidator(200)], verbose_name='Age')),
                ('disease', models.CharField(default=None, max_length=200, verbose_name='Diseases')),
                ('allergies', models.CharField(default=None, max_length=200, verbose_name='Allergies')),
                ('specialization', models.CharField(default=None, max_length=200, verbose_name='Specialization of Doctor')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('patients', models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL, verbose_name='Patients Doctor is Treating')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
