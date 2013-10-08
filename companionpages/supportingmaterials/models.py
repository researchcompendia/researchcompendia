from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel

from members.models import Member

RESEARCH_FIELDS = Choices(
    ("biological_sciences", _("Biological Sciences")),
    ("neuroscience", _("Neuroscience")),
    ("cognitive_neuroscience", _("Cognitive neuroscience")),
    ("computational_neuroscience", _("Computational neuroscience")),
    ("developmental_neuroscience", _("Developmental neuroscience")),
    ("neuroimaging", _("Neuroimaging")),
    ("neuroinformatics", _("Neuroinformatics")),
    ("neurophysiology", _("Neurophysiology")),
    ("systems_neuroscience", _("Systems neuroscience")),
    ("chemistry", _("Chemistry")),
    ("computer_and_information_sciences", _("Computer and Information Sciences")),
    ("engineering", _("Engineering")),
    ("geosciences", _("Geosciences")),
    ("mathematics", _("Mathematics")),
    ("medical_research", _("Medical Research")),
    ("other_computational_sciences", _("Other Computational Sciences")),
    ("physics", _("Physics")),
    ("social_sciences", _("Social Sciences")),
    ("econometrics", _("Econometrics")),
    ("asymptotic_theory", _("Asymptotic Theory")),
    ("bayesian_analysis", _("Bayesian Analysis")),
    ("bootstrap_and_montecarlo", _("Bootstrap and Monte Carlo")),
    ("classification_methods", _("Classification Methods")),
    ("duration_analysis", _("Duration analysis")),
    ("econometric_modeling", _("Econometric modeling")),
    ("financial_econometrics", _("Financial Econometrics")),
    ("forecasting", _("Forecasting")),
    ("hypothesis_testing", _("Hypothesis Testing")),
    ("microeconometrics", _("Microeconometrics")),
    ("neural_networks", _("Neural Networks")),
    ("nonlinear_econometrics", _("Nonlinear econometrics")),
    ("nonparametric_econometrics", _("Nonparametric econometrics")),
    ("panel_data_models", _("Panel data models")),
    ("qualitative_choice_models", _("Qualitative choice models")),
    ("regime_switching_models", _("Regime switching models")),
    ("simultaneous_equation_methods", _("Simultaneous equation methods")),
    ("spatial_econometrics", _("Spatial econometrics")),
    ("time_series"),
    ("truncated_and_censored_models", _("Truncated and Censored Models")),
    ("economics", _("Economics")),
    ("agricultural_environment_energy_economics", _("Agricultural, Environmental, and Energy Economics")),
    ("development_and_transition_economics", _("Development and Transition Economics")),
    ("economic_theory", _("Economic Theory")),
    ("experimental_economics", _("Experimental Economics")),
    ("experiments", _("Experiments")),
    ("financial_economics", _("Financial Economics")),
    ("game_theory", _("Game Theory")),
    ("game_theory_and_decision_science", _("Game Theory and Decision Science")),
    ("general_equilibrium", _("General Equilibrium")),
    ("health_economics_and_management", _("Health Economics and Management")),
    ("industrial_organization", _("Industrial Organization")),
    ("innovation_and_entrepreneurship", _("Innovation and Entrepreneurship")),
    ("international_economics", _("International Economics")),
    ("labor_economics", _("Labor Economics")),
    ("law_and_economics", _("Law and Economics")),
    ("macroeconomics", _("Macroeconomics")),
    ("microeconomics", _("Microeconomics")),
    ("monetary _conomics", _("Monetary Economics")),
    ("optimization", _("Optimization")),
    ("public_economics_and_public_choice", _("Public Economics and Public Choice")),
    ("real_estate", _("Real Estate")),
    ("urban_spatial_regional_economics", _("Urban, Spatial, and Regional Economics")),
    ("finance", _("Finance")),
    ("alternative_investments", _("Alternative Investments")),
    ("asset_management", _("Asset Management")),
    ("asset_pricing", _("Asset Pricing")),
    ("banking_and_risk_management", _("Banking and Risk Management")),
    ("behavioral_finance", _("Behavioral Finance")),
    ("corporate_finance", _("Corporate Finance")),
    ("derivatives", _("Derivatives")),
    ("energy_and_commodities", _("Energy and Commodities")),
    ("financial_econometrics", _("Financial Econometrics")),
    ("financing", _("Financing")),
    ("fixed_income", _("Fixed Income")),
    ("governance", _("Governance")),
    ("household_finance", _("Household Finance")),
    ("international_finance", _("International Finance")),
    ("investment", _("Investment")),
    ("mergers_and_acquisitions", _("Mergers and Acquisitions")),
    ("microstructure", _("Microstructure")),
    ("real_estate", _("Real Estate")),
    ("real_option", _("Real Option")),
    ("valuation", _("Valuation")),
    ("management", _("Management")),
    ("accounting", _("Accounting")),
    ("general_management", _("General Management")),
    ("human_resources_management", _("Human Resources Management")),
    ("information_systems", _("Information Systems")),
    ("insurance_and_actuarial_science", _("Insurance and Actuarial Science")),
    ("marketing", _("Marketing")),
    ("operations_research", _("Operations Research")),
    ("organizational_behavior", _("Organizational Behavior")),
    ("strategy", _("Strategy")),
    ("technology_and_operations_management", _("Technology and Operations Management")),
    ("statistics", _("Statistics")),
    ("other", _("Other")),
)

PAPER_TYPE = Choices(
    ('published_paper', _('Published Paper')),
    ('working_paper', _('Working Paper')),
    ('methods_paper', _('Methods Paper')),
    ('negative_results', _('Negative Results')),
    ('public_tool', _('Public Tool')),
    ("other", _("Other")),
)


class Collaborator(TimeStampedModel):
    member = models.ManyToManyField(
        Member,
        null=True,
        blank=True,
        help_text=_(u'Member account for the collaborator'))
    name = models.CharField(max_length=200, help_text=_(u'The name of a collaborator'))
    coder = models.BooleanField()
    author = models.BooleanField()
    affiliation = models.CharField(max_length=200, help_text=_(u'Collaborator affiliation'), blank=True)
    country = models.CharField(max_length=200, help_text=_(u'Collaborator country'), blank=True)
    author_order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta(object):
        ordering = ['author_order', 'name']
        verbose_name = _(u'collaborator')
        verbose_name_plural = _(u'collaborators')


class Article(StatusModel, TimeStampedModel):
    site_owner = models.ForeignKey(Member, help_text=_(u'The member who has ownership of the page'), blank=True, null=True)
    collaborators = models.ManyToManyField(Collaborator, blank=True, null=True)
    STATUS = Choices('draft', 'active')
    title = models.CharField(max_length=500, verbose_name=_(u'Article title'))
    abstract = models.TextField(max_length=5000)
    journal = models.CharField(blank=True, max_length=500, verbose_name=_(u'Journal Name'))
    article_url = models.URLField(blank=True, max_length=2000, help_text=_(u'external URL to the paper.'))
    storage_url  = models.URLField(blank=True, max_length=2000, help_text=_(u'URL where we have stored the paper.'))
    legacy_id = models.IntegerField(blank=True, null=True)
    doi = models.CharField(max_length=2000, help_text=_(u'The DOI for the article'), blank=True)
    primary_research_field = models.CharField(max_length=300, choices=RESEARCH_FIELDS,
                                              verbose_name="Primary research field", blank=True)
    secondary_research_field = models.CharField(max_length=300, choices=RESEARCH_FIELDS,
                                                verbose_name="Secondary research field", blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('researchcompendium', args=(self.id))

    class Meta(object):
        ordering = ['title']
        verbose_name = _(u'compendium')
        verbose_name_plural = _(u'compendia')


class SupportingMaterial(StatusModel, TimeStampedModel):
    STATUS = Choices('draft', 'active')
    article = models.ForeignKey(Article, null=True, blank=True)
    name = models.CharField(max_length=500)
    archive_file = models.FileField(upload_to='materials', blank=True)
    explanatory_text = models.TextField(max_length=5000, blank=True)
    materials_url = models.URLField(blank=True,
                                    max_length=2000,
                                    help_text=_(u'URL to the supporting material. For example, '
                                                u'if this is source code, this would be a url '
                                                u'to to the code repository.'))
    storage_url  = models.URLField(blank=True,
                                   max_length=2000,
                                   help_text=_(u'internal URL where we have stored this material.'))

    def __unicode__(self):
        return self.name
