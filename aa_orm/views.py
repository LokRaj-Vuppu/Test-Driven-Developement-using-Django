from django.shortcuts import render
from aa_orm.models import Restaurant, Sale, Rating, Staff, StaffRestaurant
# Create your views here.

def index(request):
    # 
    # restaurants = Restaurant.objects.prefetch_related('ratings', 'sales').filter(name__startswith='c')
    # staffs = Staff.objects.all()
    # for staff in staffs:
    #     print(staff.restaurants.all())
    srs = StaffRestaurant.objects.all().prefetch_related('staff', 'restaurant')
    for sr in srs:
        print(sr.staff.name)
        print(sr.restaurant.name)
        print(sr.salary)
    return render(request, 'aa_orm/index.html')