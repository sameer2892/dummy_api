import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import *
import re
from django.contrib.auth import authenticate, login, logout


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


@csrf_exempt
def get_all_venues_events(request):
    venue_list = []
    venue_list.append({'id': 1, 'name': "venue1", 'category': "pub",
            'rating': 4, 'votes': 1000, 'coordinates': None, 'city': 1, 'image': "../../static/assets/images/sample.png",
                'details': None})

    venue_list.append({'id': 2, 'name': "venue2", 'category': "cafe",
                       'rating': 3, 'votes': 3000, 'coordinates': None, 'city': 2,
                       'image': "../../static/assets/images/sample1.png",
                       'details': None})

    event_list = []
    event_list.append({'id': 1, 'name': "event1", 'venue': "venue1",
                       'date': "2016-10-22", 'likes': 1000})

    event_list.append({'id': 1, 'name': "event1", 'venue': "venue1",
                       'date': "2016-10-22", 'likes': 1000})

    data = {'venues': venue_list, 'events': event_list}
    data = json.dumps(data, default=date_handler)
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def get_venue(request):
    if request.POST['id'] == "1":
        table_list = []
        table_list.append({'id': 1, 'name': "table1", 'guests': 2,
                           'min_spend': 1500, 'description': None})
        table_list.append({'id': 2, 'name': "table2", 'guests': 3,
                           'min_spend': 2000, 'description': None})

        package_list = []
        package_list.append({'id': 1, 'name': "package1", 'guests': 2,
                           'price': 2000, 'description': None})
        package_list.append({'id': 2, 'name': "package2", 'guests': 3,
                           'price': 2500, 'description': None})

        ticket_list = []
        ticket_list.append({'id': 1, 'name': "ticket1", 'guests': 1,
                             'price': 500, 'description': None})
        ticket_list.append({'id': 2, 'name': "ticket2", 'guests': 3,
                            'price': 1000, 'description': None})

        data = {'id': 1, 'name': "venue1", 'category': "pub",
                               'rating': 4, 'votes': 1000, 'coordinates': None, 'city': 1, 'image': "../../static/assets/images/sample.png",
                               'details': None, 'tables': table_list, 'packages': package_list, 'tickets': ticket_list}
        data = json.dumps(data)
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse("", content_type='application/json', status=404)


@csrf_exempt
def get_event(request):
    if request.POST['id'] == "1":
        data = {'id': 1, 'name': "event1", 'date': "2016-10-22", 'venue': "venue1", 'likes': 0}
        data = json.dumps(data, default=date_handler)
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse("", content_type='application/json', status=404)


# @csrf_exempt
# def get_my_bookings(request):
#     customer_id = request.POST['id']
#     customer = Customer.objects.get(pk=customer_id).user.first_name
#     all_carts = Cart.objects.filter(customer=customer_id)
#     cart_list = []
#     for cart in all_carts:
#         cart_id = cart.id
#         cart_list.append({'id': cart_id})
#
#     data = {'customer': customer, 'carts': cart_list}
#     data = json.dumps(data)
#     return HttpResponse(data, content_type="application/json")


@csrf_exempt
def register(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if username == "user1" or username == "user2" or username == "user3":
            message = "UF"
        else:
            if not re.match(r'(?=.*[!@#$%^&*()_+=])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', password):
                message = "PF"
            else:
                message = "S"

    else:
        message = "NP"

    data = {'message': message}
    data = json.dumps(data, default=date_handler)
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if (username == "user1" and password == "user1") or (username == "user2" and password == "user2") or (username == "user3" and password == "user3"):
            if username == "user1" or username == "user2":
                message = "S"
            else:
                message = "NC"
        else:
            message = "F"
    else:
        message = "NP"

    data = {'message': message}
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")