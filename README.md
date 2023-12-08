# Connect Four

This project implements the Connect Four game in Python, utilizing the resources available in the language.

## How to Play

Connect Four is a classic game in which two players take turns trying to form a line of four consecutive pieces of the same color, whether horizontally, vertically, or diagonally. The board consists of seven columns and six rows, and players choose in which column to place their piece.

To play:

1. Execute the file `Main.py`.
2. Follow the instructions to configure the number of players.
3. During the game, players will take turns, and each will make their move by choosing the desired column.

## UML Diagram

![UML Diagram](/UML_Connect4.png)

The UML diagram presents the structure of the project's classes, highlighting the relationship between them.

## Environment Setup

1. **Virtual Environment (Optional for Pygame):** 

If you intend to run the game with Pygame, it is recommended to create a virtual environment. To do this, execute:

```bash
python -m venv venv
```

Then, activate the virtual environment:


- On Windows:

```bash
.\venv\Scripts\activate
```

- On Linux/Mac:

```bash
source venv/bin/activate
```

2. **Execution without Pygame:**

If you are not using Pygame, you can run the project normally without the need for a virtual environment.

```bash
python Main.py
```

## Contributions

Contributions are welcome! If you find bugs, issues, or have suggestions to improve the game, feel free to open an issue or submit a pull request.

## Future Improvements

- Implement Pygame features for a more interactive experience.
- Improve code organization and add more comments.
- Add automated tests.

## Running Tests

To run the tests, use the following command:

```bash
python -m pytest -v test/
```

or

```bash
python -m pytest test/
```

## License

This project is licensed under the  [MIT License](LICENSE.md), which means you have complete freedom to use it as you prefer. Enjoy playing and contributing!
