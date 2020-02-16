from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Network, Show

# Create your views here.
def shows(request):
    context = {
        'all_my_shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def addshow(request):
    context = {
        'all_networks': Network.objects.all()
    }
    return render(request, 'addshow.html', context)

def process_show(request):
    # Pass the post data to the method we wrote and save the request in a
    # variable called errors.
    errors = Show.objects.basic_validator(request.POST)
    # if there are any errors, then put them in the dictionary

    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)
        # redirect to the page to fix the errors
        return redirect('/addshow')
    
    showName = request.POST['show_name']
    showNetwork = Network.objects.get(id=request.POST['show_network'])
    showRelease = request.POST['show_release']
    showDesc = request.POST['show_desc']
    print(showName, showNetwork, showRelease, showDesc)
    
    Show.objects.create(name=showName, network=showNetwork, release_date=showRelease, desc=showDesc)
    print('show added')
    message.success(request, 'Show sucessfully added')
    return redirect('/addshow')

def show_detail(request, my_int):
    currentShow = Show.objects.get(id=my_int)

    context = {
        'current_show': currentShow,
    }
    return render(request, 'showtemplate.html', context)

def delete_record(request, my_int):
    currentShow = Show.objects.get(id=my_int)
    currentShow.delete()
    print('You sho has been trashed')

    return redirect("/")

def edit_record(request, my_int):
    currentShow = Show.objects.get(id=my_int)

    context = {
        'current_id': my_int,
        'current_title': currentShow.name,
        'current_network': currentShow.network.id,
        'current_release': currentShow.release_date,
        'current_desc': currentShow.desc,
        'all_networks': Network.objects.all()
    }

    return render(request, 'edittemplate.html', context)

def process_edit(request, my_int):
    c = Show.objects.get(id=my_int)
    newTitle = request.POST['new_title']
    newNetwork = Network.objects.get(id=request.POST['new_network'])
    newRelease = request.POST['new_release_date']
    newDesc = request.POST['new_description']

    print(newTitle, newRelease, newDesc)

    # Pass the post data to the method we wrote and save the request in a
    # variable called errors.
    errors = Show.objects.edit_validator(request.POST)
    # if there are any errors, then put them in the dictionary

    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)
        # redirect to the page to fix the errors
        return redirect('/' + str(my_int) + '/edit')

    c.name = newTitle
    c.network = newNetwork
    c.release_date = newRelease
    c.desc = newDesc
    c.save()
    print('update saved Yo')
    messages.success(request, "Record has been updated")
    return redirect('/' + str(my_int) + '/edit')