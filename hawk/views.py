from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import heroImage, Athlete, News, training

######################################################################################################################################################################################################
######################################################################################################################################################################################################
def home(request):
    hero_selection = heroImage.objects.first()
    latest_news = News.objects.all()
    context = {'hero_section': hero_selection,'latest_news': latest_news}
    return render(request,'hawk/home.html', context)


######################################################################################################################################################################################################
######################################################################################################################################################################################################
def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        passwrord1 = request.POST['password1']
        passwrord2 = request.POST['password2']

        if passwrord1 == passwrord2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'E-mail already already exist!')
                return redirect('register')
            else:
                user= User.objects.create_user(username = username, password = passwrord1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                messages.info(request, "user created")
                return redirect('login')

        else:
            messages.info(request, 'Password does not match!')
            return redirect('register')
        return redirect('/')
        
    else:    
        return render(request,'hawk/register.html')


######################################################################################################################################################################################################
######################################################################################################################################################################################################
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
             messages.info(request, 'invalid credentials')
        return redirect('login')
    
    else:   
        return render(request,'hawk/login.html')
    

######################################################################################################################################################################################################
######################################################################################################################################################################################################
def logout(request):
    auth.logout(request)
    return redirect('/')


######################################################################################################################################################################################################
######################################################################################################################################################################################################
def about(request):
    return render(request,'hawk/about.html')


######################################################################################################################################################################################################
######################################################################################################################################################################################################
def ourTeam(request):
    athletes = Athlete.objects.all()
    return render(request, 'hawk/our_team.html', {'athletes': athletes})


######################################################################################################################################################################################################
######################################################################################################################################################################################################
def trainning(request):
    train = training.objects.all ()

    return render(request,'hawk/trainning.html',{'train': train})


######################################################################################################################################################################################################
######################################################################################################################################################################################################
def athlete_detail_view(request, athlete_id):
    athlete = get_object_or_404(Athlete, id=athlete_id)
    return render(request, 'hawk/athlete_detail.html', {'athlete': athlete})


######################################################################################################################################################################################################
######################################################################################################################################################################################################
def member(request):
    return render(request, 'hawk/member.html')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PDFFile
from .forms import PDFUploadForm

@login_required
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.save(commit=False)
            pdf.user = request.user
            pdf.save()
            return redirect('pdf_list')
    else:
        form = PDFUploadForm()
    return render(request, 'hawk/upload_pdf.html', {'form': form})

@login_required
def pdf_list(request):
    pdfs = PDFFile.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'hawk/pdf_list.html', {'pdfs': pdfs})
