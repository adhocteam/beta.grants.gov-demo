from django.shortcuts import render
from .models import Opportunity
from .documents import OpportunityDocument

def search(request):
    query = request.GET.get('q')
    if query:
        s = OpportunityDocument.search().query('multi_match', query=query, fields=['title', 'description', 'agency_name'])
        results = s.to_queryset()
    else:
        results = Opportunity.objects.none()
    
    return render(request, 'search/search.html', {'results': results})

def details(request, id):
    opp = Opportunity.objects.get(id=id)
    return render(request, 'details.html', {'opportunity': opp})
