from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Questions, Activeusers,Profile
from .forms import SignUpForm
import json
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse
@login_required
def save(request):
  if request.method == 'POST':
  	competitor=int(request.POST.get('comptitor'));
  	ques1=int(request.POST.get('ques1'));
  	ques1 = Questions.objects.get(id=ques1)
  	ques2=int(request.POST.get('ques2'));
  	ques2 = Questions.objects.get(id=ques2)
  	ques3=int(request.POST.get('ques3'));
  	ques3 = Questions.objects.get(id=ques3)
  	ques4=int(request.POST.get('ques4'));
  	ques4 = Questions.objects.get(id=ques4)
  	ques5=int(request.POST.get('ques5'));
  	ques5 = Questions.objects.get(id=ques5)
  	ans1=int(request.POST.get('ans1'));
  	ans2=int(request.POST.get('ans2'));
  	ans3=int(request.POST.get('ans3'));
  	ans4=int(request.POST.get('ans4'));
  	ans5=int(request.POST.get('ans5'));
  	try:
  		checkwith =Activeusers.objects.get(id=competitor)
  	except Activeusers.DoesNotExist:
  		checkwith=None
  	if checkwith ==None:
  		print("None")
  		t =Activeusers(user= request.user,qid1=ques1,qid2=ques2,qid3=ques3,qid4=ques4,qid5=ques5,answer1=ans1,answer2=ans2,answer3=ans3,answer4=ans4,answer5=ans5)
  		t.save()
  		return HttpResponse("You will get score when your opponent will finish")
  	elif checkwith.isfinished==2:
  		print("compe get settled")
  		t=Activeusers(user= request.user,qid1=ques1,qid2=ques2,qid3=ques3,qid4=ques4,qid5=ques5,answer1=ans1,answer2=ans2,answer3=ans3,answer4=ans4,answer5=ans5)
  		t.save()
  		return HttpResponse("You will get score when your opponent will finish")
  	else:
  		print("still frre compte")
  		score=0
  		if checkwith.answer1==ans1 and ans1!=0:
  			score+=1
  		if checkwith.answer2==ans2 and ans2!=0:
  			score+=1
  		if checkwith.answer3==ans3 and ans3!=0:
  			score+=1
  		if checkwith.answer4==ans4 and ans4!=0:
  			score+=1
  		if checkwith.answer5==ans5 and ans5!=0:
  			score+=1
  		obj=request.user
  		obj.profile.score+=score
  		obj.save()
  		obj=checkwith.user
  		obj.profile.score+=score
  		obj.save()
  		checkwith.isfinished=2
  		checkwith.score=score
  		checkwith.save()
  		t=Activeusers(user= request.user,qid1=ques1,qid2=ques2,qid3=ques3,qid4=ques4,qid5=ques5,answer1=ans1,answer2=ans2,answer3=ans3,answer4=ans4,answer5=ans5,score=score,isfinished=2)
  		t.save()
  		return HttpResponse("you get "+str(score) + " points from this task")
  return HttpResponse("Try Again , We dont get your data.")






@login_required
def gamepage(request):
	try:
		comp=Activeusers.objects.filter(isfinished=0)[:1]
	except Activeusers.IndexError:
		comp=None
	compe=-1
	if comp:
		comp.isfinished=1
		data = []
		data.append(comp[0].qid1)
		data.append(comp[0].qid2)
		data.append(comp[0].qid3)
		data.append(comp[0].qid4)
		data.append(comp[0].qid5)
		compe=comp[0].id
	else:
		data = Questions.objects.order_by('?')[:5]
	obj=request.user
	totalscore=obj.profile.score 
	context = {'data': data, 'compe':compe, 'totalscore':totalscore}
	return render(request, 'gameapp/playgame.html' , context)



@login_required
def home(request):
	obj=request.user
	totalscore=obj.profile.score 
	context = {'totalscore':totalscore}
	return render(request, 'gameapp/home.html',context )


@login_required
def scorecard(request):
	obj=request.user
	totalscore=obj.profile.score
	data=Activeusers.objects.filter(user=obj).order_by('-id')
	context = {'data':data ,'totalscore':totalscore}
	return render(request, 'gameapp/scorecard.html',context )


def signup(request):
	if request.user.is_authenticated():
		return redirect('home')
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.score = 0
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'gameapp/signup.html', {'form': form})
