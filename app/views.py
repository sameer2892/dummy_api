import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import *
import re
from django.contrib.auth import authenticate, login, logout


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


@csrf_exempt
def get_data(request):
    venue_list = []
    days_list = []
    city_list = []
    venuecategory_list = []
    vendor_list = []
    paymenttype_list = []

    paymenttype_list.append({
        'id': 1,
        'name': "At venue",
        'percentage_paid': 0
    })
    paymenttype_list.append({
        'id': 2,
        'name': "Half",
        'percentage_paid': 50
    })
    paymenttype_list.append({
        'id': 3,
        'name': "Full",
        'percentage_paid': 100
    })

    city_list.append({
        'id': 1,
        'name': "City1",
        'code': "C1"
    })
    city_list.append({
        'id': 2,
        'name': "City2",
        'code': "C2"
    })

    venuecategory_list.append({
        'id': 1,
        'name': "pub"
    })
    venuecategory_list.append({
        'id': 2,
        'name': "cafe"
    })

    vendor_list.append({
        'id': 1,
        'user_id': 3
    })

    days_list.append({'id': 1, 'name': "Monday"})
    days_list.append({'id': 2, 'name': "Tuesday"})
    days_list.append({'id': 3, 'name': "Wednesday"})
    days_list.append({'id': 4, 'name': "Thursday"})
    days_list.append({'id': 5, 'name': "Friday"})
    days_list.append({'id': 6, 'name': "Saturday"})
    days_list.append({'id': 7, 'name': "Sunday"})

    venue_list.append({
        'id': 1,
        'name': "venue1",
        'category': 1,
        'rating': 4,
        'votes': 1000,
        'coordinates': None,
        'city': 1,
        'image': "../../static/assets/images/sample.png",
        'details': {'why_we_lie_it': "God knows", 'crowd': "Hippie", 'busy_nights': "[1,2]"},
        'vendor': 1,
        'events': [
            {
                'id': 1,
                'name': "event1",
                'date': "2016-10-22",
                'likes': 1000
            },
            {
                'id': 2,
                'name': "event2",
                'date': "2016-10-02",
                'likes': 500
            }
        ],
        'tables': [
            {
                'id': 1,
                'days': [1, 2],
                'name': "table1",
                'guests_no': 2,
                'min_spend': 1000,
                'description': "this is table 1"
            },
            {
                'id': 2,
                'days': [3, 4],
                'name': "table2",
                'guests_no': 3,
                'min_spend': 1500,
                'description': "this is table 2"
            }
        ],
        'packages': [
            {
                'id': 1,
                'days': [1, 2],
                'name': "package1",
                'guests_no': 2,
                'price': 1000,
                'description': "this is package 1"
            },
            {
                'id': 2,
                'days': [3, 4],
                'name': "package1",
                'guests_no': 3,
                'min_spend': 1500,
                'description': "this is package 2"
            }
        ],
        'tickets': [
            {
                'id': 1,
                'days': [1, 2],
                'name': "ticket1",
                'guests_no': 2,
                'price': 1000,
                'description': "this is ticket 1"
            },
            {
                'id': 2,
                'days': [3, 4],
                'name': "ticket1",
                'guests_no': 3,
                'min_spend': 1500,
                'description': "this is ticket 2"
            }
        ],
        'menu_item': [
            {
                'id': 1,
                'name': "item1",
                'description': "this is item 1",
                'price': 1000
            },
            {
                'id': 2,
                'name': "item2",
                'description': "this is item 2",
                'price': 800
            }
        ]

    })

    # venue_list.append({
    #     'id': 2,
    #     'name': "venue2",
    #     'category': "cafe",
    #     'rating': 3,
    #     'votes': 3000,
    #     'coordinates': None,
    #     'city': 2,
    #     'image': "../../static/assets/images/sample1.png",
    #     'details': {'why_we_lie_it': "God knows", 'crowd': "Hiipie", 'busy_nights': "[1,2]"},
    #     'vendor_id': 1})
    #
    # event_list = []
    # event_list.append({'id': 1, 'name': "event1", 'venue': "venue1",
    #                    'date': "2016-10-22", 'likes': 1000})
    #
    # event_list.append({'id': 1, 'name': "event1", 'venue': "venue1",
    #                    'date': "2016-10-22", 'likes': 1000})
    #
    data = {'venues': venue_list, 'days': days_list, 'city': city_list, 'vendor': vendor_list, 'venuecategory': venuecategory_list, 'paymentype': paymenttype_list}
    data = json.dumps(data, default=date_handler)
    return HttpResponse(data, content_type='application/json')


# @csrf_exempt
# def get_venue(request):
#     if request.POST['id'] == "1":
#         monday = [{'table': [{'id': 1}, {'id': 2}], 'package': [], 'ticket': []}]
#         tuesday = [{'table': [], 'package': [{'id': 1}, {'id': 2}], 'ticket': []}]
#         wednesday = [{'table': [], 'package': [{'id': 1}, {'id': 2}], 'ticket': []}]
#         thursday = [{'table': [], 'package': [], 'ticket': [{'id': 1}, {'id': 2}]}]
#         friday = [{'table': [], 'package': [], 'ticket': [{'id': 1}, {'id': 2}]}]
#         saturday = [{'table': [{'id': 1}, {'id': 2}], 'package': [{'id': 1}, {'id': 2}], 'ticket': [{'id': 1}, {'id': 2}]}]
#         sunday = [{'table': [], 'package': [{'id': 1}, {'id': 2}], 'ticket': [{'id': 1}, {'id': 2}]}]
#
#         day = [{'monday': monday, 'tuesday': tuesday, 'wednesday': wednesday, 'thursday': thursday, 'friday': friday,
#                 'saturday': saturday, 'sunday': sunday}]
#
#         data = {'id': 1, 'name': "venue1", 'category': "pub",
#                                'rating': 4, 'votes': 1000, 'coordinates': None, 'city': 1, 'image': "../../static/assets/images/sample.png",
#                                'details': None, 'day': day}
#         data = json.dumps(data)
#         return HttpResponse(data, content_type="application/json")
#     else:
#         return HttpResponse("", content_type='application/json', status=404)
#
#
# @csrf_exempt
# def get_table(request):
#     if request.POST['id'] == "1":
#         data = {'id': 1, 'name': "table1", 'guests': 2,
#                     'min_spend': 1500, 'description': None}
#     elif request.POST['id'] == "2":
#         data = {'id': 2, 'name': "table2", 'guests': 3,
#                  'min_spend': 2000, 'description': None}
#     else:
#         return HttpResponse("", content_type='application/json', status=404)
#
#     data = json.dumps(data)
#     return HttpResponse(data, content_type="application/json")
#
#
# @csrf_exempt
# def get_package(request):
#     if request.POST['id'] == "1":
#         data = {'id': 1, 'name': "package1", 'guests': 2,
#                  'price': 1500, 'description': None}
#     elif request.POST['id'] == "2":
#         data = {'id': 2, 'name': "package2", 'guests': 3,
#                  'price': 2000, 'description': None}
#     else:
#         return HttpResponse("", content_type='application/json', status=404)
#
#     data = json.dumps(data)
#     return HttpResponse(data, content_type="application/json")
#
#
# @csrf_exempt
# def get_ticket(request):
#     if request.POST['id'] == "1":
#         data = {'id': 1, 'name': "ticket1", 'guests': 2,
#                  'price': 1500, 'description': None}
#     elif request.POST['id'] == "2":
#         data = {'id': 2, 'name': "ticket2", 'guests': 3,
#                  'price': 2000, 'description': None}
#     else:
#         return HttpResponse("", content_type='application/json', status=404)
#
#     data = json.dumps(data)
#     return HttpResponse(data, content_type="application/json")
#
#
#
# # table_list = []
# # table_list.append({'id': 1, 'name': "table1", 'guests': 2,
# #                    'min_spend': 1500, 'description': None})
# # table_list.append({'id': 2, 'name': "table2", 'guests': 3,
# #                    'min_spend': 2000, 'description': None})
# #
# # package_list = []
# # package_list.append({'id': 1, 'name': "package1", 'guests': 2,
# #                    'price': 2000, 'description': None})
# # package_list.append({'id': 2, 'name': "package2", 'guests': 3,
# #                    'price': 2500, 'description': None})
# #
# # ticket_list = []
# # ticket_list.append({'id': 1, 'name': "ticket1", 'guests': 1,
# #                      'price': 500, 'description': None})
# # ticket_list.append({'id': 2, 'name': "ticket2", 'guests': 3,
# #                     'price': 1000, 'description': None})
#
# @csrf_exempt
# def get_event(request):
#     if request.POST['id'] == "1":
#         data = {'id': 1, 'name': "event1", 'date': "2016-10-22", 'venue': "venue1", 'likes': 0}
#         data = json.dumps(data, default=date_handler)
#         return HttpResponse(data, content_type="application/json")
#     else:
#         return HttpResponse("", content_type='application/json', status=404)
#
#
# @csrf_exempt
# def get_menu(request):
#     if request.POST['id'] == "1":
#         menu_list = []
#         menu_list.append({'id': 1, 'name': "item1", 'price': 500, 'description': None})
#         menu_list.append({'id': 2, 'name': "item2", 'price': 700, 'description': None})
#         menu_list.append({'id': 3, 'name': "item3", 'price': 900, 'description': None})
#         menu_list.append({'id': 4, 'name': "item4", 'price': 1000, 'description': None})
#         data = {'items': menu_list}
#         data = json.dumps(data)
#         return HttpResponse(data, content_type="application/json")
#     else:
#         return HttpResponse("", content_type='application/json', status=404)
#
#
# # @csrf_exempt
# # def get_my_bookings(request):
# #     customer_id = request.POST['id']
# #     customer = Customer.objects.get(pk=customer_id).user.first_name
# #     all_carts = Cart.objects.filter(customer=customer_id)
# #     cart_list = []
# #     for cart in all_carts:
# #         cart_id = cart.id
# #         cart_list.append({'id': cart_id})
# #
# #     data = {'customer': customer, 'carts': cart_list}
# #     data = json.dumps(data)
# #     return HttpResponse(data, content_type="application/json")
#
#
# @csrf_exempt
# def register(request):
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#         if username == "user1" or username == "user2" or username == "user3":
#             message = "UF"
#         else:
#             if not re.match(r'(?=.*[!@#$%^&*()_+=])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', password):
#                 message = "PF"
#             else:
#                 message = "S"
#
#     else:
#         message = "NP"
#
#     data = {'message': message}
#     data = json.dumps(data, default=date_handler)
#     return HttpResponse(data, content_type="application/json")
#
#
# @csrf_exempt
# def login(request):
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#         if (username == "user1" and password == "user1") or (username == "user2" and password == "user2") or (username == "user3" and password == "user3"):
#             if username == "user1" or username == "user2":
#                 message = "S"
#             else:
#                 message = "NC"
#         else:
#             message = "F"
#     else:
#         message = "NP"
#
#     data = {'message': message}
#     data = json.dumps(data)
#     return HttpResponse(data, content_type="application/json")
#
#
# @csrf_exempt
# def get_all_cities(request):
#     city_list = []
#     city_list.append({'id': 1, 'code': "C1", 'name': "city1"})
#     city_list.append({'id': 2, 'code': "C2", 'name': "city2"})
#     city_list.append({'id': 3, 'code': "C3", 'name': "city3"})
#     data = {'cities': city_list}
#     data = json.dumps(data)
#     return HttpResponse(data, content_type="application/json")
#
#
# @csrf_exempt
# def get_card(request):
#     if request.POST['id'] == "1":
#         data = {'id': 1, 'full_name': "user1", 'card_number': "1234234534564567", 'expiry_date': "2020-07-17", 'cvv': "456"}
#     elif request.POST['id'] == "2":
#         data = {'id': 1, 'full_name': "user2", 'card_number': "2345123445673456", 'expiry_date': "2018-01-19", 'cvv': "123"}
#     else:
#         return HttpResponse("", content_type="application/json", status=404)
#
#     data = json.dumps(data)
#     return HttpResponse(data, content_type="application/json")
#
