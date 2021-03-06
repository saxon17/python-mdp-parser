import unittest

from mpd.parser import MPDParser


class XML2MDPTestCase(unittest.TestCase):
    def test_xml2mpd_from_string(self):
        mpd_string = '''
        <MPD xmlns="urn:mpeg:DASH:schema:MPD:2011" mediaPresentationDuration="PT0H1M52.43S" minBufferTime="PT1.5S"
        profiles="urn:mpeg:dash:profile:isoff-on-demand:2011" type="static">
          <Period duration="PT0H1M52.43S" start="PT0S">
            <AdaptationSet>
              <ContentComponent contentType="video" id="1" />
              <Representation bandwidth="4190760" codecs="avc1.640028" height="1080" id="1" mimeType="video/mp4" width="1920">
                <BaseURL>motion-20120802-89.mp4</BaseURL>
                <SegmentBase indexRange="674-981">
                  <Initialization range="0-673" />
                </SegmentBase>
              </Representation>
            </AdaptationSet>
          </Period>
        </MPD>
        '''
        self.assertMPD(MPDParser.parse(mpd_string))

    def test_xml2mpd_from_file(self):
        self.assertMPD(MPDParser.parse('./tests/mpd-samples/sample-001.mpd'))
        self.assertMPD(MPDParser.parse('./tests/mpd-samples/motion-20120802-manifest.mpd'))
        self.assertMPD(MPDParser.parse('./tests/mpd-samples/oops-20120802-manifest.mpd'))

    def test_xml2mpd_from_url(self):
        mpd_url = 'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/motion-20120802-manifest.mpd'
        self.assertMPD(MPDParser.parse(mpd_url))

    def assertMPD(self, mpd):
        self.assertTrue(mpd is not None)
        self.assertTrue(len(mpd.periods) > 0)
        self.assertTrue(mpd.periods[0].adaptation_sets is not None)
        self.assertTrue(len(mpd.periods[0].adaptation_sets) > 0)
        self.assertTrue(mpd.periods[0].adaptation_sets[0].representations is not None)
        self.assertTrue(len(mpd.periods[0].adaptation_sets[0].representations) > 0)
        self.assertTrue(len(mpd.periods[0].adaptation_sets[0].representations[0].id) > 0)
