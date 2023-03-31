from gedcom_parser import GedcomTree


def sprint_003_main(filename=None):
    """ Main function to run Sprint 2 User Stories """

    scrum = GedcomTree(r'../GEDCOM_files/Sprint_003_test_GEDCOM.ged', pt=True, write=True)
    scrum2 = GedcomTree(r'../GEDCOM_files/U17_21_test.ged', pt=False, write=False)
    scrum.us08_birth_before_marriage_of_parents()
    scrum.us09_birth_before_death_of_parents()
    scrum.us35_list_recent_births(pt=True)
    scrum.us36_list_recent_deaths(pt=True)
    scrum.us27_include_individual_ages(pt=True)
    scrum.us06_divorce_before_death()
    scrum2.us17_no_marriage_to_children()
    scrum2.us21_correct_gender_for_role()

    print('Error Log:')
    for errors in scrum.error_log:
        print(f'{errors}')

    for errors in scrum2.error_log:
        print(f'{errors}')

    if filename:
        try:
            fp = open(filename, 'a')

        except FileNotFoundError:
            print("Can't Open!")
        else:
            with fp:
                fp.write("Sprint 2 Results\n")
                scrum = GedcomTree(r'./GEDCOM_files/Sprint2_test_GEDCOM.ged', pt=False, write=True)
                scrum2 = GedcomTree(r'./GEDCOM_files/U17_21_test.ged', pt=False, write=False)
                scrum.us08_birth_before_marriage_of_parents()
                scrum.us09_birth_before_death_of_parents()
                scrum.us35_list_recent_births(write=True)
                scrum.us36_list_recent_deaths(write=True)
                scrum.us27_include_individual_ages(write=True)
                scrum.us06_divorce_before_death()
                scrum2.us17_no_marriage_to_children()
                scrum2.us21_correct_gender_for_role()

                for j in scrum.write_to_file:
                    for content in j:
                        fp.write(f'{str(content)}\n')

                fp.write("Sprint 2 Error Log\n")

                for errors in scrum.error_log:
                    fp.write(f'{errors}\n')

                for errors in scrum2.error_log:
                    fp.write(f'{errors}\n')

                fp.write("\n")
