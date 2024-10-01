# Blackjack Dealer Simulation

## Overview

The Blackjack Dealer Simulation is a Python program that simulates the actions of a Blackjack dealer. The dealer draws cards randomly from a deck and continues to draw until reaching a hand value of 17 or higher. The simulation handles the values of aces and checks for Blackjack or bust conditions, providing an interactive way to understand the dealer's behavior in the game.

## Features

- **Card Drawing**: The dealer draws cards randomly from a standard deck until the hand value is at least 17.
- **Ace Handling**: Aces are counted as either 11 or 1, depending on the current hand value.
- **Blackjack Evaluation**: The program checks if the dealer achieves a Blackjack (21 with two cards) or busts (exceeds 21).

## Requirements

- Python 3.x
- `Cards` module: A custom implementation required to handle card suits, ranks, and values.
- `random` and `time` standard Python libraries

## How to Use

1. Clone or download this repository.
2. Ensure you have the `Cards.py` module in the same directory.
3. Run the script using Python:

    ```sh
    python blackjack_dealer_simulation.py
    ```

4. Observe the dealer's card draws and final hand value in the console.

## Functions

### `main()`
Controls the main flow of the simulation.

- **Outputs**: Displays the dealer's hand value and checks for Blackjack or bust conditions.

### `distance(x1, y1, x2, y2)`
Calculates the distance between two points using the distance formula.

- **Inputs**: `x1`, `y1` (coordinates of the first point), `x2`, `y2` (coordinates of the second point)
- **Outputs**: `dist` (distance between the two points)

### `circle(x, y, color)`
Creates a circle object with a given position and color.

- **Inputs**: `x`, `y` (coordinates of the circle center), `color` (color of the circle)
- **Outputs**: `c` (circle object)

### `movement(x, y, window, color)`
Moves the circle to a new random position within a specified range.

- **Inputs**: `x`, `y` (coordinates of the current circle position), `window` (graphics window object), `color` (color of the circle)
- **Outputs**: `x`, `y` (new coordinates of the circle)

## Game Flow

1. **Initialization**: Sets up the deck and initial values.
2. **Card Drawing**: The dealer draws cards until reaching a hand value of 17 or higher.
3. **Win or Lose**:
   - If the dealer achieves Blackjack, a message is displayed.
   - If the dealer busts, a message is displayed with the final hand value.

## Future Improvements

- **Enhanced Dealer Strategy**: Implement more complex strategies for card drawing based on additional rules.
- **User Interaction**: Allow users to play against the dealer for a more interactive experience.
- **Graphical User Interface**: Develop a GUI for a more engaging simulation experience.

## License

This project is open source and available.

---

**Author**: Alexander Harshman
