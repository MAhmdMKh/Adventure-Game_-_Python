# Adventure Game (Python)
My first Python project, written when I knew only the basics. You read a
short story, choose between options, and the final score decides if you win.

## How to run
Install Python 3, then run:
    python adventure_game.py

## What I practiced
- Functions with parameters and return values
- Small functions that each do one job (`add_points`, `show_result`)
- Loops (`while`) and conditions (`if / elif / else`)
- Lists and strings (f-strings, `split`)
- The `random` and `time` modules
- The `global` keyword

## Story map
```
story_beginning (2 options)
├─ 1 → the_sunny_road (+1, 3 options)
│     ├─ 1 → listen_to_advice (+2, 3 options)
│     │     ├─ 1 → swim_across      (+1)  final 9   lose
│     │     ├─ 2 → build_a_raft     (+2)  final 10  WIN
│     │     └─ 3 → jump_on_stones   (+1)  final 9   lose
│     ├─ 2 → ask_for_help           (+2)  final 8   lose
│     └─ 3 → cross_alone            (+1)  final 7   lose
└─ 2 → the_dark_road (+2, 2 options)
      ├─ 1 → tell_the_truth         (+3)  final 10  WIN
      └─ 2 → run_away               (+2)  final 9   lose
```

## What I would improve
- Use a dictionary instead of my `add_random_list` helper to remember random choices.
