from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_admin', '0014_add_parent_event_and_child_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='progress_percent',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='completion_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Chưa thực hiện'), (2, 'Đang thực hiện'), (3, 'Hoàn thành'), (4, 'Chưa hoàn thành')], default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='incomplete_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='actual_amount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='event',
            name='over_budget_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='report_updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
