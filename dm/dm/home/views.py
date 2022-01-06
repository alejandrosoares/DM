# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

# Own
from user_information.models import Queries, SearchWords, UseOfCategories, UserInformation
from publications.models import Publication
from opening.models import Opening
from products.models import Product, Category, Brand
from .utils import (
   RecordMaker,
   create_userid_for_cookies,
   RecordVisit,
   RoundPrice
)


# Third Party
from datetime import datetime, timedelta

def get_date_cookies():
   """Get date for cookies 
   @return: sts
   """
   expiration_days = 365
   date = datetime.now() + timedelta(days=expiration_days)

   return date.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

def get_userid_cookies(dicCookies):
   """Get userid for cookies
   Get or create userid for insert in cookies

   @param: dict
   @return: bool, str
   """

   if 'userid' not in dicCookies:

      return True, create_userid_for_cookies()

   return False, dicCookies.get('userid')

def GetProducts(publicationCode, userid):
    #	Funcion para obtener los productos de manera personalizada
    # 	Viene desde una publicacion entonces muestra los p de la publicacion

    isPublication = False

    if publicationCode:
        try:
            p = Publication.objects.get(code=publicationCode)
            p.numberOfVisites = p.numberOfVisites + 1
            p.save()

            try:
                u = UserInformation.objects.get(userid=userid)
                p.users.add(u)
            except UserInformation.DoesNotExist:
                print(
                    "Error en RegisteringPublication: no existe el usuario para asignar a la publicacion")

            products = p.products.all()
            isPublication = True
        except:
            print("Error en Home-HomeView: no existe la publicacion")
            products = Product.objects.all().order_by("-id")
    else:
        products = Product.objects.all().order_by("-id")

    return products, isPublication


def DetectUserAgent(request):

    acceptWebp = False
    browser = request.user_agent.browser.family
    stringVersion = request.user_agent.browser.version_string

    # Formateo de  string
    dotCount = stringVersion.count(".")
    if dotCount > 1:
        while dotCount > 1:
            index = stringVersion.rfind(".")
            stringVersion = stringVersion[:index]
            dotCount -= 1

    versionBrowser = float(stringVersion)

    if (browser == "Chrome" and versionBrowser >= 9) or ((browser == "Chrome for Android" or browser == "Chrome Mobile") and versionBrowser >= 87):
        acceptWebp = True
    elif (browser == "Firefox" and versionBrowser >= 65) or ((browser == "Firefox for Android" or browser == "Firefox Mobile") and versionBrowser >= 83):
        acceptWebp = True
    elif browser == "Edge" and versionBrowser >= 18:
        acceptWebp = True
    elif browser == "Safari" and versionBrowser >= 14:
        acceptWebp = True
    elif browser == "Opera" and versionBrowser >= 11.5:
        acceptWebp = True
    elif browser == "Opera Mini":
        acceptWebp = True
    elif browser == "iOS Safari" and versionBrowser >= 14.2:
        acceptWebp = True
    elif browser == "Android Browser" and versionBrowser >= 4:
        acceptWebp = True
    elif browser == "UC Browser for Android" and versionBrowser >= 12.12:
        acceptWebp = True
    elif browser == "Samsung Internet" and versionBrowser >= 4:
        acceptWebp = True

    versionBrowser = str(versionBrowser)

    if acceptWebp:
        print("Acepta cookies")
    else:
        print("no acepta cookies")

    return acceptWebp, browser, versionBrowser


def AWCookies(request, dicCookies):
    # Verificacion de las cookies para saber si el navegador del usuario acepta img webp
    if 'aw_cookie' not in dicCookies:  # La cookie no esta configurada
        acceptWebp, browser, versionBrowser = DetectUserAgent(request)

    else:  # La cookie esta configurada
        aw_cookie = dicCookies.get("aw_cookie", False)

        # Ya tengo el navegador y la version
        browser = None
        versionBrowser = None

        if aw_cookie == "1":
            acceptWebp = True
        else:
            acceptWebp = False

    return acceptWebp, browser, versionBrowser


@require_http_methods(["GET"])
def HomeView(request):
   categories = Category.objects.all()
   listWords = SearchWords.objects.all()
   publicationCode = request.GET.get("c", False)
   lastPage = request.META.get('HTTP_REFERER', None)
   acceptWebp, browser, versionBrowser = AWCookies(request, request.COOKIES)
   createdUser, userid = get_userid_cookies(request.COOKIES)
   products, isPublication = GetProducts(publicationCode, userid)

   # Opening
   opening = Opening.objects.all()
   products = Product.objects.all()

   context = {
      'products': products,
      'categories': categories,
      'listWords': listWords,
      'isPublication': isPublication,
      'acceptWebp': acceptWebp,
      'opening': opening
   }

   response = render(request, 'home/home.html', context)

   date = get_date_cookies()

   if createdUser:
      response.set_cookie('userid', userid, max_age=None, expires=date,
                           path='/', domain=None, secure=False, httponly=True)

   if acceptWebp:
      response.set_cookie('aw_cookie', "1", max_age=None, expires=date,
                           path='/', domain=None, secure=False, httponly=True)
   else:
      response.set_cookie('aw_cookie', "0", max_age=None, expires=date,
                           path='/', domain=None, secure=False, httponly=True)

   # Registrando Visita con la pagina de donde proviene
   RecordVisit(userid, lastPage, browser, versionBrowser)
   
   return response


@require_http_methods(["GET"])
def SearchByIdView(request):
    '''
            Vista que realiza las busquedas por id
            Utilizada para responder a las busquedas que se realizan en el input de busqueda y que a partir de lo
            que coincide con lo que el usuario escribe, se realiza la busqueda del item por su id
    '''
    identifier = request.GET.get('q', False)
    typeQuery = request.GET.get('t', False)

    acceptWebp, browser, versionBrowser = AWCookies(request, request.COOKIES)

    if identifier and typeQuery:
        if typeQuery == 'p':
            # Se selecciono un producto
            products = Product.objects.filter(id=int(identifier))
            if len(products) == 0:
                products = Product.objects.all().order_by("-id")
            else:
                # Se produjo una consulta correcta
                # Se registra la consulta realizada
                listSearch = SearchWords.objects.filter(
                    typeString='p', idObject=identifier)
                o = listSearch[0]
                o.quantity = o.quantity + 1
                o.save()
        else:
            # Se selecciono una marca
            try:

                brand = Brand.objects.get(id=int(identifier))
                products = Product.objects.filter(brand=brand)
                if len(products) == 0:
                    # Si la marca existe pero no tiene productos asociados (se borran todos los productos de una marca)
                    products = Product.objects.all().order_by("-id")
                else:
                    # Se produjo una consulta correcta
                    # Se registra la consulta realizada
                    listSearch = SearchWords.objects.filter(
                        typeString='b', idObject=identifier)
                    o = listSearch[0]
                    o.quantity = o.quantity + 1
                    o.save()
            except Brand.DoesNotExist:
                products = Product.objects.all().order_by("-id")
    else:
        products = Product.objects.all().order_by("-id")

    print("acceptWebp", acceptWebp)

    return render(request, 'products/products.html', {'products': products, 'acceptWebp': acceptWebp})


@require_http_methods(["GET"])
def SearchByCategoryView(request):
    '''
            Remplazar las tildes de los nombres
            Si busca varias palabras tengo que generar la lista con cada palabra
    '''
    idCategory = request.GET.get('q', False)
    acceptWebp, browser, versionBrowser = AWCookies(request, request.COOKIES)

    if idCategory:
        if int(idCategory) == 0:
            # Etiqueta que trae todas las categorias
            products = Product.objects.all().order_by("-id")
        else:
            try:
                category = Category.objects.get(id=int(idCategory))
                products = Product.objects.filter(category=category)
                if len(products) == 0:
                    products = Product.objects.all().order_by("-id")
                else:
                    # La consulta de la categoria fue exitosa
                    categoryUsed = UseOfCategories.objects.filter(
                        category=category)
                    c = categoryUsed[0]
                    c.quantity = c.quantity + 1
                    c.save()

            except Category.DoesNotExist:
                products = Product.objects.all().order_by("-id")
    else:
        products = Product.objects.all().order_by("-id")

    return render(request, 'products/products.html', {'products': products, 'acceptWebp': acceptWebp})


@require_http_methods(["GET"])
def SearchView(request):
    '''
            Remplazar las tildes de los nombres
            Si busca varias palabras tengo que generar la lista con cada palabra
    '''
    query = request.GET.get('q', False)
    if query:
        Queries.objects.create(query=query)
        query = query.replace("á", "a").replace("é", "e").replace(
            "í", "i").replace("ó", "o").replace("ú", "u")

        # Se Elimina los parentesis con la marca en caso de que los tenga
        if '(' in query:
            index = query.index("(")
            query = query[:index].strip()

        products = Product.objects.filter(Q(name__icontains=query) | Q(
            code__icontains=query) | Q(brand__brandName__icontains=query))
    else:
        products = Product.objects.all().order_by("-id")

    return render(request, 'products/products.html', {'products': products, 'query': query})


@require_http_methods(["POST"])
def ReceivingData(request):

    string = request.POST.get('listCodes', False)
    userid = request.COOKIES.get('userid', False)

    if userid:
        if string:
            try:
                userinfo = UserInformation.objects.get(userid=userid)
                # RecordMaker(string, userinfo)
            except UserInformation.DoesNotExist:
                print("Se modifico la cookie en el navegador de usuario")
        else:
            print("No se el parametro de peticion POST 'listCodes'")
    else:
        if string:
            # Registrando los datos como usuarios anonimos
            userinfo = UserInformation.objects.get(userid="2020251100000")
            # RecordMaker(string, userinfo)
        else:
            print("No se el parametro de peticion POST 'listCodes'")

    return HttpResponse("ok")


def Pruebas(request):
    # aw_cookie -> accept webp cookie

    products = Product.objects.filter(vendor__name="RAYABO")

    if 'aw_cookie' not in request.COOKIES:  # La cookie no esta configurada
        acceptWebp = DetectUserAgent(request)
        response = render(request, 'home/pruebas.html',
                          {'products': products, 'acceptWebp': acceptWebp})

        date = datetime.now() + timedelta(days=365)
        date = date.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

        if acceptWebp:
            response.set_cookie('aw_cookie', "1", max_age=None, expires=date,
                                path='/', domain=None, secure=False, httponly=True)
        else:
            response.set_cookie('aw_cookie', "0", max_age=None, expires=date,
                                path='/', domain=None, secure=False, httponly=True)
    else:  # La cookie esta configurada
        aw_cookie = request.COOKIES.get("aw_cookie", False)

        if aw_cookie == "1":
            acceptWebp = True
        else:
            print("Nav NO acepta wepb")
            acceptWebp = False

    for x in products:
        print(f'{x.name} - {x.img_webp.url}')

    response = render(request, 'home/pruebas.html',
                      {'products': products, 'acceptWebp': acceptWebp})

    return response


def Pruebas2(request):

    products = Product.objects.all()

    for p in products:
        p.save()

    return HttpResponse("ok")
