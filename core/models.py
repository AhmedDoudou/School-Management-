from turtle import title
from django.db import models
from phone_field import PhoneField
from birthday import BirthdayField, BirthdayManager


class Student (models.Model):
    GENDER_S = (('Boy', 'Boy'),('Girl', 'Girl'))
    gender      = models.CharField( max_length=10,choices=GENDER_S,default='Boy')
    first_name  = models.CharField( max_length=30)
    last_name   = models.CharField( max_length=30)
    tiny = "Tiny Makers"
    mini = "Mini Makers"
    champions ="Makers Champions"
    grades = [
        (tiny,"Tiny Makers" ),
        (mini, "Mini Makers"),
        (champions, "Makers Champions"),
    ]
    grade = models.CharField(max_length=20, choices=grades, default=mini)
    email       = models.EmailField(max_length=254)
    phone       = PhoneField(blank=True, help_text='Contact phone number')
    birthday    = BirthdayField()
    address     = models.CharField( max_length=50)
    picture     = models.ImageField(null=True, blank=True,upload_to='profiles/')
    date_added  = models.DateTimeField(auto_now_add=True)
    is_active   = models.BooleanField(default=False)

    objects = BirthdayManager()
    def __str__(self):
        return self.first_name

class Program(models.Model):
    stemQuest = "StemQuest Program"
    on_choice = "On Choice Camps"
    holidays_camps = "Holidays Camps"
    categories = [(stemQuest, 'StemQuest Program'), (on_choice, 'On Choice Camps'), (holidays_camps, 'Holidays Camps')]
    label = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200, blank=True)
    category =models.CharField(max_length=25, choices=categories, default=stemQuest,)

    def __str__(self):
        return self.label

class Abonnement(models.Model):
    label = models.CharField(max_length=50)
    price = models.FloatField()
    remise = models.FloatField()  
    
    def __str__(self):
        return self.label

        
class Payment(models.Model):
    cash = "CASH"
    cheque = "CHEQUE"
    card = "CREDIT CARD"
    payment_choices = [(cash, "CASH"), (cheque, "CHEQUE"), (card, "Bank Credit Card")]
    student         = models.ForeignKey("Student", on_delete=models.CASCADE)
    abonnement      = models.ForeignKey("Abonnement",on_delete=models.DO_NOTHING, null=True)
    payment_method  = models.CharField(max_length=50, choices=payment_choices, default=cash, )
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)   
    created_by      = models.CharField(max_length=50)      
    
    def __str__(self):
        return self.payment_method+' | '+str(self.created_at)+' | '+self.created_by

class Inscription(models.Model):
    student      = models.ForeignKey("Student", on_delete=models.CASCADE)
    parent       = models.ForeignKey("Parent", on_delete=models.CASCADE)
    program      = models.ForeignKey("Program",on_delete=models.CASCADE)
    membership   = models.ForeignKey("Membership", on_delete=models.CASCADE)
    date_add     = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.first_name

class Parent(models.Model):
    GENDER_C      = (('Father', 'Father'),('Mother', 'Mother'))
    parent_gender = models.CharField( max_length=10,choices=GENDER_C,default='Father')
    fullname      = models.CharField( max_length=30)
    phone         = PhoneField()
    address       = models.CharField( max_length=50)
    description   = models.TextField(max_length=100, null=True)
    

    def __str__(self):
        return self.fullname

class Membership(models.Model):
    monthly = "MONTHLY"
    trimestrial = "TRIMESTRIAL"
    annual = "ANNUAL"
    period_choices = [(monthly, "MONTHLY"), (trimestrial, "TRIMESTRIAL" ),(annual, "ANNUAL")]
    label = models.CharField(max_length=100, blank=True)
    membership_period =models.CharField(max_length=50, choices=period_choices, default=trimestrial,)
    def __str__(self):
        return self.label

