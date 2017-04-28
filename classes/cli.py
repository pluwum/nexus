#!/usr/bin/env python
"""
The boiler plate for this file is taken from
the official docops examples from on github
https://raw.githubusercontent.com/docopt/docopt/master/examples/interactive_example.py

Usage:
    cli create_room <room_type> <room_name>
    cli add_person <person_name> <FELLOW> [<wants_accommodation>]
    cli print_room <room_name>
    cli print_allocations [--o=<filename>]
    cli print_unallocated [--o=<filename>]
    cli reallocate_person <person_identifier> <new_room_name>
    cli load_people
    cli save_state [--db=<sqlite_database>]
    load_state <sqlite_database>
    cli (-i | --interactive)
    cli (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --o=<filename>
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from classes.dojo import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyAndelaInteractive (cmd.Cmd):
    intro = 'Welcome to The Dojo Office Space Allocation System!' \
        + ' (type help for a list of commands.)\n\n\n'
    prompt = '>>> '
    file = None

    def __init__(self):
        self.dojo = Dojo()

        super(MyAndelaInteractive, self).__init__()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg['<room_type>']
        room_names = arg['<room_name>']

        for room_name in room_names:
            try:
                result = self.dojo.createRoom(room_name, room_type)
                if(result):
                    print("\n An {} called {} has been successfully created! \n".format(room_type, room_name))
                else:
                    print("\n Creating An office called {} failed! \n".format(arg[room_name]))
            except Exception as ex:
                print('{}\n'.format(ex))

    @docopt_cmd
    def do_add_person(self, arg):

        """Usage: add_person <person_name> [<role>] [<wants_accommodation>]"""

        person_name = arg['<person_name>']
        role = arg['<role>']
        first_name = person_name.split(' ', 1)[-1]
        wants_accommodation = arg['<wants_accommodation>']

        if(wants_accommodation == 'Y'):
            wants_accommodation = True
        else:
            wants_accommodation = False

        try:
            person_identifier = self.dojo.addPerson(person_name,role,wants_accommodation)

            if(person_identifier):
                new_person = self.dojo.people[person_identifier]
                print("{} {} has been successfully added with ID {}".format(role.capitalize(), person_name.capitalize(), new_person.identifier))

                if(new_person.office_space is not None):
                    print("{} has been allocated the office {}".format(first_name.capitalize(), new_person.office_space))
                else:
                    print("No office was allocated to {}".format(first_name.capitalize()))

                if(wants_accommodation):
                    if(new_person.living_space is not None):
                        print("{} has been allocated the livingspace {}".format(first_name.capitalize(), new_person.living_space))
                    else:
                        print("No Living Space was allocated to {}".format(first_name.capitalize()))

        except Exception as ex:
            print('{}\n'.format(ex))

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        try:
            room_occupants = self.dojo.getRoomOccupants(arg['<room_name>'])

            for person_identifier in room_occupants:
                person = self.dojo.people[person_identifier]
                print(person.name)

        except Exception as ex:
            print('{}\n'.format(ex))

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=<filename>]"""

        print_to_file = False

        text_to_print = ""
        if(arg['--o']):
            print_to_file = True

        try:
            rooms = self.dojo.getRoomAllocations()

            for room in rooms:
                if not print_to_file:
                    text_to_print = text_to_print+"ROOM {} \n".format(room.name.upper())

                    text_to_print = text_to_print+"-------------------------------------\n"
                else:
                    #TODO: Write output to file here
                    pass
                members = []
                for person_identifier in room.occupants:
                    person = self.dojo.people[person_identifier]
                    members.append(person.name)

                text_to_print = text_to_print+", ".join(members)
                text_to_print = text_to_print+"\n"

            if not print_to_file:
                print(text_to_print)
            else:
                file = open(arg['--o'], 'w')
                file.write(text_to_print)

        except Exception as ex:
            print('{}\n'.format(ex))

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--o=<filename>]"""

        doc = self.do_print_unallocated.__doc__
        print_to_file = False

        if(arg['--o']):
            print_to_file = True

        if(print_to_file):
            #TODO:
            print('print to file set')
        print(arg)
        try:
            unallocated = self.dojo.getUnallocatedPeople()
            if(len(unallocated)>0):
                print("------------------------------------------\n")
                for person in unallocated:
                    print("{} {}".format(person.role, person.name))
                return
            print('The are currently no unallocated persons in the system')
        except Exception as ex:
            print('{}\n'.format(ex))

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        try:
            person_identifier = int(arg['<person_identifier>'])
            room_name = arg['<new_room_name>']
            result = self.dojo.rellocatePerson(person_identifier, room_name)
            if result:
                print('{} Successfully relocated to {} {}'.format(self.dojo.people[person_identifier].name, self.dojo.rooms[room_name].room_type, room_name))
                return
            print('Oops!! Something went wrong while reallocating')
        except Exception as ex:
            print('{}\n'.format(ex))

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people"""
        try:
            print(arg)
        except Exception as ex:
            print('{}\n'.format(ex))

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=<sqlite_database>]"""

        try:
            print(arg)
        except Exception as ex:
            print('{}\n'.format(ex))

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <sqlite_database>"""

        try:
            print(arg)
        except Exception as ex:
            print('{}\n'.format(ex))

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

    def do_exit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyAndelaInteractive().cmdloop()

print(opt)
