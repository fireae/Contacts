from django.shortcuts import render_to_response
from address_book.models import  AddressBookUser

# Create your views here.
def list_address(request):
    title_array = []
    i = 0
    for t_data in AddressBookUser.objects.all():
        u_data = {}
        u_data['user_name'] = t_data.user_name
        u_data['user_pwd'] = t_data.user_pwd
        i = i+1
    return render_to_response('list.html', {'title_array': title_array, 'count': i})