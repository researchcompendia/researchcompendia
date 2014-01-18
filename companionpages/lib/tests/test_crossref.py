# -*- coding: utf-8 -*-
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

    def test_nonbarfing_unicode(self):
        # 10.12688/f1000research.2-217.v1
        xml = self.get_record_with_unicode_character()
        r = crossref.parse_crossref_output(xml)

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

    def get_record_with_unicode_character(self):
        return """
<?xml version="1.0" encoding="UTF-8"?>
<crossref_result xmlns="http://www.crossref.org/qrschema/3.0" version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.crossref.org/qrschema/3.0 http://www.crossref.org/schema/queryResultSchema/crossref_query_output3.0.xsd">
  <query_result>
    <head>
      <doi_batch_id>none</doi_batch_id>
    </head>
    <body>
      <query status="resolved">
        <doi type="journal_article">10.12688/f1000research.2-217.v1</doi>
        <crm-item name="publisher-name" type="string">F1000 Research, Ltd.</crm-item>
        <crm-item name="prefix-name" type="string">F1000 Research, Ltd.</crm-item>
        <crm-item name="citation-id" type="number">64814802</crm-item>
        <crm-item name="journal-id" type="number">175545</crm-item>
        <crm-item name="deposit-timestamp" type="number">1382710500301</crm-item>
        <crm-item name="owner-prefix" type="string">10.12688</crm-item>
        <crm-item name="last-update" type="date">2013-10-25 10:26:36.0</crm-item>
        <crm-item name="citedby-count" type="number">0</crm-item>
        <doi_record>
          <crossref xmlns="http://www.crossref.org/xschema/1.1" xsi:schemaLocation="http://www.crossref.org/xschema/1.1 http://doi.crossref.org/schemas/unixref1.1.xsd">
            <journal>
              <journal_metadata language="en">
                <full_title>F1000Research</full_title>
                <abbrev_title>F1000Res</abbrev_title>
                <issn media_type="electronic">2046-1402</issn>
                <doi_data>
                  <doi>10.12688/f1000research</doi>
                  <resource>http://www.f1000research.com/</resource>
                </doi_data>
              </journal_metadata>
              <journal_article>
                <titles>
                  <title>MethylExtract: High-Quality methylation maps and SNV calling from whole genome bisulfite sequencing data</title>
                </titles>
                <contributors>
                  <person_name sequence="first" contributor_role="author">
                    <given_name>Guillermo</given_name>
                    <surname>Barturen</surname>
                  </person_name>
                  <person_name sequence="additional" contributor_role="author">
                    <given_name>Antonio</given_name>
                    <surname>Rueda</surname>
                  </person_name>
                  <person_name sequence="additional" contributor_role="author">
                    <given_name>José L.</given_name>
                    <surname>Oliver</surname>
                  </person_name>
                  <person_name sequence="additional" contributor_role="author">
                    <given_name>Michael</given_name>
                    <surname>Hackenberg</surname>
                  </person_name>
                </contributors>
                <publication_date media_type="online">
                  <month>10</month>
                  <day>15</day>
                  <year>2013</year>
                </publication_date>
                <publisher_item>
                  <item_number item_number_type="r-v-db-id">2616</item_number>
                </publisher_item>
                <crossmark>
                  <crossmark_policy>10.12688/f1000research.crossmark-policy</crossmark_policy>
                  <crossmark_domains>
                    <crossmark_domain>
                      <domain>f1000research.com</domain>
                    </crossmark_domain>
                  </crossmark_domains>
                  <crossmark_domain_exclusive>true</crossmark_domain_exclusive>
                  <custom_metadata>
                    <assertion group_label="Current Referee Status"
                    group_name="current-referee-status" label="Referee status"
                    name="referee-status" order="0"
                    href="http://f1000research.com/articles/2-217/v1#article-reports">Approved
                    with reservations</assertion>
                  
                  <assertion group_label="Article Reports"
                  group_name="article-reports" label="Referee Report"
                  name="referee-response-2103" order="1"
                  href="http://f1000research.com/articles/2-217/v1#referee-response-2103">&lt;b&gt;Michael
                  Stadler&lt;/b&gt; Friedrich-Miescher Institute for Biomedical
                  Research, Basel, Switzerland Approved with reservations: 25
                  Oct 2013 (v1); 
                  I have read this submission. I believe that I have an
                  appropriate level of expertise to confirm that it is of an
                  acceptable scientific standard, however I have significant
                  reservations, as outlined above.; The authors present the
                  tool MethylExtract that combines extraction of methylation
                  states and SNV calling, given alignments of
                  bisulfite-converted reads to a reference in SAM/BAM format.
                  Methylated CpG are mutation hotspots - dealing with SNVs is
                  therefore an important part of any analysis of Bis-seq
                  data.The main functions of MethylExtract are implemented in a
                  single Perl script, which should make it easy to use -
                  unfortunately I could not verify this because it failed to
                  run in my environment (see below).The performance of
                  MethylExtract is evaluated using simulated sequence data
                  (completely methylated or completely unmethylated containing
                          sequencing errors and SNVs) and compared to Bis-SNP,
                  a conceptually similar tool that is based on the GATK variant
                  calling package. The simulations cover most important aspects
                  of the tool; however, the paper would benefit from extended
                  simulations and a test on a real dataset. For example, the
                  current evaluation does not cover Bis-seq datasets with very
                  low or very high coverage or intermediate methylation levels
                  (see minor issues below).The paper is clearly written, and
                  the conclusions are supported by the presented results.
                  &lt;b&gt;Major issues:&lt;/b&gt;The &lt;b&gt;MethylExtract
                  perl script&lt;/b&gt; (version 1.3) did not run in my
                  environment (RHEL 6, with Kernel 2.6.32-220.7.1.el6.x86_64,
                          perl 5.10.1 built for x86_64-linux-thread-multi).
                  Trying to run the main script resulted in a compilation
                  error:&amp;nbsp; &amp;gt;perl MethylExtract_1.3.pl&amp;nbsp;
                  Type of arg 1 to keys must be hash (not hash element) at
                  MethylExtract_1.3.pl line 318, near &amp;quot;})
                  &amp;quot;&amp;nbsp; Execution of MethylExtract_1.3.pl
                  aborted due to compilation errors.It is possible that the
                  problem lies in the combination of the script and the test
                  environment. However, the test environment fulfills the
                  stated requirements and dependencies.&amp;nbsp;
                  &lt;b&gt;Figure 6&lt;/b&gt; and corresponding text: A single
                  point comparison of Sn/PPV between MethylExtract and Bis-SNP,
                  both with default parameters, is not very informative.
                  Typically there is a trade-off between sensitivity and
                  specificity which can be influenced by the choice of
                  parameter values such as the score or P value cutoffs. It is
                  possible that with slightly altered parameter values, the
                  improved Sn/reduced PPV of MethylExtract compared to Bis-SNP
                  turn into the opposite. The two tools should therefore be
                  compared using varying parameter settings or cutoffs
                  (altering the trade-off between Sn and PPV) and then relating
                  the resulting specificity and sensitivity in an ROC analysis.
                  The same applies in principle to the results presented in
                  Figure 3. &lt;b&gt;Minor issues:&lt;/b&gt;
                  &lt;b&gt;Simulations - readout:&lt;/b&gt; The current
                  evaluation of &amp;quot;correct methylation&amp;quot;
                  requires exact identity of simulated and estimated
                  methylation states. This criterium is very stringent yet may
                  not be able to uncover systematic problems. In practice, a
                  very small deviation from the true methylation level may be
                  tolerable. For illustration: A tool that produces many
                  incorrect values that are off only by a small amount may be
                  preferable to a tool that produces fewer incorrect values
                  that are several-fold off. I would suggest using a continuous
                  measure of performance (e.g. the differences between true and
                          estimated methylation levels) or to allow for a
                  minimum deviation.&amp;nbsp; &lt;b&gt;Simulations -
                  methylation levels:&lt;/b&gt; In the introduction, the
                  authors point out the value of methylation levels as opposed
                  to methylation states. Also, intermediate methylation is
                  present in virtually all real world Bis-seq data sets. The
                  simulations should take this into account and also contain
                  C's with intermediate methylation levels (e.g. around 50%
                  methylation).&amp;nbsp; &lt;b&gt;Simulations -
                  coverage:&lt;/b&gt; The current simulations are performed at
                  15- and 20 fold coverage and the two yield very similar
                  results. More informative differences in performance may be
                  observed when simulating data at even lower (~5-fold) or
                  higher (&amp;gt;30-fold) coverage, which are commonly found
                  in published Bis-seq datasets.&amp;nbsp; &lt;b&gt;Runtime
                  comparison:&lt;/b&gt; It's surprising that even though
                  MethylExtract supports BAM input, SAM.gz was used for runtime
                  measurements, while Bis-SNP was reading from BAM input.
                  Unpacking of alignments from BAM files is CPU-intensive, and
                  I wonder if MethylExtract would take more time if it was run
                  on the same input as Bis-SNP.&amp;nbsp; &lt;b&gt;Table
                  1:&lt;/b&gt; MethylExtract is listed to support both SAM and
                  BAM inputs. However, it does not directly read BAM files, but
                  converts them to SAM using SAMtools. Using such a conversion,
                  BSMAP and Bismark also support BAM input. I would suggest not
                  to discriminate between SAM and BAM inputs in the table to
                  avoid confusion based on this subtle difference.&amp;nbsp;
                  &lt;b&gt;Impact of parameter choice when analyzing real world
                  data:&lt;/b&gt; For some parameters (e.g.
                          &amp;quot;duplicated reads filter&amp;quot; and
                          &amp;quot;elimination of bisulfite conversion
                          failure&amp;quot;), it is unclear how they would
                  impact results in a real world analysis. A comparison of the
                  results obtained on an experimental dataset with different
                  parameter values could identify sensitive parameters and
                  guide users when choosing parameters for their own
                  analysis.&amp;nbsp; &lt;b&gt;Figure 5:&lt;/b&gt; The labels
                  of the two y-axes are missing. In addition, CpG coverage
                  (blue line) was probably scaled to be plotted on the same
                  axis; if that is the case, it should be described in the
                  legend and/or indicated in the plot.; &lt;b&gt;Competing
                  Interests:&lt;/b&gt;No competing interests were
                  disclosed.</assertion>

                  </custom_metadata>
                </crossmark>
                <doi_data>
                  <doi>10.12688/f1000research.2-217.v1</doi>
                  <resource>http://f1000research.com/articles/2-217/v1</resource>
                  <collection property="crawler-based" setbyID="fres">
                    <item crawler="iParadigms">
                      <resource>http://f1000research.com/articles/2-217/v1/iparadigms</resource>
                    </item>
                  </collection>
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
