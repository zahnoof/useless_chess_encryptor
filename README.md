# The Useless Chess Encryptor

This project is a unique and creative take on data encryption. It's a Python-based application that uses a custom-built chess game to "encrypt" text into a series of chess moves. The application then "decrypts" the game by reading the moves made on the board and converting them back into the original text.

## Core Concept

The core idea is to demonstrate a "useless" but fully functional encryption process. Each move made on the chessboard corresponds to a single bit of data (a move to a white square represents a `1`, and a move to a black square represents a `0`). The entire game becomes the encrypted data stream.

## Features

- **Interactive UI:** A graphical interface built with `pygame` that includes an interactive start screen, a text input bar, and buttons to control the game.
- **Data-Driven Bots:** Two bots that play a game based on the binary stream of your input text.
- **Robust Gameplay:** The chess engine includes move validation for all pieces and correctly handles game-over conditions like checkmate.
- **Persistent History:** The application can save your gameplay history to a JSON file, and you can view it on a separate history page.
- **Game Replay:** You can select a saved game from the history and watch it replay on the chessboard.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [your_repository_url]
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd useless_chess_project
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  **Install the required libraries:**
    ```bash
    pip install pygame
    ```
5.  **Run the application:**
    ```bash
    .\venv\Scripts\python.exe main.py
    ```

## Technologies Used

* **Python:** The core programming language.
* **Pygame:** For building the graphical user interface and game engine.
* **JSON:** For storing and retrieving game history.


# The Useless Chess Encryptor

This project is a Python application that uses a custom-built chess game to "encrypt" text into a series of chess moves. The application then "decrypts" the game by reading the moves made on the board and converting them back into the original text.

## How to Run the Project

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.10 or higher
* `pip` (Python package installer)

### Step 1: Clone the Repository

First, you need to get a copy of the project's code. Open your terminal or command prompt and run the following command, replacing `[your_repository_url]` with the actual URL of your GitHub repository.

```bash
git clone [your_repository_url]

Step 2: Navigate to the Project Directory
Move into the newly cloned project folder.

Bash

cd useless_chess_project
Step 3: Create and Activate a Virtual Environment
It's a best practice to use a virtual environment to manage project dependencies. This prevents conflicts with other Python projects on your machine.

On Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
On macOS and Linux:

Bash

python3 -m venv venv
source venv/bin/activate
Step 4: Install Dependencies
With the virtual environment activated, install the pygame library using pip.

Bash

pip install pygame
Step 5: Run the Application
Finally, run the main Python script to start the application.

Bash

python main.py
You should now see the application's start screen, and you can begin using your Useless Chess Encryptor!
