from haber.models import Haber
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    son_haber_liste = Haber.objects.all().order_by('-yay_tarihi')[:5]
    return render_to_response('haber/index.html', {'son_haber_liste': son_haber_liste})

def icerik(request, haber_id):
    p = get_object_or_404(Haber, pk=haber_id)
    return render_to_response('haber/icerik.html', {'haber': p})
