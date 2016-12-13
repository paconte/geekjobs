from django.db import models
from geekjobs.stackoverflow_parser import DE_STATE_CHOICES
from geekjobs.stackoverflow_parser import de_states
from geekjobs.stackoverflow_parser import JobItem


class Job(models.Model):
    title = models.CharField(max_length=380)
    city = models.CharField(max_length=100, null=True, blank=True, default=None)
    state = models.CharField(choices=DE_STATE_CHOICES, max_length=50)
    remote = models.BooleanField(default=False)
    salary = models.CharField(max_length=100, null=True, blank=True, default=None)
    description = models.CharField(max_length=10000)
    instructions = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    published = models.DateTimeField(auto_now_add=True)


def load_model_jobs():
    result = dict()
    jobs = Job.objects.all()
    for k, v in de_states.items():
        result[k] = []
        for job in jobs:
            if job.state == k:
                new_job = JobItem.from_model_job(job)
                job_list = result[k]
                job_list.append(new_job.to_dict())
                result[k] = job_list
    return result
