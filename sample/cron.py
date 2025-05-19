# sample/cron.py
from django_cron import CronJobBase, Schedule

from sample.utils import fetch_current_time


class FetchTimeCronJob(CronJobBase):
    # Run every 1 minute (for testing purposes)
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'sample.fetch_time_cron'  # Unique code identifier

    def do(self):
        # Call the new utility function
        fetch_current_time()
        print("Cron Job Executed!")

#  python manage.py runcrons
