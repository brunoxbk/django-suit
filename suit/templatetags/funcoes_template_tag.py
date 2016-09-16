from django import template
# from core.models import Offer

register = template.Library()

@register.simple_tag(takes_context= True)
def imagem_evento_consulta(context, evento_id):
    context['evento_imagem'] = Evento.objects.get(id=evento_id)

    return ''

@register.simple_tag(takes_context= True)
def especificacao_evento_interno(context, objeto):
    todas_especificacao = {}
    for evento in objeto.especificacaoatributo_set.all():
        for especificacao_evento in evento.especificacao.especificacaoatributo_set.all():
            if especificacao_evento == evento:

                if todas_especificacao.has_key(evento.especificacao.get_grupo_display()):
                    todas_especificacao[evento.especificacao.get_grupo_display()][especificacao_evento.especificacao.titulo] = especificacao_evento.valor
                else:
                    todas_especificacao[evento.especificacao.get_grupo_display()] = {especificacao_evento.especificacao.titulo: especificacao_evento.valor}
    context['lista_especificacao'] = todas_especificacao
    return ''


# template tag para exibir somente os campos unicos
@register.simple_tag(takes_context=True)
def campos_unicos(context, objeto):
    lista = []
    campos_unicos = objeto.especificacaoatributo_set.all()
    for campo in campos_unicos:
        lista.append(campo.valor)
    lista = set(lista)
    context['campos_unicos'] = lista
    return ''
