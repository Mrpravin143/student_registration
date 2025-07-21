from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Students(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True ,blank=True)
    student_name=models.CharField(max_length=300)
    student_class=models.CharField(max_length=100)
    student_roll_no=models.IntegerField()
    student_In_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    student_Out_time=models.DateTimeField(auto_now=True, auto_now_add=False)
    student_singnature=models.FileField(upload_to='singnature')
    student_image=models.FileField(upload_to='image')
    student_count_view=models.IntegerField(default=1)


#Second Project Start Here

class StudentID(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id





#main Student Model
class Student_Info(models.Model):
    student_id=models.OneToOneField("StudentID",on_delete=models.CASCADE)
    student_name=models.CharField(max_length=200)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)

    def __str__(self) ->str:
        return self.student_name

    class Meta:
        ordering=['student_name']
        verbose_name = 'student'

class Fake(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    address=models.TextField()



        
