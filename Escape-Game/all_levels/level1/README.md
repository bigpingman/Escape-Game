# Level 1

A puzzle where the player must match certain cards with other cards on a board. We will use a 2D array to populate the board with “cards” laying face down. Each card has an identical pair. The player must flip over two cards at a time trying to find pairs. If the cards that the player chose are not a pair, they are flipped back over, and the player must select another pair of cards. If the cards that the player chose are a pair, the cards remain face-up, and the player must continue
searching for other pairs. The task is completed successfully if the player finds all the pairs in the given time limit. If the player fails to do so in the given time limit for the matching game, the overall time limit is reduced by x seconds.

## Quick Start

`python match.py`
