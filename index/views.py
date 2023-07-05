from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, Http404
from .models import Coliseum, Fortress, Pyramid, User
from .forms import ColiseumForm, FortressForm, PyramidForm
from django.contrib.auth.decorators import login_required
from .utils import unplublish_all_portifolios

def index(request):
    return render(request, 'pages/home.html')


def create_portifolio_page(request, model_id):

    form = None

    if model_id == 'coliseum' : form = ColiseumForm()
    if model_id == 'fortress' : form = FortressForm()
    if model_id == 'pyramid'  : form = PyramidForm()
        

    return render(request, 'pages/create_portifolio.html', {
        'form': form,
        'model_id': model_id,
    })


   
login_required(login_url='/accounts/login/')
def create_portifolio(request, model_id):

    POST = request.POST

    if not POST:
        return redirect(reverse("create_page"))
    
    form = None
    if model_id == 'coliseum' : form = ColiseumForm(POST)
    if model_id == 'fortress' : form = FortressForm(POST)
    if model_id == 'pyramid'  : form = PyramidForm(POST)
    
    
    if form.is_valid():
        portifolio = form.save(commit=False)
        portifolio.user = request.user
        portifolio.save()
        return redirect(reverse("meus_portifolios"))
    

login_required(login_url='/accounts/login/')
def meus_portifolios(request):

    coliseum = Coliseum.objects.filter(user=request.user)
    fortress = Fortress.objects.filter(user=request.user)
    pyramid = Pyramid.objects.filter(user=request.user)

    return render(request, 'pages/portifolios.html', {
        'coliseum': coliseum,
        'fortress': fortress,
        'pyramid': pyramid,
    })


login_required(login_url='/accounts/login/')
def publish(request, model_id, id):

    if request.user.subscriber == True:

        if model_id == 'coliseum' :
            portifolio = Coliseum.objects.filter(pk=id)
            user = request.user
            if user == portifolio.first().user:
                unplublish_all_portifolios(request)
                portifolio.update(public=True)
                return redirect(reverse("meus_portifolios"))
            else: return Http404()

        if model_id == 'fortress' :
            portifolio = Fortress.objects.filter(pk=id)
            user = request.user
            if user == portifolio.first().user:
                unplublish_all_portifolios(request)
                portifolio.update(public=True)
                return redirect(reverse("meus_portifolios"))
            else: return Http404()

        if model_id == 'pyramid' :
            portifolio = Pyramid.objects.filter(pk=id)
            user = request.user
            if user == portifolio.first().user:
                unplublish_all_portifolios(request)
                portifolio.update(public=True)
                return redirect(reverse("meus_portifolios"))
            else: return Http404()
    else: return HttpResponse("Você precisa ser um assinante para fazer isso!") 


login_required(login_url='/accounts/login/')
def unpublish(request, model_id, id):

    if model_id == 'coliseum': Coliseum.objects.filter(pk=id, public=True).update(public=False)
    if model_id == 'fortress': Fortress.objects.filter(pk=id, public=True).update(public=False)
    if model_id == 'pyramid' : Pyramid.objects.filter(pk=id, public=True).update(public=False)

    return redirect(reverse("meus_portifolios"))



def my_portifolio(request, username):

    user = User.objects.get(username=username)

    coliseum = Coliseum.objects.filter(user=user, public=True)
    fortress = Fortress.objects.filter(user=user, public=True)
    pyramid  = Pyramid.objects.filter(user=user, public=True)

    if coliseum.exists() : return render(request, 'portifolios/coliseum.html', { 'coliseum': coliseum.first() })
    if fortress.exists() : return render(request, 'portifolios/fortress.html', { 'fortress': fortress.first() })
    if pyramid.exists()  : return render(request, 'portifolios/pyramid.html',  { 'pyramid' : pyramid.first() })

    return HttpResponse("ESTE USUARIO NÃO POSSUI NENHUM PORTIFÓLIO PUBLICADO!")

login_required(login_url='/accounts/login/')
def inicio_adm(request):

    user = request.user

    return render(request, 'pages/inicio.html', { 'user': user })


login_required(login_url='/accounts/login/')
def subscribe(request):
    
    User.objects.filter(id=request.user.id).update(subscriber=True)
    return redirect(reverse('inicio'))

