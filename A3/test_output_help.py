import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import output_help


class TestOutput_help(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_help(self, mock_output):
        expected_output = """****************************************************************************************
            Welcome to ~~Escape from BCIT~~
            A game of daring-do, perilous movements, underwhelming battle and nonsense.
            
            Your purpose is to find the exit on the 1st floor and escape.
            But beware! Along the way you may encounter instructors whose only goal is to terrorize you 
            with learning evaluations!
            
            Will you escape? Who knows!!!
            
            Movement commands:
            - n: go north
            - s: go south
            - e: go east
            - w: go west (life is peaceful there.)
            - quit: go back to real life
            - help: print this message
            
            Context commands:
            These will be explained in their own context.
            
            God mode:
            - god_battle: increase likelihood of getting battle-determining tech
            - god_stairs: increase likelihood of finding stairs
            - god_exit: the location of the exit
            
            Note that god-mode cannot be de-activated. I hope your tiny ego can cope.
            
            Enjoy!
            - Sid Viscous
            ****************************************************************************************\n"""

        output_help()

        self.assertEqual(expected_output, mock_output.getvalue())
