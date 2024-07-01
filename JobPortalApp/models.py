from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    vacancy = models.IntegerField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.job_name