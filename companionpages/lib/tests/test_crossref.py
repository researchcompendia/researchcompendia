from django.test import TestCase

from lib import crossref

#  flake8: noqa

class DoiTests(TestCase):

    def test_nonbarfing_emptiness(self):
        r = crossref.parse_crossref_output('')
        assert r['msg'] == 'crossref error', 'missing query should cause a crossref error'
        assert 'compendia' not in r, 'empty reply should have an empty compendia'

    def get_sample_unixsd(self):
        return """
<?xml version="1.0" encoding="UTF-8"?>
<crossref_result xmlns="http://www.crossref.org/qrschema/3.0" version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.crossref.org/qrschema/3.0 http://www.crossref.org/schema/queryResultSchema/crossref_query_output3.0.xsd">
  <query_result>
    <head>
      <doi_batch_id>none</doi_batch_id>
    </head>
    <body>
      <query status="resolved">
        <doi type="journal_article">10.1006/jmbi.2000.4282</doi>
        <crm-item name="publisher-name" type="string">Elsevier BV</crm-item>
        <crm-item name="prefix-name" type="string">Elsevier BV</crm-item>
        <crm-item name="citation-id" type="number">327027</crm-item>
        <crm-item name="journal-id" type="number">505</crm-item>
        <crm-item name="deposit-timestamp" type="number">20110807090000000</crm-item>
        <crm-item name="owner-prefix" type="string">10.1006</crm-item>
        <crm-item name="last-update" type="date">2012-04-27 17:44:35.0</crm-item>
        <crm-item name="citedby-count" type="number">9</crm-item>
        <doi_record>
          <crossref xmlns="http://www.crossref.org/xschema/1.1" xsi:schemaLocation="http://www.crossref.org/xschema/1.1 http://doi.crossref.org/schemas/unixref1.1.xsd">
            <journal>
              <journal_metadata language="en">
                <full_title>Journal of Molecular Biology</full_title>
                <abbrev_title>Journal of Molecular Biology</abbrev_title>
                <issn media_type="print">00222836</issn>
              </journal_metadata>
              <journal_issue>
                <publication_date media_type="print">
                  <month>1</month>
                  <year>2001</year>
                </publication_date>
                <journal_volume>
                  <volume>305</volume>
                </journal_volume>
                <issue>3</issue>
              </journal_issue>
              <journal_article publication_type="full_text">
                <titles>
                  <title>Specific interaction between anticodon nuclease and the tRNALys wobble base</title>
                </titles>
                <contributors>
                  <person_name contributor_role="author" sequence="first">
                    <given_name>Yue</given_name>
                    <surname>Jiang</surname>
                  </person_name>
                  <person_name contributor_role="author" sequence="additional">
                    <given_name>Roberto</given_name>
                    <surname>Meidler</surname>
                  </person_name>
                  <person_name contributor_role="author" sequence="additional">
                    <given_name>Michal</given_name>
                    <surname>Amitsur</surname>
                  </person_name>
                  <person_name contributor_role="author" sequence="additional">
                    <given_name>Gabriel</given_name>
                    <surname>Kaufmann</surname>
                  </person_name>
                </contributors>
                <publication_date media_type="print">
                  <month>1</month>
                  <year>2001</year>
                </publication_date>
                <pages>
                  <first_page>377</first_page>
                  <last_page>388</last_page>
                </pages>
                <publisher_item>
                  <item_number item_number_type="sequence-number">S0022283600942827</item_number>
                  <identifier id_type="pii">S0022283600942827</identifier>
                </publisher_item>
                <doi_data>
                  <doi>10.1006/jmbi.2000.4282</doi>
                  <resource>http://linkinghub.elsevier.com/retrieve/pii/S0022283600942827</resource>
                </doi_data>
              </journal_article>
            </journal>
          </crossref>
        </doi_record>
      </query>
    </body>
  </query_result>
</crossref_result>
"""
