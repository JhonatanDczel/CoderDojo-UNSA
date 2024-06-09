from django.db import models
from courses.models.course import Course

class Assigment(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    due_date = models.DateTimeField()
    course = models.ForeingKey(Course, related_name='assigments', on_delete=models.CASCADE)
    teacher = models.ForeingKey('users.Teacher', on_delete=models.CASCADE)
    done_by = models.ForeingKey('users.Student', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
