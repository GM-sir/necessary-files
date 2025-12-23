from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    full_name = models.CharField()
    department = models.CharField()
    dob = models.DateField()
    gender = models.CharField()
    address = models.CharField()
    image = models.ImageField(upload_to='student_app', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id}-{self.full_name}"