from .models import Coliseum, Fortress, Pyramid, User

def unplublish_all_portifolios(request):
    user = request.user
    Coliseum.objects.filter(user=user, public=True).update(public=False)
    Fortress.objects.filter(user=user, public=True).update(public=False)
    Pyramid.objects.filter(user=user, public=True).update(public=False)