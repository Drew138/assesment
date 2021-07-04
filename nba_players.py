import requests
from collections import defaultdict
import json


class Solution:
    def __init__(self, url="https://mach-eight.uc.r.appspot.com/"):
        dataset = requests.get(url)
        self.players = json.loads(dataset.text)["values"]

    def start(self):
        print("Enter a number to see players or any other key to exit.")
        while (action := input("Enter target height: ")).isnumeric():
            self.nbaPlayersHeights(int(action))

    def nbaPlayersHeights(self, target: int):
        """
        print combinations of players whose
        heights add up to a given target.
        """
        if type(target) != int: raise TypeError
        if target <= 0:
            print("No matches found.")
            return
        heights_map = defaultdict(list)
        answer = []
        for player in self.players:
            player_name = f'{player["first_name"]} {player["last_name"]}'
            answer += [
                f"- {player_name}\t{player_two_name}" for player_two_name in heights_map[target - int(player["h_in"])]
            ]
            heights_map[int(player["h_in"])].append(player_name)
        print("\n".join(answer))
        if not answer:
            print("No matches found.")


if __name__ == "__main__":
    solution = Solution()
    solution.start()
