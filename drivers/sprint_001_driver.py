from gedcom_parser import GedcomTree


def sprint_001_main(filename=None):
    scrum = GedcomTree(r'../GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=True, write=False)
    scrum.us04_marriage_before_divorce()
    scrum.us05_marriage_before_death()
    scrum.us19_first_cousins_should_not_marry()
    scrum.us42_reject_illegitimate_dates()
    scrum.us23_unique_name_and_birth_date()
    scrum.us07_less_than_150_years_old()
    scrum.us11_no_bigamy()
    scrum.us40_include_input_line_numbers(pt=True)
    scrum.us01_dates_before_current_date()
    scrum.us02_birth_before_marriage()

    for error in scrum.error_log:
        print(error)

    if filename:
        try:
            fp = open(filename, 'a')
        except FileNotFoundError:
            print("Can't Open!")
        else:
            with fp:
                fp.write("Sprint 1 Results\n")
                scrum = GedcomTree(r'GEDCOM_files/Sprint_001_test_GEDCOM.ged', pt=False, write=True)
                scrum.us04_marriage_before_divorce()
                scrum.us05_marriage_before_death()
                scrum.us19_first_cousins_should_not_marry()
                scrum.us42_reject_illegitimate_dates()
                scrum.us23_unique_name_and_birth_date()
                scrum.us07_less_than_150_years_old()
                scrum.us11_no_bigamy()
                scrum.us40_include_input_line_numbers(write=True)

                for i in scrum.write_to_file:
                    for content in i:
                        fp.write(f'{str(content)}\n')

                fp.write("Sprint 1 Error Log\n")

                for errors in scrum.error_log:
                    fp.write(f'{errors}\n')

                fp.write('\n')
