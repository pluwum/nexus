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
    prompt = '(cli) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>"""

        print(arg)

    @docopt_cmd    
    def do_add_person(self, arg):
        """Usage: add_person <person_name> <FELLOW> [<wants_accommodation>]"""

        print(arg)

    @docopt_cmd    
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""

        print(arg)

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