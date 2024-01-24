from django.shortcuts import render,redirect
from .models import ToDo
from .forms import ToDoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,UpdateView,DeleteView

class IndexView(ListView):
    model = ToDo
    template_name = "home.html"
    context_object_name = "task"

class DetailTaskView(DetailView):
    model = ToDo
    template_name = "details.html"
    context_object_name = "task_detail"

class UpdateView(UpdateView):
    model = ToDo
    form_class = ToDoForm
    template_name = "update.html"
    success_url = reverse_lazy("ToDoapp:index")

class DeleteView(DeleteView):
    model = ToDo
    template_name = "details.html"
    success_url = reverse_lazy("ToDoapp:index")


def index(request):
    task=ToDo.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        dis=request.POST.get('dis',)
        date=request.POST.get('date',)
        task1=ToDo(name=name,dis=dis,date=date)
        task1.save() 
    return render(request, "home.html",{'task':task})
 
# def delete(request,task_id):
#     task=ToDo.objects.get(id=task_id)
#     if request.method=='POST':
#         task.delete()
#         return redirect('/')
#     return render(request, "details.html")

# def update(request, task_id):
#     task = ToDo.objects.get(id=task_id)
#     form = ToDoForm(request.POST or None, request.FILES, instance=task)
#     if form.is_valid():
#         form.save()
#         print(" button clicked for task ID:", task_id)
#         return redirect('/')
#     return render(request, "update.html",{'form':form,'task':task})
    