from django.shortcuts import render, get_object_or_404
from .models import Project, DocumentGroup, Document, Sponsor
import os

def portfolio_view(request):
    projects = Project.objects.prefetch_related("images")  # Предзагружаем изображения
    sponsors = Sponsor.objects.all()  
    return render(request, 'projects/portfolio.html', {'projects': projects, 'sponsors': sponsors})

def project_detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})

def documents_view(request):  
    document_groups = DocumentGroup.objects.prefetch_related("documents").all()

    # Добавляем `short_name` в каждый документ
    for group in document_groups:
        for doc in group.documents.all():
            doc.short_name = os.path.basename(doc.file.name)

    return render(request, "documents.html", {"document_groups": document_groups})
  

