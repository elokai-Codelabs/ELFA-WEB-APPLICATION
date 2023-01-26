from django.db import models

# Create your models here.
class School_Information(models.Model):
    school_name = models.CharField(max_length=255, blank=True,null=True)
    vision = models.TextField( blank=True, null=True)
    mission = models.TextField( blank=True, null=True)
    motto = models.CharField(max_length=255, blank=True,null=True)
    school_history = models.TextField( blank=True, null=True)
    school_location = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    first_contact = models.IntegerField( null=True,blank=True)
    second_contact = models.IntegerField( null=True,blank=True)

    def __str__(self):
        return self.school_name

class Department(models.Model):
    DEPARTMENT_CHOICES = (
       ('Montessori','Montessori'),
        ('Lower Primary','Lower Primary'),
        ('Upper Primary','Upper Primary'),
        ('JHS', 'JHS')
    )
    name_of_department = models.CharField(max_length=255, blank=True, null=True, choices=DEPARTMENT_CHOICES)
    HOD = models.CharField(max_length=255, blank=True, null=True)
    featured_image = models.ImageField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True, )
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name_of_department

class Team_Member(models.Model):
    PORTFOLIO = (
         ('Proprietor','Proprietor'),
        ('Head Teacher','Head Teacher'),
        ('Executive Secretary','Executive Secretary'),
         ('Accountant','Accountant'),
    )
    portfolio = models.CharField(max_length=255, blank=True, null=True, choices=PORTFOLIO)
    name = models.CharField(max_length=255, blank=True, null=True)
    featured_image = models.ImageField(max_length=500, blank=True, null=True)
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    instagram_link = models.URLField(max_length=500, blank=True, null=True)
    linkedIn_link = models.ImageField(null=True, blank=True, default='logo.jpg')
    def __str__(self):
            return self.portfolio

class Event(models.Model):
    event_name = models.CharField(max_length=255, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True, )
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
            return self.event_name

class Staff(models.Model):
    STATUS_CHOICES = (
       ('Teaching Staff','Teaching Staff'),
        ('Non-Teaching Staff','Non-Teaching Staff'),
    )
    DEPARTMENT_CHOICES = (
       ('Montessori','Montessori'),
        ('Lower Primary','Lower Primary'),
        ('Upper Primary','Upper Primary'),
        ('JHS', 'JHS'),
        ('Non-Teaching','Non-Teaching')
    )
    name = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True, choices=STATUS_CHOICES)
    department = models.CharField(max_length=255, blank=True, choices=DEPARTMENT_CHOICES)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True,null=True)
    location = models.CharField(max_length=255, blank=True)
    staff_image = models.ImageField(blank=True, null=True)
    date_of_assumption = models.DateField(blank=True, null=True, )
    def __str__(self):
            return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True,null=True)
    featured_image = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
            return self.title



   



    