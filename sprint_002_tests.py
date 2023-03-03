import unittest
import datetime

from gedcom_parser import GedcomTree


class GedcomTreeTest(unittest.TestCase):

    def test_us25_unique_first_names_inFamilies(self):
        """ Check if User Story 25 works properly """

        sprint3 = GedcomTree(r'./GEDCOM_files/Sprint_002_test_GEDCOM.ged')
        debug_list = sprint3.us25_unique_first_names_inFamilies(debug=True)
        self.assertEqual(len(debug_list), 2)
        self.assertIn('@F8@', debug_list)
        self.assertIn('@F10@', debug_list)

    def test_us18_siblings_should_not_marry(self):
        """ Check if User Story 18 works properly """

        sprint3 = GedcomTree(r'GEDCOM_files/Sprint_002_test_GEDCOM.ged')
        debug_list = sprint3.us18_siblings_should_not_marry(debug=True)
        self.assertEqual(len(debug_list), 2)
        self.assertIn('@F3@', debug_list)
        self.assertIn('@F11@', debug_list)

    def test_us24_unique_families_by_spouse(self):
        """ Check if User Story 24 works properly """

        sprint3 = GedcomTree(r'GEDCOM_files/Sprint_002_test_GEDCOM.ged')
        debug_list = sprint3.us24_unique_families_by_spouse(debug=True)
        self.assertEqual(len(debug_list), 1)
        self.assertIn('@F15@', debug_list)

    def test_us39_list_upcoming_anniversaries(self):
        """ Check if User Story 39 works properly """

        sprint3 = GedcomTree(r'GEDCOM_files/Sprint_002_test_GEDCOM.ged')
        debug_list = sprint3.us39_list_upcoming_anniversaries(debug=True)
        for anniversary in debug_list:
            self.assertTrue(anniversary >= sprint3.current_date)
            self.assertTrue(anniversary <= (sprint3.current_date + datetime.timedelta(days=30)))
        # self.assertEqual(len(debug_list), 2)
        # self.assertIn('@F1@', debug_list)
        # self.assertIn('@F7@', debug_list)

    def test_us29_list_deceased(self):
        """ Check if User Story 29 works properly """

        sprint3 = GedcomTree(r'GEDCOM_files/Sprint_002_test_GEDCOM.ged')
        debug_list = sprint3.us29_list_deceased(debug=True)
        self.assertEqual(len(debug_list), 7)
        self.assertIn('@I7@', debug_list)
        self.assertIn('@I8@', debug_list)

    def test_us10_marry_after_14(self):
        """ Check if User Story 10 works properly """

        sprint3 = GedcomTree(r'GEDCOM_files/Sprint_002_test_GEDCOM.ged')
        debug_list = sprint3.us10_marry_after_14(debug=True)
        self.assertEqual(len(debug_list), 3)
        self.assertIn('@I21@', debug_list)
        self.assertIn('@I22@', debug_list)
        self.assertIn('@I7@', debug_list)

    def test_us02_birth_before_marriage(self):
        """ Check if User Story 2 works properly """

        sprint3 = GedcomTree(r'GEDCOM_files/Sprint_002_test_GEDCOM.ged')
        debug_list = sprint3.us02_birth_before_marriage(debug=True)
        self.assertEqual(len(debug_list), 2)
        self.assertIn('@I7@', debug_list)
        self.assertIn('@I22@', debug_list)

    def test_us03_birth_before_death(self):
        """ Check if User Story 3 works properly """

        # Create a GedcomTree object by passing the path of the GEDCOM file
        # to be parsed to the GedcomTree constructor.
        sprint3 = GedcomTree(r'GEDCOM_files/Sprint_002_test_GEDCOM.ged')

        # Call the us03_birth_before_death method of the GedcomTree object to
        # retrieve a list of individuals whose death occurred before their birth.
        # Set debug=True to print debug information to the console.
        debug_list = sprint3.us03_birth_before_death(debug=True)

        # Check if the length of the debug_list is equal to 2.
        self.assertEqual(len(debug_list), 2)

        # Check if the '@I7@' and '@I22@' individual IDs are in the debug_list.
        self.assertIn('@I7@', debug_list)
        self.assertIn('@I22@', debug_list)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)