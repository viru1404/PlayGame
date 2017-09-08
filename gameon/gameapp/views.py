from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Questions, Activeusers,Profile,checkfun
from .forms import SignUpForm
import json
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Q
import random
print(random.randint(0,9))

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
  		checkwith.isfinished+=1
  		checkwith.save()
  		score=0
  		t=Activeusers(user= request.user,qid1=ques1,qid2=ques2,qid3=ques3,qid4=ques4,qid5=ques5,answer1=ans1,answer2=ans2,answer3=ans3,answer4=ans4,answer5=ans5,score=score,isfinished=2)
  		t.save()
  		ee=checkfun(id1=checkwith.id,id2=t.id)
  		ee.save()
  		if checkwith.isfinished==2:
  			qw=checkfun.objects.filter(id1=checkwith.id)
  			score=0
  			z1=1
  			z2=1
  			z3=1
  			z4=1
  			z5=1
  			for ii in qw:
  				qa=Activeusers.objects.get(id=ii.id2)
  				if qa.answer1 != checkwith.answer1 or  checkwith.answer1==0 or  qa.answer1==0:
  					z1=0
  				if qa.answer2 != checkwith.answer2 or  checkwith.answer2==0 or  qa.answer2==0:
  					z2=0
  				if qa.answer3 != checkwith.answer3 or  checkwith.answer3==0 or  qa.answer3==0:
  					z3=0
  				if qa.answer4 != checkwith.answer4 or  checkwith.answer4==0 or  qa.answer4==0:
  					z4=0
  				if qa.answer5 != checkwith.answer5 or  checkwith.answer5==0 or  qa.answer5==0:
  					z5=0

  			score=z1+z2+z3+z4+z5
  			for ii in qw:
  				qa=Activeusers.objects.get(id=ii.id2)
  				qa.score=score
  				qa.save()
  			return HttpResponse("you get "+str(score) + " points from this task")
  		else:
  			return HttpResponse("you will get  points from this task is completed by other users")
  return HttpResponse("Try Again , We dont get your data.")






@login_required
def gamepage(request):
	try:
		comp=Activeusers.objects.filter(~Q(isfinished=2) )[:1]
	except Activeusers.IndexError:
		comp=None
	compe=-1
	if comp:
		#wsx=timer(id1=comp[0],id2=)
		print(comp[0].isfinished)
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
