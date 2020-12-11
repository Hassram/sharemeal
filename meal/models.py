from django.db import models
from datetime import datetime
from userapp.models import User
import re
portion_regex=re.compile(r'^[0-9]+$')

# Create your models here.

class MealManager(models.Manager):
    
    def validate(self,form):
        errors={}
        if len(form['meal_name'])<3:
            errors['meal_name']="Meal name should be at least 3 characters"
        if len(form['meal_note'])<3:
            errors['meal_note']="Meal note should be at least 3 characters"
        if not form['offered_portion'].isnumeric():
            errors['offered_portion']="Meal portion should be an integer"
        if datetime.now().date() > datetime.strptime(form['date'],'%Y-%m-%d').date():
            errors['date']="date should be today or in future"
            print (datetime.now().date() , "fro mform  vs. from code", datetime.strptime(form['date'],'%Y-%m-%d').date())



        
        return errors

class MealType(models.Model):
    catagory=models.CharField(max_length=45)
    unit_cost=models.IntegerField()


class Meal(models.Model):
    meal_name = models.CharField(max_length=45)
    meal_note= models.CharField(max_length=255)
    date=models.DateField()
    cook=models.ForeignKey(User,related_name='cook_meals',on_delete=models.CASCADE)
    ordered_by=models.ManyToManyField(User,related_name='orders')
    mealcost=models.ForeignKey(MealType,related_name='token_need',on_delete=models.CASCADE)
    offered_portion=models.IntegerField(default=4)
    objects=MealManager()



