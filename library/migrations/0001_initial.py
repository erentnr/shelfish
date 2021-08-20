# Generated by Django 3.2 on 2021-04-27 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('listing_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date listed')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('number_of_pages', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='library.Author')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('status', models.IntegerField(choices=[(-1, 'Rejected'), (0, 'Waiting'), (1, 'Accepted')], default=0)),
                ('proposed_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposed_book', to='library.book')),
                ('requested_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_book', to='library.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='library.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='library.Tag'),
        ),
    ]