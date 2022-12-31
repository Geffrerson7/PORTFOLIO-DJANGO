from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class ProjectCreate(LoginRequiredMixin, FormView):
    model = Project
    template_name = "create.html"
    form_class = ProjectForm

    def form_valid(self, form):
        Project.objects.create(**form.cleaned_data)
        messages.success(self.request, "Project created successfully")
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
    context_object_name = "proyecto"

class ProjectUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Project
    fields = ["title", "description", "url_image", "url_github", "tags"]
    success_message="Project updated successfully"
    def get_success_url(self):
        return reverse_lazy('update', kwargs={'pk': self.object.pk})

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url ="/"

def rick_y_morty_View(request):
    return render(request, "portfolio-rick.html")

def fin_de_unidad_1_View(request):
    return render(request, "portfolio-fin-de-unidad-1.html")

def apiPayments(request):
    return render(request,"portfolio-apiPayments.html")