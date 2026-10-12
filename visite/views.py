from django.shortcuts import render, redirect, get_object_or_404
from .models import Visit
from django.utils import timezone
from django.db.models import Q

def dashboard(request):
    query = request.GET.get('search', '')
    visits = Visit.objects.all().order_by('-arrival_time')
    if query:
        visits = visits.filter(Q(visitor_name__icontains=query) | Q(company__icontains=query))

    stats = {
        'total': Visit.objects.count(),
        'pending': Visit.objects.filter(status='PENDING').count(),
        'ongoing': Visit.objects.filter(status='ONGOING').count(),
        'completed': Visit.objects.filter(status='COMPLETED').count(),
    }
    return render(request, 'visite/dashboard.html', {'visits': visits, 'stats': stats, 'search': query})

def add_visit(request):
    if request.method == "POST":
        # On récupère l'heure du formulaire
        form_arrival = request.POST.get('arrival_time')
        
        Visit.objects.create(
            visitor_name=request.POST.get('visitor_name'),
            company=request.POST.get('company'),
            phone_number=request.POST.get('phone_number'),
            host_person=request.POST.get('host_person'),
            purpose=request.POST.get('purpose'),
            status=request.POST.get('status', 'PENDING'),
            signature=request.POST.get('signature'),
            arrival_time=form_arrival if form_arrival else timezone.now()
        )
    return redirect('dashboard')

def start_visit(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    if visit.status == 'PENDING':
        visit.status = 'ONGOING'
        # Optionnel : décommente la ligne suivante si tu veux que l'heure 
        # se mette à jour au moment où il entre réellement
        # visit.arrival_time = timezone.now()
        visit.save()
    return redirect('dashboard')

def checkout_visit(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    if request.method == "POST":
        selected_time = request.POST.get('departure_time')
        # On utilise l'heure choisie dans la modale, sinon l'heure actuelle
        visit.departure_time = selected_time if selected_time else timezone.now()
        visit.status = 'COMPLETED'
        visit.save()
    return redirect('dashboard')

def delete_visit(request, pk):
    get_object_or_404(Visit, pk=pk).delete()
    return redirect('dashboard')

def liste_visiteurs(request):
    query = request.GET.get('search', '')
    visiteurs = Visit.objects.all().order_by('visitor_name')
    if query:
        visiteurs = visiteurs.filter(Q(visitor_name__icontains=query) | Q(company__icontains=query))
    return render(request, 'visite/visiteurs.html', {'visiteurs': visiteurs, 'search': query})

def historique(request):
    history = Visit.objects.filter(status='COMPLETED').order_by('-departure_time')
    return render(request, 'visite/historique.html', {'history': history})