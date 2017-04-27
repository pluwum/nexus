#!/usr/bin/env python
"""
The boiler plate for this file is taken from 
the official docops examples from on github 
https://raw.githubusercontent.com/docopt/docopt/master/examples/interactive_example.py

Usage:
    cli create_room <room_type> <room_name>
    cli add_person <person_name> <FELLOW> [<wants_accommodation>]
    cli (-i | --interactive)
    cli (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit

from classes.dojo import Dojo
from classes.andela import Andela

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
    intro = 'Welcome to Office Space Allocation System!' \
        + ' (type help for a list of commands.)'
    prompt = '>>> '
    file = None        

    def __init__(self):
        #self.dojo1 = Dojo()
        self.andela = Andela()

        super(MyAndelaInteractive, self).__init__()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg['<room_type>']
        room_names = arg['<room_name>']

        for room_name in room_names:
            try:
                result = self.andela.createRoom(room_name, room_type)
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

        if(wants_accommodation == 'Y' ):
            wants_accommodation = True
        else:
            wants_accommodation = False

        try:
            person_identifier = self.andela.addPerson(person_name,role,wants_accommodation)

            if(person_identifier):
                new_person = self.andela.people[person_identifier]['person']
                print("{} {} has been successfully added".format(role.capitalize(), person_name.capitalize()))
                
                if(new_person.office_space is not None):
                    print("{} has been allocated the office {}".format(first_name.capitalize(), new_person.office_space.name))
                else:
                    print("No office was allocated to {}".format(first_name.capitalize()))

                if(wants_accommodation):
                    if(new_person.living_space is not None):
                        print("{} has been allocated the livingspace {}".format(first_name.capitalize(), new_person.living_space.name))
                    else:
                        print("No Living Space was allocated to {}".format(first_name.capitalize()))

        except Exception as ex:
            print('{}\n'.format(ex)) 

    @docopt_cmd    
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        try:
            room_occupants = self.andela.getRoomOccupants(arg['<room_name>'])

            for person_identifier in room_occupants:
                person = self.andela.people[person_identifier]['person']
                print(person.name)

        except Exception as ex:
            print('{}\n'.format(ex))  

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [-o=<filename>]"""

        print(arg)

    @docopt_cmd    
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [-o=<filename>]"""

        print(arg)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""

        print(arg)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people"""

        print(arg)

    @docopt_cmd    
    def do_save_state(self, arg):
        """Usage: save_state [--db=<sqlite_database>]"""

        print(arg)

    @docopt_cmd    
    def do_load_state(self, arg):
        """Usage: load_state <sqlite_database>"""

        print(arg)

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