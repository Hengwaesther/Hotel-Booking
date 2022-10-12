# Generated by Django 4.1.2 on 2022-10-12 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room_Blog_Absact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('publised', 'PUBLISHED'), ('draft', 'DRAFT')], max_length=50)),
                ('services', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title', 'published', 'status', 'image'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_blog_absact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_hotel.room_blog_absact')),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('bed', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('title', 'price', 'size', 'capacity', 'bed', 'published', 'status', 'image'),
            },
            bases=('app_hotel.room_blog_absact',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('room_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hotel.room_blog_absact')),
            ],
            options={
                'ordering': ('-created', 'name', 'email'),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('guest', models.CharField(choices=[('one_dult', '1 Dult'), ('two_dult', '2 Dult'), ('three_dult', '3 Dult'), ('four_dult', '4 Dult'), ('five_dult', '5 Dult'), ('two_dult_with_chirdeen', '2 Dult 2 chirdeen'), ('other', 'Other')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hotel.room')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('room_blog_absact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_hotel.room_blog_absact')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hotel.category')),
            ],
            bases=('app_hotel.room_blog_absact',),
        ),
    ]
