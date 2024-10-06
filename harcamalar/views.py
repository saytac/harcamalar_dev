from django.shortcuts import render, redirect
from .models import Harcama


def harcama_ekle(request):
    if request.method == 'POST':
        kalem = request.POST.get('kalem')
        odeme_turu = request.POST.get('odeme_turu')
        fiyat = request.POST.get('fiyat')
        not_ = request.POST.get('not_')

        # Boş alan kontrolü
        if not kalem or not odeme_turu or not fiyat or not not_:
            return render(request, 'harcamalar/harcama_form.html', {'error': 'Tüm alanları doldurun!'})

        # Harcama kaydetme
        harcama = Harcama(kalem=kalem, odeme_turu=odeme_turu, fiyat=fiyat, not_=not_)
        harcama.save()
        return redirect('harcama_ekle')

    return render(request, 'harcamalar/harcama_form.html')
