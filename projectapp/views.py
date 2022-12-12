from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project
from .forms import ProjectForm
from django.contrib import messages


class ProjectCreate(LoginRequiredMixin, FormView):
    model = Project
    template_name = "create.html"
    form_class = ProjectForm

    def form_valid(self, form):
        if form.is_valid():
            Project.objects.create(**form.cleaned_data)
            messages.success(self.request, "Project created")
        else:
            messages.error(self.request, "Error creating project")
        return redirect("create")


class PortfolioView(TemplateView):
    template_name = "index.html"
    extra_context = {"proyectos": Project.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyectos"] = Project.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio-details.html"
    context_object_name = "proyecto"


def rick_y_morty_View(request):
    return render(request, "portfolio-rick.html")


def fin_de_unidad_1_View(request):
    return render(request, "portfolio-fin-de-unidad-1.html")
