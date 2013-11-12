from django.test import TestCase

from lib import crossref

#  flake8: noqa

class DoiTests(TestCase):

    def test_doi_matcher(self):
        """
        tests suggested from from http://stackoverflow.com/a/10324802
        """

        tests = (
            ("This is a short DOI: 10.1000/123456.", "10.1000/123456"),
            ("This is NOT a DOI: 4210.1000/123456.", ""),
            ("This is a long DOI: 10.1016.12.31/nature.S0735-1097(98)2000/12/31/34:7-7!!!",
                "10.1016.12.31/nature.S0735-1097(98)2000/12/31/34:7-7"),
            ("10.1007/978-3-642-28108-2_19", "10.1007/978-3-642-28108-2_19"),
            ("10.1007.10/978-3-642-28108-2_19 (fictitious example, see @Ju9OR comment)",
                "10.1007.10/978-3-642-28108-2_19"),
            ("10.1016/S0735-1097(98)00347-7", "10.1016/S0735-1097(98)00347-7"),
            ("10.1579/0044-7447(2006)35\[89:RDUICP\]2.0.CO;2",
                "10.1579/0044-7447(2006)35\[89:RDUICP\]2.0.CO;2"),
            ("doi:10.1203/00006450-199305000-00005", "10.1203/00006450-199305000-00005"),
            ("<geo coords=\"10.4515260,51.1656910\"></geo>", ""),
        )
        for given, expected in tests:
            result = crossref.match_doi(given)
            assert result == expected, 'result "%s" from query "%s" does not match expected value "%s"' % (result, given, expected)


    def test_nonbarfing_invalid_param(self):
        r = crossref.query('pid', None)
        assert r['msg'] == 'invalid doi parameter: None'
        r = crossref.query('pid', 0)
        assert r['msg'] == 'invalid doi parameter: 0'


    def test_nonbarfing_emptiness(self):
        r = crossref.parse_crossref_output('')
        assert r['msg'] == 'crossref error', 'missing query should cause a crossref error'
        assert 'compendia' not in r, 'empty reply should have an empty compendia'

        r = crossref.query('pid', 'no match')
        assert r['msg'] == 'invalid doi parameter: no match'

    def test_conference_paper(self):
        # 10.1109/UKSIM.2011.38
        r = crossref.parse_crossref_output(self.get_conference_paper())
        assert 'compendia' in r, 'able to find compendia in conference paper query'

        compendia = r['compendia']
        assert compendia is not None, r

        assert compendia['title'] == 'Trend Modelling of Elderly Lifestyle within an Occupancy Simulator'

    def test_journal_article(self):
        # 10.1006/jmbi.2000.4282<
        r = crossref.parse_crossref_output(self.get_journal_article())
        assert 'compendia' in r, 'able to find compendia fields in article paper query'

        compendia = r['compendia']
        assert compendia is not None, r

        assert compendia['title'] == 'Specific interaction between anticodon nuclease and the tRNALys wobble base'


    def get_conference_paper(self):
        return """
<?xml version="1.0" encoding="UTF-8"?>
<crossref_result xmlns="http://www.crossref.org/qrschema/3.0" version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.crossref.org/qrschema/3.0 http://www.crossref.org/schema/queryResultSchema/crossref_query_output3.0.xsd">
  <query_result>
    <head>
      <doi_batch_id>none</doi_batch_id>
    </head>
    <body>
      <query status="resolved">
        <doi type="conference_paper">10.1109/UKSIM.2011.38</doi>
        <crm-item name="publisher-name" type="string">Institute of Electrical &amp; Electronics Engineers (IEEE)</crm-item>
        <crm-item name="prefix-name" type="string">Institute of Electrical &amp; Electronics Engineers (IEEE)</crm-item>
        <crm-item name="citation-id" type="number">47878037</crm-item>
        <crm-item name="book-id" type="number">837188</crm-item>
        <crm-item name="deposit-timestamp" type="number">20110425</crm-item>
        <crm-item name="owner-prefix" type="string">10.1109</crm-item>
        <crm-item name="last-update" type="date">2011-04-26 10:39:59.0</crm-item>
        <crm-item name="citedby-count" type="number">0</crm-item>
        <doi_record>
          <crossref xmlns="http://www.crossref.org/xschema/1.1" xsi:schemaLocation="http://www.crossref.org/xschema/1.1 http://doi.crossref.org/schemas/unixref1.1.xsd">
            <conference>
              <event_metadata>
                <conference_name>2011 UkSim 13th International Conference on Computer Modelling and Simulation (UKSim)</conference_name>
                <conference_location>Cambridge, United Kingdom</conference_location>
                <conference_date start_month="03" start_year="2011" start_day="30" end_month="04" end_year="2011" end_day="1" />
              </event_metadata>
              <proceedings_metadata>
                <proceedings_title>2011 UkSim 13th International Conference on Computer Modelling and Simulation</proceedings_title>
                <publisher>
                  <publisher_name>IEEE</publisher_name>
                </publisher>
                <publication_date>
                  <month>03</month>
                  <year>2011</year>
                </publication_date>
                <isbn media_type="print">978-1-61284-705-4</isbn>
              </proceedings_metadata>
              <conference_paper>
                <contributors>
                  <person_name sequence="first" contributor_role="author">
                    <given_name>Sawsan M.</given_name>
                    <surname>Mahmoud</surname>
                  </person_name>
                  <person_name sequence="additional" contributor_role="author">
                    <given_name>M. Javad</given_name>
                    <surname>Akhlaghinia</surname>
                  </person_name>
                  <person_name sequence="additional" contributor_role="author">
                    <given_name>Ahmad</given_name>
                    <surname>Lotfi</surname>
                  </person_name>
                  <person_name sequence="additional" contributor_role="author">
                    <given_name>Caroline</given_name>
                    <surname>Langensiepen</surname>
                  </person_name>
                </contributors>
                <titles>
                  <title><![CDATA[Trend Modelling of Elderly Lifestyle within an Occupancy Simulator]]></title>
                </titles>
                <publication_date>
                  <month>03</month>
                  <year>2011</year>
                </publication_date>
                <pages>
                  <first_page>156</first_page>
                  <last_page>161</last_page>
                </pages>
                <publisher_item>
                  <item_number item_number_type="arNumber">5754227</item_number>
                </publisher_item>
                <doi_data>
                  <doi>10.1109/UKSIM.2011.38</doi>
                  <resource>http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=5754227</resource>
                </doi_data>
              </conference_paper>
            </conference>
          </crossref>
        </doi_record>
      </query>
    </body>
  </query_result>
</crossref_result>
"""

    def get_journal_article(self):
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
