from celery import shared_task
from myblog.celery import app
from rest_api.models import Movies  # Import your model
from faker import Faker
from django_celery_beat.models import PeriodicTask, CrontabSchedule

fake = Faker()


@shared_task
def create_object_task():
    obj = Movies.objects.create(name=fake.name(), director=fake.job(), producer=fake.company())
    return 'Created Movie Object' # Optionally, return the ID of the created object


#TODO: Customize the task results being stored in TaskResults Table.

@shared_task(bind=True) #can self as an argument in function and can access task_name in function and do some math
def send_login_mail(self, user_email,sender, subject, message):


    from django.core.mail import send_mail
    send_mail(subject,message, sender ,[user_email],fail_silently=False)

    return 'Task Executed'


# Creating a peroidic tasks from django and directly creating in tables.
# Where celery beat looks and finds the task at specified time and sends the task to celery worker
def create_cron_job_celery_beat():
    schedule, created = CrontabSchedule.objects.get_or_create(
            hour=15, minute=26, day_of_month=16, month_of_year=5
    )
    import json,datetime
    email_args = {
        "user_email" : "lokrajkumar007@gmail.com",
        "sender" : "lokrajkumarv1@gmail.com",
        "subject" : "Welcome!",
        "message" : "Thank you for logging in. Welcome to our website!"
    }
    PeriodicTask.objects.create(
        crontab=schedule, name=f'send_mail_at_3:26pm | {datetime.datetime.now().second}',
          task='accounts.tasks.send_login_mail', kwargs=json.dumps(email_args), enabled=True
    )
    return 'Peroidic Task created'