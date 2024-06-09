from django.db import models
from courses.models.course import Course

class Group(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    course = models.ForeingKey(Course, related_name='groups', on_delete=models.CASCADE)
    students = models.ManyToManyField('users.Student', related_name='groups')
    teacher = models.ForeingKey('users.Teacher', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
