
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contato

# Create your views here.


def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 2)

    page_number = request.GET.get('p')
    contatos = paginator.get_page(page_number)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhes(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })
