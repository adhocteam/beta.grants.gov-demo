from django.shortcuts import render
from .models import Opportunity
from .documents import OpportunityDocument

from datetime import date

def search(request):
    query = request.GET.get('q')
    if query:
        s = OpportunityDocument.search().query('multi_match', query=query, fields=['title', 'description', 'agency_name'])
        s = s.query('range', post_date={'lte': date.today()})
        s = s.query('range', close_date={'gte': date.today()})
        results = s.to_queryset()
    else:
        results = Opportunity.objects.none()
    
    return render(request, 'search/search.html', {'results': results})

def details(request, gid):
    ctx = {}
    if query := request.GET.get('q'):
        ctx['query'] = query
    opp = Opportunity.objects.get(grant_id=gid)
    ctx['opportunity'] = opp
    return render(request, 'details.html', ctx)
