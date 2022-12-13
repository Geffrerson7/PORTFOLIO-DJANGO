from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from django.contrib import messages


class ProjectCreate(LoginRequiredMixin, FormView):
    model = Project
    template_name = "create.html"
    form_class = ProjectForm

    def form_valid(self, form):
        Project.objects.create(**form.cleaned_data)
        messages.success(self.request, "Project created")
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


@login_required
def deleteProject(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("index")


def rick_y_morty_View(request):
    return render(request, "portfolio-rick.html")


def fin_de_unidad_1_View(request):
    return render(request, "portfolio-fin-de-unidad-1.html")
