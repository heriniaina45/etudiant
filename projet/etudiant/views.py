from django.shortcuts import render, HttpResponseRedirect
from .forms import Student  
from .models import User

# cette fonction permet d'ajouter et d'afficher les informations
def affiche(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']  
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password'] 
            reg = User(name = nm, email = em, password = pw)
            reg.save()
            fm = Student()
    else:
        fm = Student()
    stud = User.objects.all()
    return render(request, 'etudiant/afficher.html', {'form':fm, 'fm': stud })

# cette fonctoin permet de modifier les information
def modifier(request, id):
    if request.method == 'POST':
        su = User.objects.get(pk=id)
        fm = Student(request.POST, instance=su)
        if fm.is_valid():
            fm.save()
    else:
        su = User.objects.get(pk=id)
    fm = Student(instance=su)
    return render(request, 'etudiant/modifier.html', {'form':fm})


 # cette fonction permet de supprimer les données 

def delete(request, id):
    if request.method == 'POST':
        su = User.objects.get(pk=id)
        su.delete()
        return HttpResponseRedirect('/')