from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import Image
from .models import LoadMultipleImages
from .data import *

# Create your views here.

def index(request):
    
    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def SingIn(request):
    if request.method == 'POST':
        luser = request.POST

        for _user in users:
            if _user['login'] == luser['login'] and _user['password'] == luser['password']:
                global isLogin, isAdmin, user
                isLogin = True
                isAdmin = bool(_user['isAdmin'])
                user = _user
                

                print(isAdmin)
                return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
        return render(request, 'main\SingIn.html', {'isFailed': True, 'categoryes': categoryes})
    else: return render(request, 'main\SingIn.html', {'categoryes': categoryes})

def SingUp(request):
    if request.method == 'POST':
        ruser = request.POST
        form = Image(ruser, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            global users, user, isLogin, isAdmin

            for _user in users:
                if _user['login'] == ruser['login']:
                    return render(request, 'main\SingUp.html', {'form': Image, 'categoryes': categoryes})

            users.append({
                'login': ruser['login'],
                'password': ruser['password'],
                'isAdmin': False,
                'img': img_obj.image.url
            })

            isLogin = True
            isAdmin = False
            user = users[len(users) - 1]
            

            return render(request, 'main\index.html', {'products': products,  'categoryes': categoryes, 'category': category,  'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else: return render(request, 'main\SingUp.html', {'form': Image, 'categoryes': categoryes})

def Exit(request):
    global isAdmin, isLogin, user
    isAdmin = False
    isLogin = False
    user = None

    
    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def Sort(request):
    global category
    category = None if request.POST['Category'] == "Все" else request.POST['Category']
    
    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    
def Search(request):
    resul = []
    
    for item in products:
        if str(item['name']).lower() == request.POST['Search'].lower() or str(item['name']).lower().__contains__(request.POST['Search'].lower()):
            if category != None and item['category'] == category:
                resul.append(item)
            else:
                resul.append(item)

    if len(resul) > 0:
        return render(request, 'main\index.html', {'products': resul, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        if category == None:
            return render(request, "main\Error.html", {'error': "По запросу '" + request.POST['Search'] + "' ничего не найдено!"})
        else:
            return render(request, "main\Error.html", {'error': "В категории '" + category + "' по запросу '" + request.POST['Search'] + "' ничего не найдено!"})

def Remove(request):
    name = request.POST['name']

    _list = []

    for item in products:
        if item['name'] != name:
            _list.append(item)

    products.clear()
    for item in _list:
        products.append(item)

    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def About(request):
    if request.method == 'POST':
        pass
    else:
        product = GetProductByName(request.GET['name'])

        sum = 0
        haveUserComment = False

        try:
            for comment in product['comments']:
                sum += int(comment['raiting'])
                if comment['user']['login'] == user['login']:
                    haveUserComment = True
            
            return render(request, 'main/about.html', {'user': user, 'isLogin': isLogin, 'categoryes': categoryes, 'product': product, 'aRaiting': sum/len(product['comments']), 'haveUserComment': haveUserComment})
        except:
            return render(request, 'main/about.html', {'user': user, 'isLogin': isLogin, 'categoryes': categoryes, 'product': product, 'aRaiting': 0, 'haveUserComment': haveUserComment})

def Comment(request):

    for product in products:
        if product['name'] == request.POST['name']:
            product['comments'].append({
                'user': user,
                'raiting': int(request.POST['raiting']),
                'comment': request.POST['comment'],
            })
            break

    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def AddGame(request):
    if request.method == 'POST':
        newProduct = request.POST
        
        form = Image(newProduct, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            my_file=request.FILES.getlist('images')
            screens = list()

            for file in my_file:
                new_file = LoadMultipleImages(
                    image = file
                )
                new_file.save()
                screens.append(new_file.image.url)

            products.append({
                'name': newProduct['name'],
                'category': newProduct['category'],
                'img': img_obj.image.url,
                'price': float(newProduct['price']),
                'screens': screens,
                'comments': []
            })
        return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        return render(request, 'main\AddGame.html', {'categoryes': categoryes, 'form': Image})

def Change(request):
    if request.method == 'POST':
        newProduct = request.POST

        my_file=request.FILES.getlist('screens')
        screens = list()

        for file in my_file:
            new_file = LoadMultipleImages(
                image = file
            )
            new_file.save()
            screens.append(new_file.image.url)

        for item in products:
            if item['name'] == newProduct['oldName']:

                item['name'] = newProduct['name']
                item['category'] = newProduct['category']
                item['img'] = newProduct['img']
                item['price'] = float(newProduct['price'])

                if len(screens) > 0:
                    item['screens'] = screens
                break

        return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:

        for item in products:
            if item['name'] == request.GET['name']:
                return render(request, 'main\Change.html', {'categoryes': categoryes, 'product': item})