from django.shortcuts import render, get_object_or_404
from .models import Project

def portfolio_view(request):
    projects = Project.objects.prefetch_related("images")  # Предзагружаем изображения
    return render(request, 'projects/portfolio.html', {'projects': projects})

def project_detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})
  

