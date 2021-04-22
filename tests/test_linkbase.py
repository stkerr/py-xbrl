import logging
import sys
import unittest
import os
import time
from xbrl_parser.cache import HttpCache
from xbrl_parser.linkbase import parse_linkbase, Linkbase, LinkbaseType


class LinkbaseTest(unittest.TestCase):

    def test_parse_linkbase(self):
        """
        Unit test for linkbase.parse_linkbase()
        """
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        cache_dir: str = os.path.abspath('./../cache/') + '/'
        cache: HttpCache = HttpCache(cache_dir)

        linkbase_path: str = './data/example-lab.xml'
        linkbase: Linkbase = parse_linkbase(linkbase_path, LinkbaseType.LABEL)
        self.assertEqual(len(linkbase.extended_links), 1)
        self.assertEqual(linkbase.extended_links[0].root_locators[0].name, 'example_Assets')
        label_arcs = linkbase.extended_links[0].root_locators[0].children
        self.assertEqual(label_arcs[0].labels[0].text, 'Assets, total')
        self.assertIn('An asset is a resource with economic value', label_arcs[1].labels[0].text)


if __name__ == '__main__':
    unittest.main()
