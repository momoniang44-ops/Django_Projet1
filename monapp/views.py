from django.shortcuts import render

def accueil(request):
    
    context = {
        'titre': 'Bienvenue sur mon site',
        'message': 'Decouvrez mon application Django!'
    }
    return render(request, 'monapp/accueil.html', context)

def a_propos(request):
    
    context = {
        'titre': 'A propos de moi',
        'description': 'Je suis un etudiant passionnee par le developpement web.'
    }
    return render(request, 'monapp/a_propos.html', context)

def contact(request):
    
    context = {
        'titre': 'Contactez-nous',
        'email': 'momoniang44@gmail.com',
        'telephone': '+221 78 405 13 45',
        'adresse': 'alea bi , Dakar, Senegal'
    }
    return render(request, 'monapp/contact.html', context)