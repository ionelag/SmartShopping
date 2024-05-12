from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from SmartShopping.models import Item
from SmartShopping.forms.add_item_form import (AddItemForm)
import requests

def homepage(request):
    items = Item.objects.all()
    return render(request, 'homepage.html', {'items': items})

def adauga_item(request):
    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item_nou = Item(
                denumire=form.data['denumire'],
                firma_producatoare=form.data['firma_producatoare'],
                descriere=form.data['descriere'],
                greutate=form.data['greutate'],
                pret=form.data['pret'],
                cumparat=False,
                imagine=form.files['imagine']
            )
            item_nou.save()
        return redirect('homepage')
    else:
        form = AddItemForm()
        return render(request, 'add_item.html', {'form': form})

def confirm_marcheaza_ca_achizitionat(request,id_item):
    item = get_object_or_404(Item, pk=id_item)
    return render(request, 'marcheaza_ca_achizitionat.html', {'item': item})

def marcheaza_ca_achizitionat(request, id_item):
    item = get_object_or_404(Item, pk=id_item)
    item.cumparat = True
    item.save()
    return redirect('homepage')

def delete_item(request, id_item):
    item = get_object_or_404(Item, pk=id_item)

    if request.method == 'POST':
        item.delete()
        return redirect('homepage')
    return redirect('delete_item', id_item=id_item)

def confirm_delete_item(request, id_item):
    item = get_object_or_404(Item, pk=id_item)
    return render(request, 'delete_item.html', {'item': item})

def get_nutritional_facts(request, id_item):
    item = get_object_or_404(Item, pk=id_item)
    r = requests.get(f'https://eatntrack.ro/calorii/{item.denumire}')

    if r.status_code == 500:
        return render(request, 'not_found.html', {'item': item})

    return HttpResponseRedirect(f'https://eatntrack.ro/calorii/{item.denumire}')
