from django.shortcuts import render , redirect
from .forms import TodoForm
# Create your views here.
from .models import TodoModel
from jalali_date import datetime2jalali, date2jalali
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def Todo_view(request):
	if request.user.is_authenticated:
		jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
		tasks = TodoModel.objects.filter(user = request.user , done = False)
		done_tasks = TodoModel.objects.filter(user = request.user , done = True)
	else:
		tasks = None
		done_tasks = None
	form = TodoForm(request.POST or None)
	if form.is_valid():
		task = form.cleaned_data.get('task')
		status = form.cleaned_data.get('status')
		TodoModel.objects.create(user = request.user , task = task , date = timezone.now() , done = False,status = status)
	
	context = {
	'done_tasks' : done_tasks,
	'form' : form ,
	'tasks' : tasks,
	}
	return render(request , 'index.html' , context)

@login_required(login_url='/login')
def checked(request , id):
	try:
		qs = TodoModel.objects.get(id = id)
	except:
		qs = None
	if qs is not None:
		qs.done = True
		qs.save()

	return redirect('/')

@login_required(login_url='/login')
def delete(request , id):
	try:
		qs = TodoModel.objects.get(id = id)
	except:
		qs = None
	if qs is not None:
		qs.delete()

	return redirect('/')

@login_required(login_url='/login')
def undo(request , id):
	try:
		qs = TodoModel.objects.get(id = id)
	except:
		qs = None
	if qs is not None:
		qs.done = False
		qs.save()
	else:
		print('qs is None')
	return redirect('/')

