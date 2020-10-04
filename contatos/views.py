
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contato

# Create your views here.


def index(request):
    contato_list = Contato.objects.order_by('nome').filter(
        mostrar=True
    )
    paginator = Paginator(contato_list, 10)
    page = request.GET.get('page')

    try:
        contatos = paginator.page(page)
    except PageNotAnInteger:
        contatos = paginator.page(1)

    except EmptyPage:
        contatos = paginator.page(paginator.num_pages)

    return render(request, 'contatos/index.html', {
        'contatos': contatos,
        'page': page,
    })


def detalhes(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })
