# Rock Paper Scissors

A console-based Rock Paper Scissors game written in Python.
Create a profile, get matched with a randomly generated opponent, and play a 7-round match while your wins and losses are tracked.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)

---

## Table of Contents

- [Rock Paper Scissors](#rock-paper-scissors)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Preview](#preview)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [How to Play](#how-to-play)
  - [Scoring Rules](#scoring-rules)
  - [Project Structure](#project-structure)
  - [Architecture](#architecture)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)

---

## Features

- **Player profile** with name and validated email address
- **Random opponent** with a generated name, email, and match history (powered by [Faker](https://faker.readthedocs.io/))
- **7-round matches** with a live scoreboard after every round
- **Win/loss tracking** on your profile
- **Input validation** everywhere: invalid emails, menu choices, and moves are rejected with a retry prompt
- **Quit at any time** by entering `e`
- **Clean layered code**: game rules are separated from the console UI, so the logic can be tested or reused with a different interface

## Preview

```
---------------------------------------------------
|                                                 |
|                    ROCK                         |
|                    PAPER                        |
|                    SCISSORS                     |
|                                                 |
---------------------------------------------------
```

```
---------------------------------------------------
|                                                 |
|                     Round  1                    |
|                                                 |
---------------------------------------------------
    1- Rock                                    
    2- Paper                                   
    3- Scissors                                
    (Enter the number of the desired option)   
                                                 
```

## Requirements

- Python **3.10** or newer
- Dependencies (installed via `requirements.txt`):
  - [`email-validator`](https://pypi.org/project/email-validator/): email validation
  - [`Faker`](https://pypi.org/project/Faker/): random opponent profiles

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd rock_paper_scissors
   ```
2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```
3. **Activate it**

   | Platform             | Command                       |
   | -------------------- | ----------------------------- |
   | Windows (cmd)        | `venv\Scripts\activate`     |
   | Windows (PowerShell) | `venv\Scripts\Activate.ps1` |
   | Linux / macOS        | `source venv/bin/activate`  |


   > On PowerShell, if scripts are blocked, run
   > `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and try again.
   >
4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

From the project root:

```bash
python src/main.py
```

or from inside the `src` folder:

```bash
cd src
python main.py
```

## How to Play

1. **Enter your profile**: type your name and a valid email address.
2. **Use the main menu**:
   | Key   | Action                                        |
   | ----- | --------------------------------------------- |
   | `s` | Start a game                                  |
   | `p` | Show your profile (name, email, wins, losses) |
   | `e` | Quit                                          |
3. **Meet your opponent**: the game "finds" a random opponent and shows their profile. Press `Enter` to begin.
4. **Play 7 rounds**: in each round enter:
   | Input | Move     |
   | ----- | -------- |
   | `1` | Rock     |
   | `2` | Paper    |
   | `3` | Scissors |
5. **See the result**: after round 7 the final winner is announced and your profile is updated. You then return to the main menu.

## Scoring Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- In a drawn round, both players receive a point
- After 7 rounds, the player with the higher total wins the match. Equal totals end in a draw.
- A match win increases your **Wins** by one; a match loss increases your **Losses** by one.

## Project Structure

```
rock_paper_scissors/
├── src/
│   ├── main.py              # Entry point and main menu loop
│   ├── game.py              # Game loop (play_game) and result recording
│   ├── rules.py             # Round winner, points, and overall winner
│   ├── models/
│   │   └── player.py        # Player class (name, email, wins, losses)
│   ├── services/
│   │   └── opponent.py      # Random opponent creation and move selection
│   └── ui/
│       ├── console_input.py   # Input prompts and validation
│       └── console_output.py  # All printed screens and messages
├── requirements.txt
├── .gitignore
└── README.md
```

## Architecture

The project follows a simple layered structure with a clear dependency direction:

```
main  ->  game  ->  rules
  |         |
  |         +---->  services (opponent)
  |         +---->  ui (injected as ci / co)
  +---->  models, ui, services
```

Design principles used:

- **Rules contain only logic.** They take values and return values, with no `print`, no `input`, and no side effects on players.
- **The UI is isolated.** All console input lives in `ui/console_input.py` and all output in `ui/console_output.py`. The game loop receives them as parameters, so another interface (GUI, web) could replace them without touching the rules.
- **`main` is the coordinator.** It decides what happens next (menu choices, quitting, recording results).
- **No hidden global state.** Players are created at runtime and passed explicitly.

## Roadmap

- [ ] Unit tests for `rules.py` with `pytest`
- [ ] "Play again?" prompt after each match
- [ ] Persistent profiles (save/load wins and losses to a JSON file)
- [ ] Configurable number of rounds
- [ ] Smarter computer opponent strategies
- [ ] Two-player mode
- [ ] Optional GUI or web interface

## Contributing

Contributions, issues, and suggestions are welcome.

1. Fork the repository
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push the branch: `git push origin feature/my-feature`
5. Open a Pull Request
