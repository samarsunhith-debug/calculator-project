# Submission Note – Project 01: Interactive Calculator & Unit Converter

**File:** `calculator.py` (Python 3.10+, no external libraries)

## What I built
A menu-driven CLI program that repeats until the user picks Quit. Main menu:
1 Add, 2 Subtract, 3 Multiply, 4 Divide, 5 Convert units, 6 Quit.

## Conversions added (6 total, in a submenu)
1. Kilometres to miles
2. Miles to kilometres
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius
5. Kilograms to pounds
6. Pounds to kilograms

All factors (km/miles 0.621371, kg/pounds 2.20462) are stored in a single
`CONVERSION_FACTORS` dictionary at the top of the file. Temperature uses the
formulas C x 9/5 + 32 and (F - 32) x 5/9.

## Input validation
- `read_number()` loops with try/except ValueError until a valid number is given.
  It also rejects empty input and `nan`/`inf`.
- `read_choice()` loops until a valid menu option is typed.
- `divide()` returns a clear message instead of crashing on division by zero.
- `eval()` is never used.

## Testing (more than six inputs, see sample_run.txt)
| Input | Result |
|---|---|
| Letters ("abc", "hello") as a menu choice / number | Friendly error, asks again |
| Empty input | "Input cannot be empty", asks again |
| Invalid menu option (9) | "Invalid choice", asks again |
| 7 + 5 | 12.0 |
| 10 / 4 | 2.5 |
| 10 / 0 | "Error: cannot divide by zero." |
| Negative number (-40 C to F) | -40.0 °F |
| 100 C to F | 212.0 °F |
| 42 km to miles | 26.0976 miles |
| 10 kg to pounds | 22.0462 pounds |

## Files
- `calculator.py` – the program
- `sample_run.txt` – output of a sample run

