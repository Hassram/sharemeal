from django.contrib import messages
from django.shortcuts import redirect, render
from userapp.models import User

from .models import Meal, MealType


# Create your views here.
def index(request):  #display main page with all the meals on display
    user = User.objects.get(id=request.session['user_id'])
    cook_meals=user.cook_meals.all().order_by('-date')
    messages.success(request, "You have successfully logged in!")
    meals=Meal.objects.all().order_by('-date')
    context = {
        'user': user,
        'cook_meals':cook_meals,
        'meals':meals,
        }
    return render(request,'meal.html',context)
    
def newmeal(request): # redner new meal page,
    print(request)
    errors={}
    messages={}
    allmealtype=MealType.objects.all()
    user = User.objects.get(id=request.session['user_id'])
    usermeals= user.cook_meals.all()

    #creating content dic with  mealtype and usermeals
    context={
        'mealtype':allmealtype,
        'usermeals':usermeals,
    }

    return render(request,'newmeal.html',context)

def mealregister(request):
    errors=Meal.objects.validate(request.POST)
    print ("************",errors)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/meals/newmeal')
    else:
        Meal.objects.create(
            meal_name=request.POST['meal_name'],
            meal_note=request.POST['meal_note'],
            date=request.POST['date'],
            cook=User.objects.get(id=request.session['user_id']),
            mealcost=MealType.objects.get(catagory=request.POST['mealtype']),
            offered_portion=request.POST['offered_portion']
        )
        return redirect('/meals/newmeal')

def delete(request,id):
    Meal.objects.get(id=id).delete()
    return redirect('/meals')

def add(request,id):
    meal=Meal.objects.get(id=id)
    cook=Meal.objects.get(id=id).cook
    user = User.objects.get(id=request.session['user_id'])

    print ("cook token at begin of exchange  is :", cook.token)

    meal.ordered_by.add(User.objects.get(id=request.session['user_id'])) #adding to ordered by
    meal.offered_portion -=1
    #udating cook's token
    cook.token +=meal.mealcost.unit_cost
    cook.save()
    meal.save()
    #udating user token
    
    user.token -=meal.mealcost.unit_cost
    user.save()

    print ("cook token now is :", meal.cook.token, "after add of ", meal.mealcost.unit_cost)
    return redirect('/meals')


def remove(request,id):

    
    meal=Meal.objects.get(id=id)
    cook=Meal.objects.get(id=id).cook
    user = User.objects.get(id=request.session['user_id'])

    print ("cook token at begin of exchange  is :", cook.token)

    Meal.objects.get(id=id).ordered_by.remove(User.objects.get(id=request.session['user_id'])) #adding to ordered by
    meal.offered_portion +=1
    #udating cook's token
    cook.token -=meal.mealcost.unit_cost
    cook.save()
    meal.save()
    #udating user token
    
    user.token +=meal.mealcost.unit_cost
    user.save()

    print ("cook token now is :", meal.cook.token, "after add of ", meal.mealcost.unit_cost)
    return redirect('/meals')

def mylist(request):
    user = User.objects.get(id=request.session['user_id'])
    usermeals= user.cook_meals.all().order_by('-date')

    #creating content dic with  mealtype and usermeals
    context={
        'usermeals':usermeals,
    }
    
    return render(request,'mylist.html',context)
