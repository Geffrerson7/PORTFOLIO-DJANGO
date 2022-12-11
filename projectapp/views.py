from django.shortcuts import redirect

from django.views.generic import TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Project
from .forms import ProjectForm


class ProjectCreate(LoginRequiredMixin, SuccessMessageMixin, FormView):
    model = Project
    template_name = "create.html"
    form_class = ProjectForm

    def form_valid(self, form):
        Project.objects.create(**form.cleaned_data)
        return redirect("create")


class PortfolioView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    extra_context = {"proyectos": Project.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyectos"] = Project.objects.all()
        return context


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "portfolio-details.html"
    context_object_name = "proyecto"
