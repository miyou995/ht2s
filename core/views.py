from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView , DetailView, CreateView
from django.views.generic.edit import FormView
from django.http import JsonResponse
from business import translation
from django.contrib import messages
from config import settings 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from business.models import  Slide
from core.models import Service, Contact, Quote, Hiring,About, Company, Solution
from core.forms import ContactForm, QuoteForm, HiringForm
from django.shortcuts import redirect
# from django.utils.translation import LANGUAGE_SESSION_KEY
from django.shortcuts import redirect
from django.utils.translation import activate
from django.conf import settings
from django.shortcuts import redirect
from django.utils.translation import activate
from django.conf import settings
from django.views.decorators.cache import never_cache


############### INDEX ###############
class IndexView(TemplateView):
    def get_template_names(self):
        # if self.request.LANGUAGE_CODE == 'ar':
        #     return ['rtl/index.html']
        # else:
        return ['index.html']
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["services_one"] =  Service.objects.filter(company__order=1)
        print('cccccc', Service.objects.filter(company__order=1))
        context["services_two"] =  Service.objects.filter(company__order=2)
        context["slides"]   = Slide.objects.filter(actif=True)
        first_company = Company.objects.first()
        context["company_first"]   = Company.objects.first()
        context["company_second"]   = None
        if first_company:
            context["company_second"]   = Company.objects.exclude(id=first_company.id).last()
        return context

############### ABOUT ###############
class AboutView(TemplateView):
    def get_template_names(self):
        # if self.request.LANGUAGE_CODE == 'ar':
        #     return ['rtl/about.html']
        # else:
        return ['about.html']
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["abouts"] =About.objects.all()
        return context

############### SERVICES ###############
##### LIST
class ServiceView(ListView):
    def get_template_names(self):
        # if self.request.LANGUAGE_CODE == 'ar':
        #     return ['rtl/services.html']
        # else:
        return ['services.html']
    model = Service
    context_object_name ="services"
##### DETAIL

############### SOLTUIONS ###############
##### LIST
class SolutionsListView(ListView):
    def get_template_names(self):
        # if self.request.LANGUAGE_CODE == 'ar':
        #     return ['rtl/services.html']
        # else:
        return ['solutions.html']
    model = Solution
    context_object_name ="solutions"
##### DETAIL


class SolutionsDetailView(DetailView):
    model = Solution
    template_name = "solution-detail.html"
    context_object_name ="solution"


class ServiceDetail(DetailView):
    model = Service
    def get_template_names(self):
        # if self.request.LANGUAGE_CODE == 'ar':
        #     return ['rtl/services_detail.html']
        # else:
        return ['services_detail.html']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] =Service.objects.all()
        context["abouts"] =About.objects.all()
        return context

############### CONTACT ###############
class ContactView(SuccessMessageMixin, FormView):
    def get_template_names(self):
        # if self.request.LANGUAGE_CODE == 'ar':
        #     return ['rtl/contact.html']
        # else:
        return ['contact.html']
    form_class= ContactForm
    model = Contact 
    success_message = "We received your message, you will be contacted you soon."
    success_url = reverse_lazy('core:contact')
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        contact_form = ContactForm
        context['form'] = contact_form  
        context["services"] = Service.objects.all()
        return context
    def form_valid(self, form):
        if form.is_valid() :
            self.object = form.save()
            message = _("We received your message, you will be contacted soon.")
            messages.success(self.request, str(message))
        else:
            message = _("Error occures when submitting the message, please check the required fields.")
            messages.error(self.request, str(message))
        return HttpResponseRedirect(self.get_success_url())
    
############### QUOTE ###############
class QuoteoView(SuccessMessageMixin, CreateView):
    def get_template_names(self):
        # if self.request.LANGUAGE_CODE == 'ar':
        #     return ['rtl/quote.html']
        # else:
        return ['quote.html']
    form_class= QuoteForm
    model = Quote 
    success_message = "We received your message, you will be contacted you soon."
    success_url = reverse_lazy('business:quote')
    def get_context_data(self, **kwargs):
        context = super(QuoteoView, self).get_context_data(**kwargs)
        quote_form = QuoteForm
        context['form'] = quote_form  
        context["services"] =Service.objects.all()
        return context
    def form_valid(self, form):
        if form.is_valid() :
            self.object = form.save()
            message = _("We received your message, you will be contacted soon.")
            messages.success(self.request, str(message))
        else:
            message = _("Error occures when submitting the message, please check the required fields.")
            messages.error(self.request, str(message))
        return HttpResponse(status=204) 
    
############### HIRING ###############
class RecruitingView(SuccessMessageMixin, CreateView):
    def get_template_names(self):
        # if self.request.LANGUAGE_CODE == 'ar':
        #     return ['rtl/hiring.html']
        # else:
        return ['hiring.html']
    form_class= HiringForm
    model = Hiring 
    success_message = "We received your message, you will be contacted you soon." 
    success_url = reverse_lazy('core:hiring')
    def get_context_data(self, **kwargs):
        context = super(RecruitingView, self).get_context_data(**kwargs)
        hiring_form = HiringForm
        context['form'] = hiring_form  
        return context
    def form_valid(self, form):
        if form.is_valid() :
            self.object = form.save()
            message = _("We received your message, you will be contacted soon.")
            messages.success(self.request, str(message))
        else:
            message = _("Error occures when submitting the message, please check the required fields.")
            messages.error(self.request, str(message))
        return HttpResponse(status=204) 



from django.shortcuts import render

# def contact(request, language):
#     template_name = f'contact_{language}.html'
#     return render(request, template_name)

# def hiring(request, language):
#     template_name = f'hiring_{language}.html'
#     return render(request, template_name)
# def index(request, language):
#     template_name = f'index_{language}.html'
#     return render(request, template_name)
# def about(request, language):
#     template_name = f'about_{language}.html'
#     return render(request, template_name)
# def services(request, language):
#     template_name = f'services_{language}.html'
#     return render(request, template_name)
# @never_cache
# def switch_language(request):
#     if request.method == 'POST':
#         selected_language = request.POST.get('language')
#         print(f"Selected Language: {selected_language}")
#         request.session['language'] = selected_language
#     return redirect(request.META.get('HTTP_REFERER'))






