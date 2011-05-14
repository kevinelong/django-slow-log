from django.db import models


class Record(models.Model):

    pid = models.IntegerField()
    status_code = models.IntegerField()
    time_delta = models.FloatField()
    request_method = models.CharField(max_length=6)
    path = models.CharField(max_length=255)
    django_view = models.CharField(max_length=255)
    memory_delta = models.IntegerField()
    load_delta = models.FloatField()
    queries = models.IntegerField()
    response_started = models.DateTimeField()
