from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models, forms

class ParserLalafoListView(generic.ListView):
    model = models.LalafoProducts
    template_name = 'parser/lalafo_parser_list.html'

    def get_queryset(self):
        return models.LalafoProducts.objects.all()

class ParserFormView(generic.FormView):
    template_name = 'parser/start_parse.html'
    form_class = forms.ParserProductForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Nice job! 👌😀')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)