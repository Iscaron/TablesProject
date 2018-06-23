from django.views.generic import FormView

class AjaxFormMixin(FormView):

    #template_name = 'form_ajax.html'  # Поскольку существенная часть форм в проекте рендерятся одним шаблоном, то зачем его везде указывать=) Впрочем, эта строка несущественна.

    def form_valid(self, form):
        form.save()
        return HttpResponse('OK')

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        return HttpResponseBadRequest(json.dumps(errors_dict))