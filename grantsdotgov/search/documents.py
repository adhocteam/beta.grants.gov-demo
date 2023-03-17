from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from .models import Opportunity

opp_index = Index('opportunities')
opp_index.settings(number_of_shards=1, number_of_replicas=0)

@registry.register_document
class OpportunityDocument(Document):
    class Django:
        model = Opportunity
        fields = [
            'title',
            'description',
            'agency_name',
            'post_date',
            'close_date',
            'award_ceiling',
            'award_floor',
        ]

    class Index:
        name = 'opportunities'
        settings = opp_index._settings

