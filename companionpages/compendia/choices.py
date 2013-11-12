from django.utils.translation import ugettext_lazy as _
from model_utils.choices import Choices

STATUS = Choices('draft', 'active')

RESEARCH_FIELDS = Choices(
    ("accounting", _("Accounting")),
    ("agricultural_environment_energy_economics", _("Agricultural, Environmental, and Energy Economics")),
    ("alternative_investments", _("Alternative Investments")),
    ("asset_management", _("Asset Management")),
    ("asset_pricing", _("Asset Pricing")),
    ("asymptotic_theory", _("Asymptotic Theory")),
    ("banking_and_risk_management", _("Banking and Risk Management")),
    ("bayesian_analysis", _("Bayesian Analysis")),
    ("behavioral_finance", _("Behavioral Finance")),
    ("biological_sciences", _("Biological Sciences")),
    ("bootstrap_and_montecarlo", _("Bootstrap and Monte Carlo")),
    ("chemistry", _("Chemistry")),
    ("classification_methods", _("Classification Methods")),
    ("cognitive_neuroscience", _("Cognitive neuroscience")),
    ("computational_neuroscience", _("Computational neuroscience")),
    ("computer_and_information_sciences", _("Computer and Information Sciences")),
    ("corporate_finance", _("Corporate Finance")),
    ("derivatives", _("Derivatives")),
    ("developmental_neuroscience", _("Developmental neuroscience")),
    ("development_and_transition_economics", _("Development and Transition Economics")),
    ("duration_analysis", _("Duration analysis")),
    ("econometric_modeling", _("Econometric modeling")),
    ("econometrics", _("Econometrics")),
    ("economics", _("Economics")),
    ("economic_theory", _("Economic Theory")),
    ("energy_and_commodities", _("Energy and Commodities")),
    ("engineering", _("Engineering")),
    ("experimental_economics", _("Experimental Economics")),
    ("experiments", _("Experiments")),
    ("finance", _("Finance")),
    ("financial_econometrics", _("Financial Econometrics")),
    ("financial_econometrics", _("Financial Econometrics")),
    ("financial_economics", _("Financial Economics")),
    ("financing", _("Financing")),
    ("fixed_income", _("Fixed Income")),
    ("forecasting", _("Forecasting")),
    ("game_theory_and_decision_science", _("Game Theory and Decision Science")),
    ("game_theory", _("Game Theory")),
    ("general_equilibrium", _("General Equilibrium")),
    ("general_management", _("General Management")),
    ("geosciences", _("Geosciences")),
    ("governance", _("Governance")),
    ("health_economics_and_management", _("Health Economics and Management")),
    ("household_finance", _("Household Finance")),
    ("human_resources_management", _("Human Resources Management")),
    ("hypothesis_testing", _("Hypothesis Testing")),
    ("industrial_organization", _("Industrial Organization")),
    ("information_systems", _("Information Systems")),
    ("innovation_and_entrepreneurship", _("Innovation and Entrepreneurship")),
    ("insurance_and_actuarial_science", _("Insurance and Actuarial Science")),
    ("international_economics", _("International Economics")),
    ("international_finance", _("International Finance")),
    ("investment", _("Investment")),
    ("labor_economics", _("Labor Economics")),
    ("law_and_economics", _("Law and Economics")),
    ("macroeconomics", _("Macroeconomics")),
    ("management", _("Management")),
    ("marketing", _("Marketing")),
    ("mathematics", _("Mathematics")),
    ("medical_research", _("Medical Research")),
    ("mergers_and_acquisitions", _("Mergers and Acquisitions")),
    ("microeconometrics", _("Microeconometrics")),
    ("microeconomics", _("Microeconomics")),
    ("microstructure", _("Microstructure")),
    ("monetary _conomics", _("Monetary Economics")),
    ("neural_networks", _("Neural Networks")),
    ("neuroimaging", _("Neuroimaging")),
    ("neuroinformatics", _("Neuroinformatics")),
    ("neurophysiology", _("Neurophysiology")),
    ("neuroscience", _("Neuroscience")),
    ("nonlinear_econometrics", _("Nonlinear econometrics")),
    ("nonparametric_econometrics", _("Nonparametric econometrics")),
    ("operations_research", _("Operations Research")),
    ("optimization", _("Optimization")),
    ("organizational_behavior", _("Organizational Behavior")),
    ("other_computational_sciences", _("Other Computational Sciences")),
    ("other", _("Other")),
    ("panel_data_models", _("Panel data models")),
    ("physics", _("Physics")),
    ("public_economics_and_public_choice", _("Public Economics and Public Choice")),
    ("qualitative_choice_models", _("Qualitative choice models")),
    ("real_estate", _("Real Estate")),
    ("real_estate", _("Real Estate")),
    ("real_option", _("Real Option")),
    ("regime_switching_models", _("Regime switching models")),
    ("simultaneous_equation_methods", _("Simultaneous equation methods")),
    ("social_sciences", _("Social Sciences")),
    ("spatial_econometrics", _("Spatial econometrics")),
    ("statistics", _("Statistics")),
    ("strategy", _("Strategy")),
    ("systems_neuroscience", _("Systems neuroscience")),
    ("technology_and_operations_management", _("Technology and Operations Management")),
    ("time_series"),
    ("truncated_and_censored_models", _("Truncated and Censored Models")),
    ("urban_spatial_regional_economics", _("Urban, Spatial, and Regional Economics")),
    ("valuation", _("Valuation")),
)


PAPER_TYPES = Choices(
    ('published_paper', _('Published Paper')),
    ('working_paper', _('Working Paper')),
    ('methods_paper', _('Methods Paper')),
    ('negative_results', _('Negative Results')),
    ('public_tool', _('Public Tool')),
    ("other", _("Other")),
)


MATERIAL_TYPES = Choices(
    ('code', _('Code')),
    ('data', _('Data')),
    ('other', _('Other')),
)


CONTRIBUTOR_ROLES = Choices(
    ('author', _('Author')),
    ('editor', _('Editor')),
    ('programmer', _('Programmer')),
)


# TODO make representation of the licenses chosen for content by using rdf schema and use that rather than Choices
# http://creativecommons.org/ns#
CONTENT_LICENSES = Choices(
    ('CC0', _(u'Public Domain Mark')),
    ('other', _(u'Other (must be approved by ResearchCompendia'))
)


CODE_LICENSES = Choices(
    ('MIT', _(u'MIT License')),
    ('other', _(u'Other (must be approved by ResearchCompendia'))
)
