# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

# Own
from user_information.models import Queries, SearchWords, UseOfCategories
from publications.models import Publication
from opening.models import Opening
from products.models import Product, Category, Brand

# Third Party
from datetime import datetime, timedelta


@require_http_methods(["GET"])
def HomeView(request):
    """Home View"""
    # Opening
    opening = Opening.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    listWords = SearchWords.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'listWords': listWords,
        'opening': opening
    }

    return render(request, 'home/home.html', context)


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
