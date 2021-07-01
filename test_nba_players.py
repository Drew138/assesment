import unittest
from nba_players import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testSolutionRaisesExceptionOnNoNNumericTargets(self):
        """
        test whether nbaPlayersHeights function 
        raises type erros on non numeric target 
        arguments.
        """

        self.assertRaises(
            TypeError, self.solution.nbaPlayersHeights, "a string")
        self.assertRaises(TypeError, self.solution.nbaPlayersHeights, True)
        self.assertRaises(TypeError, self.solution.nbaPlayersHeights, [])
        self.assertRaises(TypeError, self.solution.nbaPlayersHeights, {})
        self.assertRaises(TypeError, self.solution.nbaPlayersHeights, set())
