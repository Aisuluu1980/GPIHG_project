from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from webapp.models import Project, News

class IndexView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'



    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update({
            'news_list': News.objects.order_by('-created_at')[0:4]

            # 'groups': StudyGroup.objects.all().order_by('name'),
            # 'disciplines': Discipline.objects.all()
        })
        return context

    def get_queryset(self):
        return Project.objects.order_by('-created_date')[0:6]
