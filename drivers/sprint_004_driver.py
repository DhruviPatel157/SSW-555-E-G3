from gedcom_parser import GedcomTree


def sprint_004_main(filename=None):
    """ Main function to run Sprint 1 User Stories """

    sprint1 = GedcomTree(r'../GEDCOM_files/Sprint_004_test_GEDCOM.ged', pt=True)
    sprint1.us16_male_lastname()
    sprint1.us22_unique_ids()
    sprint1.us14_multiple_births_fewer_than_6()
    sprint1.us15_fewer_than_15_siblings()
    sprint1.us31_list_living_single(pt=True)
    sprint1.us30_list_living_married(pt=True)
    sprint1.us38_upcoming_birthdays(pt=True)
    sprint1.us33_list_orphans(pt=True)

    for errors in sprint1.error_log:
        print(errors)

    if filename:
        try:
            fp = open(filename, 'a')

        except FileNotFoundError:
            print("Can't Open!")
        else:
            with fp:
                fp.write("Sprint 1 Results\n")
                sprint = GedcomTree(r'./GEDCOM_files/Sprint1_test_GEDCOM.ged', pt=False, write=True)
                sprint.us14_multiple_births_fewer_than_6()
                sprint.us15_fewer_than_15_siblings()
                sprint.us33_list_orphans(write=True)
                sprint.us38_upcoming_birthdays(write=True)
                sprint.us30_list_living_married(write=True)
                sprint.us31_list_living_single(write=True)
                sprint.us22_unique_ids()
                sprint.us16_male_lastname()

                for i in sprint.write_to_file:
                    for content in i:
                        fp.write(f'{str(content)}\n')

                fp.write("Sprint 1 Error Log\n")

                for errors in sprint.error_log:
                    fp.write(f'{errors}\n')

                fp.write("\n")
