import unittest
from nba_players import Solution
import sys
from io import StringIO

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testSolutionRaisesExceptionOnNoNNumericTargets(self):
        """
        test whether nbaPlayersHeights method 
        raises type erros on non numeric target 
        arguments.
        """

        self.assertRaises(
            TypeError, self.solution.nbaPlayersHeights, "a string")
        self.assertRaises(TypeError, self.solution.nbaPlayersHeights, True)
        self.assertRaises(TypeError, self.solution.nbaPlayersHeights, [])
        self.assertRaises(TypeError, self.solution.nbaPlayersHeights, {})
        self.assertRaises(TypeError, self.solution.nbaPlayersHeights, set())

    def testNoMatchesFoundForTargetZero(self):
        output = StringIO()
        sys.stdout = output
        self.solution.nbaPlayersHeights(0)
        self.assertEqual(output.getvalue().strip(), "No matches found.")

    def testSampleTestCase(self):
        output = StringIO()
        sys.stdout = output
        self.solution.nbaPlayersHeights(139)
        self.assertEqual(output.getvalue().strip(), "- Nate Robinson\tBrevin Knight\n- Mike Wilks\tNate Robinson")

