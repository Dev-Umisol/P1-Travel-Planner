# 📁 Travel Planner
A Python program that determines whether commuting is possible based on distance, weather, and available transport.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About

This was my first Python project, built to get hands on with conditional statements and logical operators. The program takes a set of variables: distance, weather, and transport options, and works through a decision tree to determine whether a commute is possible. Simple in scope, but a solid foundation for understanding how conditions chain together.

## 🧠 What I Learned
- **Conditional statements** — Writing `if`, `elif`, and `else` chains to handle multiple possible scenarios, and understanding the order in which Python evaluates them
- **Logical operators** — Using `and`, `or`, and `not` to combine multiple conditions in a single check (e.g. `hasBike and not isRaining`)
- **Nested conditionals** — Placing `if/else` blocks inside other `if/else` blocks to handle sub-conditions within a larger decision tree
- **Boolean variables** — Using `True/False` flags to represent real-world states like `isRaining` or `hasCar`, and understanding how they evaluate in conditions
- **Falsy values** — Using if not `distanceMi` to catch a zero or missing distance before any other checks run

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x   | Core Language |

## 💡 How It Works
The program checks distance first, then layers in weather and transport availability:
- 0 miles → not possible
- Up to 1 mile → possible if it's not raining
- 1–6 miles → possible if there's a bike and it's not raining
- 6+ miles → possible if there's a car or a rideshare app
**Example output:**
```
distanceMi = 5, isRaining = False, hasBike = True
→ True
```

## 🚀 Future Improvements
- [ ]  Accept user input at runtime instead of hardcoded variables
- [ ]  Add more transport options like public transit or walking in light rain
- [ ]  Return a suggested mode of transport rather than just True/False
- [ ]  Refactor the decision tree into a function for reusability

## 📂 Project Structure
```
travel-planner/
│
├── P1TravelPlanner.py    # Decision logic and test variables
└── README.md
```

*Part of my Python learning journey 🐍 — my first project, practising conditional statements and logical operators*
