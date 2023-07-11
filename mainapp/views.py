from typing import Any, Dict
from django.views.generic import TemplateView
from datetime import datetime


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["news_title"] = "First test header"
        context["news_preview"] = "Preliminary first news description"

        context['range'] = range(5)
        context['datetime_obj'] = datetime.now()

        return context

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/docsite.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
