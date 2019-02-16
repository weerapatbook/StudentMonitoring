from django.db import models
from enum import Enum
# Create your models here.
class Student(models.Model):
    class SexChoiceEnum(Enum):
        male = '1'
        fremale = '2'

        @classmethod
        def choices(cls):
            return tuple((i.value, i.name) for i in cls)

    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name =  models.CharField(max_length=200,blank=True, null=True)
    code = models.CharField(max_length=200,blank=True, null=True)
    sex  = models.CharField(max_length=1, choices=SexChoiceEnum.choices(),blank=True, null=True)

    def __str__(self):
        return r"%s %s" %(self.first_name, self.last_name)
class Room (models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return r"%s" %(self.name)

class Teacher(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    telephone = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return r"%s" %(self.name)

class Absent(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return r"%s" %(self.name)

class Subject(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return r"%s" %(self.name)

class StudentInRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True, null=True )
    student = models.ForeignKey(Student, on_delete=models.CASCADE,blank=True, null=True )
    current_year = models.IntegerField(blank=True, null=True,default=2561)
    def __str__(self):
        return r"%s (%s)" %(self.room, self.student)


class TeacherInRoom(models.Model):
    teach_date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=200,blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True, null=True )


    def __str__(self):
        return r"%s %s (%s)" % (self.teach_date, self.subject, self.teacher)

class StudentAbsent(models.Model):
    teacherinroom = models.ForeignKey(TeacherInRoom, on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    absent = models.ForeignKey(Absent, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return r"%s %s" % (self.student, self.absent)
