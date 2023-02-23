import unittest
from gedcom_parser import GedcomTree, Family, Individual

import unittest

from gedcom_parser import GedcomTree


class GedTestUS04Test(unittest.TestCase):
    def test_1_us04_marriage_after_divorce(self):
        """ Check if User Story 04 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us04_marriage_before_divorce(debug=True)
        self.assertIn("@I31@", debug_list)

    def test_2_us04_marriage_after_divorce(self):
        """ Check if User Story 04 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us04_marriage_before_divorce(debug=True)
        self.assertIn("@I30@", debug_list)

    def test_3_us04_marriage_after_divorce(self):
        """ Check if User Story 04 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us04_marriage_before_divorce(debug=True)
        self.assertEqual(len(debug_list), 2)
        self.assertNotIn("@432@", debug_list)

    def test_4_us04_marriage_after_divorce(self):
        """ Check if User Story 04 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us04_marriage_before_divorce(debug=True)
        self.assertNotIn("@234@", debug_list)

    def test_5_us04_marriage_after_divorce(self):
        """ Check if User Story 04 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us04_marriage_before_divorce(debug=True)
        self.assertNotIn("@121@", debug_list)


class GedTestUS05Test(unittest.TestCase):

    def test_1_us05_marriage_before_death(self):
        """ Check if User Story 05 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us05_marriage_before_death(debug=True)
        self.assertEqual(len(debug_list), 2)

    def test_2_us05_marriage_before_death(self):
        """ Check if User Story 05 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us05_marriage_before_death(debug=True)
        self.assertIn("@I7@", debug_list)

    def test_3_us05_marriage_before_death(self):
        """ Check if User Story 05 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us05_marriage_before_death(debug=True)
        self.assertIn("@I8@", debug_list)

    def test_4_us05_marriage_before_death(self):
        """ Check if User Story 05 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us05_marriage_before_death(debug=True)
        self.assertNotIn("@I85@", debug_list)

    def test_5_us05_marriage_before_death(self):
        """ Check if User Story 05 works properly """

        sprint4 = GedcomTree(
            r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us05_marriage_before_death(debug=True)
        self.assertNotIn("@I82@", debug_list)
class Gedcom_US_07_Test(unittest.TestCase):

    def test_1_us07_less_than_150_years_old(self):
        """ Check if User Story 07 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us07_less_than_150_years_old(debug=True)
        self.assertIn("@I7@", debug_list)

    def test_2_us07_less_than_150_years_old(self):
        """ Check if User Story 07 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us07_less_than_150_years_old(debug=True)
        self.assertEqual(len(debug_list), 1)

    def test_3_us07_less_than_150_years_old(self):
        """ Check if User Story 07 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us07_less_than_150_years_old(debug=True)
        self.assertNotIn("@I71@", debug_list)

    def test_4_us07_less_than_150_years_old(self):
        """ Check if User Story 07 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us07_less_than_150_years_old(debug=True)
        self.assertNotIn("@I73@", debug_list)

    def test_5_us07_less_than_150_years_old(self):
        """ Check if User Story 07 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us07_less_than_150_years_old(debug=True)
        self.assertNotIn("@I72@", debug_list)


class GedcomTreeTest(unittest.TestCase):
    """ Test class for Sprint 2 User Stories """

    def test_us19_first_cousins_should_not_marry(self):
        """ Check if User Story 19 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us19_first_cousins_should_not_marry(debug=True)
        self.assertEqual(len(debug_list), 3)
        self.assertIn("@F4@", debug_list)
        self.assertIn("@F8@", debug_list)

    def test_us42_reject_illegitimate_dates(self):
        """ Check if User Story 42 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us42_reject_illegitimate_dates(debug=True)
        self.assertEqual(len(debug_list), 6)
        self.assertIn("@I31@", debug_list)
        self.assertIn("@I32@", debug_list)
        self.assertIn("@F4@", debug_list)
        self.assertIn("@F8@", debug_list)
        self.assertIn("@F16@", debug_list)

    def test_us23_unique_name_and_birth_date(self):
        """ Check if User Story 23 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        bug_number = sprint4.us23_unique_name_and_birth_date(debug=True)
        self.assertEqual(bug_number, 1)

    def test_us07_less_than_150_years_old(self):
        """ Check if User Story 07 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us07_less_than_150_years_old(debug=True)
        self.assertEqual(len(debug_list), 1)
        self.assertIn("@I7@", debug_list)

    def test_us11_no_bigamy(self):
        """ Check if User Story 11 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us11_no_bigamy(debug=True)
        self.assertEqual(len(debug_list), 4)
        self.assertIn("@I6@", debug_list)
        self.assertIn("@I13@", debug_list)
        self.assertIn("@I19@", debug_list)

    def test_us40_include_input_line_numbers(self):
        """ Check if User Story 40 works properly """

        sprint4 = GedcomTree(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=False)
        debug_list = sprint4.us40_include_input_line_numbers(debug=True)

        with open(r'./GEDCOM_files/Sprint_001_test_GEDCOM.ged') as fp:
            for index, line in enumerate(fp):
                pass

        total_lines = index + 1

        for line_numbers in debug_list:
            self.assertTrue(0 < line_numbers)
            self.assertTrue(line_numbers < total_lines)
            self.assertFalse(line_numbers <= 0)
            self.assertFalse(line_numbers > total_lines)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
