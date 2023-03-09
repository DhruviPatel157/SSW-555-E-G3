from gedcom_parser import GedcomTree


def sprint_002_main(filename=None):
    scrum = GedcomTree(r'../GEDCOM_files/Sprint_002_test_GEDCOM.ged', pt=True, write=False)
    scrum.us25_unique_first_names_inFamilies()
    scrum.us18_siblings_should_not_marry()
    scrum.us02_birth_before_marriage()
    scrum.us03_birth_before_death()
    scrum.us29_list_deceased(pt=True)
    scrum.us10_marry_after_14()
    scrum.us24_unique_families_by_spouse()
    scrum.us39_list_upcoming_anniversaries(pt=True)

    for error in scrum.error_log:
        print(error)

    if filename:
        try:
            fp = open(filename, 'a')
        except FileNotFoundError:
            print("Can't Open!")
        else:
            with fp:
                fp.write("Sprint 3 Results\n")
                scrum = GedcomTree(r'../GEDCOM_files/Sprint_002_test_GEDCOM.ged', pt=False, write=True)
                scrum.us25_unique_first_names_inFamilies()
                scrum.us18_siblings_should_not_marry()
                scrum.us02_birth_before_marriage()
                scrum.us03_birth_before_death()
                scrum.us29_list_deceased(write=True)
                scrum.us10_marry_after_14()
                scrum.us24_unique_families_by_spouse()
                scrum.us39_list_upcoming_anniversaries(write=True)

                for i in scrum.write_to_file:
                    for content in i:
                        fp.write(f'{str(content)}\n')

                fp.write("Sprint 3 Error Log\n")

                for errors in scrum.error_log:
                    fp.write(f'{errors}\n')

                fp.write('\n')


