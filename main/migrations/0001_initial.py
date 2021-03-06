# Generated by Django 3.1 on 2020-08-26 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hash_tag',
            fields=[
                ('ht_id', models.AutoField(primary_key=True, serialize=False)),
                ('ht_name', models.CharField(max_length=45, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ip',
            fields=[
                ('ip_id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=45, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('lesson_desc', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('mem_id', models.AutoField(primary_key=True, serialize=False)),
                ('mem_name', models.CharField(max_length=45)),
                ('mem_email', models.CharField(max_length=45)),
                ('mem_profile', models.ImageField(null=True, upload_to='')),
                ('mem_number', models.CharField(max_length=45, null=True)),
                ('joined_at', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mem_rank', models.CharField(max_length=45)),
                ('github_url', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=45)),
                ('service_desc', models.CharField(max_length=45)),
                ('service_img', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('made_at', models.DateTimeField()),
                ('skill_stack', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sns',
            fields=[
                ('sns_id', models.AutoField(primary_key=True, serialize=False)),
                ('sns_name', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sns_img', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='time_line',
            fields=[
                ('tl_id', models.AutoField(primary_key=True, serialize=False)),
                ('tl_img', models.ImageField(null=True, upload_to='')),
                ('tl_name', models.CharField(max_length=45)),
                ('tl_desc', models.TextField()),
                ('tl_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='wiki',
            fields=[
                ('wiki_id', models.AutoField(primary_key=True, serialize=False)),
                ('wiki_img', models.ImageField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('wiki_desc', models.TextField(null=True)),
                ('wiki_title', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='rel_wiki_ip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ip')),
                ('wiki', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.wiki')),
            ],
        ),
        migrations.CreateModel(
            name='rel_wiki_hashtag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('hash_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.hash_tag')),
                ('wiki', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.wiki')),
            ],
        ),
        migrations.CreateModel(
            name='rel_member_service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rank', models.CharField(max_length=45, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.member')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service')),
            ],
        ),
        migrations.CreateModel(
            name='rel_mem_timeline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('start_act', models.DateTimeField(null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.member')),
                ('time_line', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.time_line')),
            ],
        ),
        migrations.CreateModel(
            name='rel_mem_sns',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sns_url', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.member')),
                ('sns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sns')),
            ],
        ),
        migrations.CreateModel(
            name='opinion',
            fields=[
                ('op_id', models.AutoField(primary_key=True, serialize=False)),
                ('op_body', models.CharField(max_length=45, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ip')),
            ],
        ),
        migrations.CreateModel(
            name='discussion',
            fields=[
                ('dis_id', models.AutoField(primary_key=True, serialize=False)),
                ('dis_title', models.CharField(max_length=45, null=True)),
                ('dis_desc', models.CharField(max_length=500, null=True)),
                ('dis_solved', models.CharField(max_length=500, null=True)),
                ('ip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ip')),
                ('wiki', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.wiki')),
            ],
        ),
    ]
