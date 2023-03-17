from django.db import models

class Opportunity(models.Model):
    grant_id = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    external_id = models.CharField(max_length=40, blank=True, null=True) # XML: OpportunityNumber
    category = models.CharField(max_length=20, blank=True, null=True)
    opp_category_explanation = models.CharField(max_length=255, blank=True, null=True)
    category_explanation = models.TextField(blank=True, null=True)
    # FundingInstrumentType              []string
    # CategoryOfFundingActivity          []string
    # CFDANumbers                        []string
    # EligibleApplicants                 []string
    eligibility_info = models.TextField(blank=True, null=True)
    agency_code = models.CharField(max_length=255, blank=True, null=True)
    agency_name = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    close_date_explanation = models.TextField(blank=True, null=True)
    last_updated_date = models.DateField(blank=True, null=True)
    award_ceiling = models.IntegerField(blank=True, null=True)
    award_floor = models.IntegerField(blank=True, null=True)
    est_total_funding = models.IntegerField(blank=True, null=True)
    exp_num_awards = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    cost_sharing_or_match_req = models.CharField(max_length=3, blank=True, null=True)
    archive_date = models.DateField(blank=True, null=True)
    addl_info_url = models.URLField(blank=True, null=True)
    addl_info_text = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_description = models.CharField(max_length=102, blank=True, null=True)
    contact_text = models.TextField(blank=True, null=True)

    def __repr__(self):
        return self.title
