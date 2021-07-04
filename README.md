
# Instructions For Use

1. Create a new virtual environment by running `python3 -m venv ./env`.
2. Run `source ./env/bin/activate` to activate the virtual environment.
3. Install required libraries by running `pip3 install -r requirements.txt`.
4. Run `python3 nba_players.py` to run the script or alternatively `python3 -m unittest` to run tests.

# Algorithm Explaination

1. Create a map where keys represent players heights, and values are the players whose heights correspond to that key. In addition, we create a list that will hold our answers.
2. Iterate over the list of players. For each player, search the list of players in the map whose height added with the initial player's height equals our target. For each of these players, add a row to our answer.
3. Print each entry in our list of answers, separated by a linebreak.
4. Incase there are no entries in the answer list, print an informative message.
