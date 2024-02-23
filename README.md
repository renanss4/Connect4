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

### With Pygame (Optional)

1. **Virtual Environment:** If you intend to run the game with Pygame, it is recommended to create a virtual environment. To do this, execute:

   ```bash
   python -m venv venv
   ```

   1.a. Then, activate the virtual environment:

   - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

   - On Linux/Mac:

      ```bash
      source venv/bin/activate
      ```

2. **Install requirements.txt:** Don't forget to install the requirements listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project:** After setting up the environment and installing the necessary dependencies, execute this command to start the project.

   ```bash
   python pygameMain.py
   ```

### Without Pygame

1. **Execution without Pygame:** If you are not using Pygame, you can run the project normally without the need for a virtual environment.

   ```bash
   python Main.py
   ```

## Contributing

Contributions are welcome! If you find bugs, issues, or have suggestions to improve the game, feel free to open an issue or submit a pull request. Below are some ways you can contribute:

### Create a Fork

1. Fork the project by clicking on the "Fork" button at the top right of this page. This will create a copy of the repository in your account.

### Clone the Repository

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/your-username/your-repository.git
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repository
   ```

### Create a New Branch

1. Create a new branch to work on:
   ```sh
   git checkout -b my-contribution
   ```

### Make Changes

1. Make desired changes in the code.

### Commit and Push

1. Commit your changes:
   ```sh
   git commit -am 'Adding a new feature'
   ```
2. Push your changes to GitHub:
   ```sh
   git push origin my-contribution
   ```

### Send a Pull Request

1. Navigate to your fork's page on GitHub.
2. Click on the "New Pull Request" button.
3. Describe your changes and click "Create Pull Request".

Once your Pull Request is reviewed, it can be merged into the main project.

Thank you for contributing!

## Running Tests

>  **I'm still learning about testing, so this section is deprecated. I will fix it in the future.**

### With Pytest

If you prefer to run the project with the interface, and have installed the project dependencies, you can execute the tests with the commands below.

To run the tests, use the following command:

```bash
python  -m  pytest  -v  tests/
```

or

```bash
python  -m  pytest  tests/
```

### Without Pytest

Otherwise, if you haven't installed any dependencies, you can run the tests as follows:

If you want to test file by file, use the command below:

```bash
# Example
python  test_math_operations.py
```

Or if you want to test all at once, use the command below:

```bash
python  -m  unittest  discover
```

## Future Improvements

- Implement Pygame features for a more interactive experience.
- Improve code organization and add more comments.
- Add automated tests.

## Note

> Perhaps, on Ubuntu it may be necessary to run the commands with `python3`. Don't forget to execute commands such as creating the virtual environment and running the project within the project directory.

## License

This project is licensed under the  [MIT License](LICENSE.md), which means you have complete freedom to use it as you prefer. Enjoy playing and contributing!
