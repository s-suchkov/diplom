from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import SignupForm
from .models import Article, Section, Products, Review, Order, Basket
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    template_name = 'base.html'
    sections = Section.objects.all()
    if request.method == 'POST':
        basket, created = Basket.objects.get_or_create(author=request.user.email, buy=False)
        product = Products.objects.get(id=request.POST['cart'])
        basket.product.add(product)
        basket.save()
    context = {
        'article': Article.objects.order_by('date').all(),
        'sections': sections
    }
    return render(request, template_name, context)



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return HttpResponseRedirect('/login')
    else:
        form = SignupForm()
    return render(
        request,
        'signup.html',
        {'form': form,
        'sections': Section.objects.all()}
    )


def section(request):
    id = int(request.GET.get('id'))
    print(id)
    section = Section.objects.get(id=id)

    contact_list = section.products_set.all()
    paginator = Paginator(contact_list, 3)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
        # return render_to_response('list.html', {"contacts": contacts}

    if request.method == 'POST':
        print(request.POST)
        basket, created = Basket.objects.get_or_create(author=request.user.email, buy=False)
        product = Products.objects.get(id=request.POST['cart'])
        basket.product.add(product)
        basket.save()
    template_name = 'smartphones.html'
    context = {
        'sec': section,
        'sections': Section.objects.all(),
        'contacts': contacts
    }
    return render(request, template_name, context)

def phone(request):
    id = request.GET.get('id_product')
    product = Products.objects.get(id=id)
    print(request.POST)
    if request.method == 'POST':
        if request.POST.get('mark') != None:
            mark = '★' * int(request.POST['mark'])
            if request.POST['name'] == '':
                name = 'Аноним'
            else:
                name = request.POST['name']
            Review.objects.create(products=product, name=name, text=request.POST['description'], rating=mark)
            return HttpResponseRedirect(request.get_full_path())
        elif request.POST.get('merchandise_id') != None:
            basket, created = Basket.objects.get_or_create(author=request.user.email, buy=False)
            product = Products.objects.get(id=request.POST['merchandise_id'])
            basket.product.add(product)
            basket.save()

    template_name = 'phone.html'
    context = {
        'product': product,
        'sections': Section.objects.all(),
    }
    return render(request, template_name, context)

def basket(request):
    template_name = 'cart.html'
    basket, created = Basket.objects.get_or_create(buy=False, author=request.user.email)
    print(basket)
    length = len(basket.product.all())
    if request.method == 'POST' and request.POST.get('order') == 'true':
        basket.buy = True
        ord = Order.objects.create(date=datetime.datetime.now(), username=request.user.email, count=length)
        basket.order = ord
        basket.save()
        length = 0
    basket = Basket.objects.filter(buy=False, author=request.user.email)
    context = {
        'len': length,
        'basket': basket,
        'sections': Section.objects.all(),
    }
    return render(request, template_name, context)

