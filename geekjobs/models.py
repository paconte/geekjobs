from django.db import models
from geekjobs.stackoverflow_parser import EU_COUNTRIES_CHOICES
from geekjobs.stackoverflow_parser import de_states, eu_countries
from geekjobs.stackoverflow_parser import JobItem


class Job(models.Model):
    title = models.CharField(max_length=380)
    city = models.CharField(max_length=100, null=True, blank=True, default=None)
    state = models.CharField(choices=EU_COUNTRIES_CHOICES, max_length=50)
    remote = models.BooleanField(default=False)
    salary = models.CharField(max_length=100, null=True, blank=True, default=None)
    description = models.CharField(max_length=10000)
    instructions = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[%s, %s, %s, %s, %s, %s, %s, %s, %s. %s, %s]' % (
            self.title, self.city, self.state, self.remote, self.salary, 'DESCRIPTION', self.instructions, self.name,
            self.url, self.email, self.published)


def load_model_jobs():
    result = dict()
    jobs = Job.objects.all()
    result['EU'] = []
    result['REMOTE'] = []
    for k, v in eu_countries.items():
        result[k] = []
        for job in jobs:
            # for europe (all jobs)
            if k == 'EU':
                new_job = JobItem.from_model_job(job)
                job_list = result['EU']
                job_list.append(new_job.to_dict())
                result['EU'] = job_list
            # per country
            if job.state == k:
                new_job = JobItem.from_model_job(job)
                job_list = result[k]
                job_list.append(new_job.to_dict())
                result[k] = job_list
            # remote
            if job.remote:
                new_job = JobItem.from_model_job(job)
                job_list = result['REMOTE']
                job_list.append(new_job.to_dict())
                result['REMOTE'] = job_list
    return result
