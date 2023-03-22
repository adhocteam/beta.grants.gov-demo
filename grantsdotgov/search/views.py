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
        open_opps = s.to_queryset()

        s = OpportunityDocument.search().query('multi_match', query=query, fields=['title', 'description', 'agency_name'])
        s = s.query('range', close_date={'lte': date.today()})
        closed_opps = s.to_queryset()
    else:
        open_opps = Opportunity.objects.none()
        closed_opps = Opportunity.objects.none()

    if request.headers.get('HX-Request') == 'true':
        return render(request, 'search/active.html', {
			'query': query,
            'opportunities': open_opps,
        })
    else:
        return render(request, 'search/search.html', {
			'query': query,
            'open_opps': open_opps,
            'closed_opps': closed_opps,
        })

def details(request, gid):
    ctx = {}
    if query := request.GET.get('q'):
        ctx['query'] = query
    opp = Opportunity.objects.get(grant_id=gid)
    ctx['opportunity'] = opp
    return render(request, 'details.html', ctx)
