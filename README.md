# Rock Paper Scissors

A console-based Rock Paper Scissors game written in Python.
Create a profile, get matched with a randomly generated opponent, and play 7-round matches as many times as you like while your wins and losses are tracked.

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
  - [Known Limitations](#known-limitations)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)

---

## Features

- **Player profile** with a name and a validated email address
- **Random opponent**: every match is played against a newly generated opponent with a random name, email, and win/loss history (powered by [Faker](https://faker.readthedocs.io/))
- **7-round matches** with a live scoreboard after every round
- **Unlimited matches**: after each match you return to the main menu and can play again until you quit
- **Win/loss tracking** on your profile (kept in memory for the current session)
- **Input validation**: invalid emails, menu choices, and moves are rejected with a retry prompt
- **Separated UI**: all `input()` and `print()` calls live in the `ui` package, away from the game rules

## Preview

Title screen:

```
---------------------------------------------------
|                                                 |
|                    ROCK                         |
|                    PAPER                        |
|                    SCISSORS                     |
|                                                 |
---------------------------------------------------
```

A round:

```
---------------------------------------------------
|                                                 |
|                     Round  1                    |
|                                                 |
---------------------------------------------------
|    1- Rock                                      |
|    2- Paper                                     |
|    3- scissors                                  |
|    (Enter the number of the desired option)     |
|                                                 |
     your choice : 2
|    computer input :  1                          |
|    Result :                                     |
|    Computer :  0                                |
|    User :  1                                    |
---------------------------------------------------
```

The computer's move is shown as a number (`1` = Rock, `2` = Paper, `3` = Scissors).

## Requirements

- Python **3.10** or newer
- Dependencies (installed via `requirements.txt`):
  - [`email-validator`](https://pypi.org/project/email-validator/): email validation
  - [`Faker`](https://pypi.org/project/Faker/): random opponent profiles
  - Their own sub-dependencies (`dnspython`, `idna`, `tzdata`) are installed automatically

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

   | Platform             | Command                     |
   | -------------------- | --------------------------- |
   | Windows (cmd)        | `venv\Scripts\activate`     |
   | Windows (PowerShell) | `venv\Scripts\Activate.ps1` |
   | Linux / macOS        | `source venv/bin/activate`  |

   > On PowerShell, if scripts are blocked, run
   > `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and try again.

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

   | Key | Action                                        |
   | --- | --------------------------------------------- |
   | `s` | Start a game                                  |
   | `p` | Show your profile (name, email, wins, losses) |
   | `e` | Quit                                          |

3. **Meet your opponent**: the game "finds" a random opponent and shows their profile. Read the game rules, then press `Enter` to begin (or `e` to quit).
4. **Play 7 rounds**: in each round enter:

   | Input | Move     |
   | ----- | -------- |
   | `1`   | Rock     |
   | `2`   | Paper    |
   | `3`   | Scissors |

5. **See the result**: after round 7 the final winner is announced and your profile is updated.
6. **Play again or quit**: you return to the main menu. The game loop has no limit, so you can play as many matches as you want and leave with `e` whenever the menu is shown.

## Scoring Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- In a drawn round, **both** players receive a point
- After 7 rounds, the player with the higher total wins the match. Equal totals end in a draw.
- A match win increases your **Wins** by one, a match loss increases your **Losses** by one, and a draw changes nothing.
- The opponent's win/loss numbers are only part of its randomly generated profile. They are not updated, because a new opponent is created for every match.

## Project Structure

```
rock_paper_scissors/
├── src/
│   ├── main.py              # Entry point: profile setup and the endless menu/game loop
│   ├── game.py              # play_game: runs the 7 rounds and returns the result
│   ├── rules.py             # Round winner, round points, and final result
│   ├── models/
│   │   └── player.py        # Player class (name, email, wins, losses)
│   ├── services/
│   │   └── opponent.py      # Random opponent creation and random move selection
│   └── ui/
│       ├── console_input.py   # Input prompts and validation
│       └── console_output.py  # All printed screens and messages
├── requirements.txt
├── .gitignore
└── README.md
```

## Architecture

The code is organized in layers, and `main.py` is the only place that ties everything together:

```
main  ->  ui (console_input, console_output)
main  ->  models (Player)
main  ->  services (opponent)
main  ->  game  ->  rules
                ->  services (opponent move)
                ->  ui (passed in as ci / co)
```

Design decisions:

- **UI isolation.** Every `input()` and `print()` is inside the `ui` package. `rules.py` contains no input or output, and `play_game` receives the UI modules as parameters (`ci`, `co`) instead of importing them.
- **`main` is the coordinator.** It builds the menu flow, creates the players, and decides when the program exits.
- **Endless game loop.** The program is intentionally an infinite loop: the menu is shown again after every match, and the only way out is choosing `e`.
- **Fresh opponent per match.** The computer player is regenerated for every game, so its record is never tracked.
- **User profile created at startup.** The `Player` object for the user is created once, empty, and then filled in with `change_name` and `change_email` after the user enters their information.

## Known Limitations

- The final match result is recorded inside `rules.overall_winner`, which calls the user's `add_win` / `add_loss` through functions passed down from `main`. This is the one place where the rules module has a side effect on a player.
- Profiles are not saved: wins and losses are lost when the program closes.
- There are no automated tests yet.

## Roadmap

- [ ] Make `rules.py` side-effect free (return only `"user"`, `"computer"`, or `"draw"`) and record the result in `main`
- [ ] Unit tests for `rules.py` with `pytest`
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