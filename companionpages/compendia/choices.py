# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from model_utils.choices import Choices

STATUS = Choices('draft', 'active')

TAG_TYPES = Choices('folksonomic', 'taxonomic')

RESEARCH_FIELDS = Choices(
    ("accounting", _(u"Accounting")),
    ("agricultural_environment_energy_economics", _(u"Agricultural, Environmental, and Energy Economics")),
    ("alternative_investments", _(u"Alternative Investments")),
    ("asset_management", _(u"Asset Management")),
    ("asset_pricing", _(u"Asset Pricing")),
    ("asymptotic_theory", _(u"Asymptotic Theory")),
    ("banking_and_risk_management", _(u"Banking and Risk Management")),
    ("bayesian_analysis", _(u"Bayesian Analysis")),
    ("behavioral_finance", _(u"Behavioral Finance")),
    ("biological_sciences", _(u"Biological Sciences")),
    ("bootstrap_and_montecarlo", _(u"Bootstrap and Monte Carlo")),
    ("chemistry", _(u"Chemistry")),
    ("classification_methods", _(u"Classification Methods")),
    ("cognitive_neuroscience", _(u"Cognitive neuroscience")),
    ("computational_neuroscience", _(u"Computational neuroscience")),
    ("computer_and_information_sciences", _(u"Computer and Information Sciences")),
    ("corporate_finance", _(u"Corporate Finance")),
    ("derivatives", _(u"Derivatives")),
    ("developmental_neuroscience", _(u"Developmental neuroscience")),
    ("development_and_transition_economics", _(u"Development and Transition Economics")),
    ("duration_analysis", _(u"Duration analysis")),
    ("econometric_modeling", _(u"Econometric modeling")),
    ("econometrics", _(u"Econometrics")),
    ("economics", _(u"Economics")),
    ("economic_theory", _(u"Economic Theory")),
    ("energy_and_commodities", _(u"Energy and Commodities")),
    ("engineering", _(u"Engineering")),
    ("experimental_economics", _(u"Experimental Economics")),
    ("experiments", _(u"Experiments")),
    ("finance", _(u"Finance")),
    ("financial_econometrics", _(u"Financial Econometrics")),
    ("financial_econometrics", _(u"Financial Econometrics")),
    ("financial_economics", _(u"Financial Economics")),
    ("financing", _(u"Financing")),
    ("fixed_income", _(u"Fixed Income")),
    ("forecasting", _(u"Forecasting")),
    ("game_theory_and_decision_science", _(u"Game Theory and Decision Science")),
    ("game_theory", _(u"Game Theory")),
    ("general_equilibrium", _(u"General Equilibrium")),
    ("general_management", _(u"General Management")),
    ("geosciences", _(u"Geosciences")),
    ("governance", _(u"Governance")),
    ("health_economics_and_management", _(u"Health Economics and Management")),
    ("household_finance", _(u"Household Finance")),
    ("human_resources_management", _(u"Human Resources Management")),
    ("hypothesis_testing", _(u"Hypothesis Testing")),
    ("industrial_organization", _(u"Industrial Organization")),
    ("information_systems", _(u"Information Systems")),
    ("innovation_and_entrepreneurship", _(u"Innovation and Entrepreneurship")),
    ("insurance_and_actuarial_science", _(u"Insurance and Actuarial Science")),
    ("international_economics", _(u"International Economics")),
    ("international_finance", _(u"International Finance")),
    ("investment", _(u"Investment")),
    ("labor_economics", _(u"Labor Economics")),
    ("law_and_economics", _(u"Law and Economics")),
    ("macroeconomics", _(u"Macroeconomics")),
    ("management", _(u"Management")),
    ("marketing", _(u"Marketing")),
    ("mathematics", _(u"Mathematics")),
    ("medical_research", _(u"Medical Research")),
    ("mergers_and_acquisitions", _(u"Mergers and Acquisitions")),
    ("microeconometrics", _(u"Microeconometrics")),
    ("microeconomics", _(u"Microeconomics")),
    ("microstructure", _(u"Microstructure")),
    ("monetary _conomics", _(u"Monetary Economics")),
    ("neural_networks", _(u"Neural Networks")),
    ("neuroimaging", _(u"Neuroimaging")),
    ("neuroinformatics", _(u"Neuroinformatics")),
    ("neurophysiology", _(u"Neurophysiology")),
    ("neuroscience", _(u"Neuroscience")),
    ("nonlinear_econometrics", _(u"Nonlinear econometrics")),
    ("nonparametric_econometrics", _(u"Nonparametric econometrics")),
    ("operations_research", _(u"Operations Research")),
    ("optimization", _(u"Optimization")),
    ("organizational_behavior", _(u"Organizational Behavior")),
    ("other_computational_sciences", _(u"Other Computational Sciences")),
    ("other", _(u"Other")),
    ("panel_data_models", _(u"Panel data models")),
    ("physics", _(u"Physics")),
    ("public_economics_and_public_choice", _(u"Public Economics and Public Choice")),
    ("qualitative_choice_models", _(u"Qualitative choice models")),
    ("real_estate", _(u"Real Estate")),
    ("real_option", _(u"Real Option")),
    ("regime_switching_models", _(u"Regime switching models")),
    ("simultaneous_equation_methods", _(u"Simultaneous equation methods")),
    ("social_sciences", _(u"Social Sciences")),
    ("spatial_econometrics", _(u"Spatial econometrics")),
    ("statistics", _(u"Statistics")),
    ("strategy", _(u"Strategy")),
    ("systems_neuroscience", _(u"Systems neuroscience")),
    ("technology_and_operations_management", _(u"Technology and Operations Management")),
    ("time_series", _(u"Time series")),
    ("truncated_and_censored_models", _(u"Truncated and Censored Models")),
    ("urban_spatial_regional_economics", _(u"Urban, Spatial, and Regional Economics")),
    ("valuation", _(u"Valuation")),
)


MATERIAL_TYPES = Choices(
    ('code', _(u'Code')),
    ('data', _(u'Data')),
    ('other', _(u'Other')),
)


CONTRIBUTOR_ROLES = Choices(
    ('author', _(u'Author')),
    ('editor', _(u'Editor')),
    ('programmer', _(u'Programmer')),
    # http://schema.datacite.org/meta/kernel-3/metadata.xsd
    # contributorType
    ('contact', _(u'Contact Person')),
    ('datacollector', _(u'Data Collector')),
    ('datamanager', _(u'Data Manager')),
    ('distributor', _(u'Distributor')),
    ('funder', _(u'Funder')),
    ('hosting', _(u'Hosting Institution')),
    ('producer', _(u'Producer')),
    ('projectleader', _(u'Project Leader')),
    ('projectmanager', _(u'Project Manager')),
    ('projectmember', _(u'Project Member')),
    ('registrationagency', _(u'Registration Agency')),
    ('registrationauthority', _(u'Registration Authority')),
    ('relatedperson', _(u'Related Person')),
    ('researcher', _(u'Researcher')),
    ('researchgroup', _(u'Research Group')),
    ('rightsholder', _(u'Rights Holder')),
    ('sponsor', _(u'Sponsor')),
    ('supervisor', _(u'Supervisor')),
    ('workpackageleader', _(u'Work Package Leader')),
    ('other', _(u'Other')),
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


# http://www.openoffice.org/bibliographic/bibtex-defs.html
ENTRY_TYPES = Choices(
    ('article', _(u'Journal or Magazine article')),
    ('book', _(u'Book')),
    ('booklet', _(u'Booklet')),
    ('inbook', _(u'Book chapter or section')),
    ('incollection', _(u'Book collection')),
    ('inproceedings', _(u'Conference proceedings article')),
    ('manual', _(u'Technical Documentation')),
    ('mastersthesis', _(u'Master’s thesis')),
    ('misc', _(u'Misc')),
    ('phdthesis', _(u'PhD thesis')),
    ('proceedings', _(u'Conference proceedings')),
    ('techreport', _(u'Technical Report')),
    ('unpublished', _(u'Unpublished Document')),
    # non-bibtex classifications
    ('published_paper', _(u'Published Paper')),
    ('working_paper', _(u'Working Paper')),
    ('misc_methods_paper', _(u'Methods Paper')),
    ('misc_negative_results', _(u'Negative Results')),
    ('misc_public_tool', _(u'Public Tool')),
)


# http://schema.datacite.org/meta/kernel-3/metadata.xsd
# resourceTypeGeneral
RESOURCE_TYPES = Choices(
    ('audiovisual', _(u'Audiovisual')),
    ('collection', _(u'Collection')),
    ('dataset', _(u'Dataset')),
    ('event', _(u'Event')),
    ('image', _(u'Image')),
    ('interactive', _(u'Interactive Resource')),
    ('model', _(u'Model')),
    ('physical', _(u'Physical Object')),
    ('service', _(u'Service')),
    ('software', _(u'Software')),
    ('sound', _(u'Sound')),
    ('text', _(u'Text')),
    ('workflow', _(u'Workflow')),
    ('other', _(u'Other')),

)


# http://schema.datacite.org/meta/kernel-3/metadata.xsd
# relatedIdentifierType
IDENTIFIERS = Choices(
    ('ark', _(u'Archival Resource Key')),
    ('doi', _(u'Digital Object Identifier')),
    ('ean13', _(u'International Article Number')),
    ('eissn', _(u'Electronic Internation Standard Serial Number')),
    ('handle', _(u'Handle')),
    ('isbn', _(u'International Standard Book Number')),
    ('issn', _(u'Internation Standard Serial Number')),
    ('istc', _(u'International Standard Text Code')),
    ('lissn', _(u'Linking ISSN')),
    ('lsid', _(u'Life Science Identifier')),
    ('pmid', _(u'PubMed Identifier')),
    ('pmcid', _(u'PubMed Centrial Identifier')),  # not included by DataCite
    ('purl', _(u'Persistent Uniform Resource Locator')),
    ('upc', _(u'Universal Product Code')),
    ('url', _(u'Uniform Resource Locator')),
    ('urn', _(u'Uniform Resource Name')),
)
