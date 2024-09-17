# Garbage Invader Game

A fun, eco-themed space invader style game built with Python and Pygame! Take control of a recycling bin character and defend the ocean from falling trash by shooting down garbage-throwing enemies.

## Game Features

- **Classic Space Invader Gameplay**: Move left and right while shooting at enemies
- **Environmental Theme**: Play as a recycling bin defending the ocean from pollution
- **Multiple Waves**: Face increasingly difficult waves of trash can enemies
- **Power-ups**: Collect red power-ups to increase your movement speed
- **Scoring System**: Earn points for hitting enemies and trash, with accuracy tracking
- **Lives System**: Lose lives when trash hits the water - game over after 3 strikes
- **Day/Night Mode**: Toggle between day and night backgrounds
- **Beautiful Graphics**: Hand-drawn scenery with ocean, beach, trees, and animated waves

## Controls

- **Left/Right Arrow Keys**: Move your recycling bin character
- **Spacebar**: Shoot at enemies and falling trash
- **Mouse**: Navigate menus and select options

## Installation and Setup

### Prerequisites
- Python 3.6 or higher installed on your system

### Setting up the Environment

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd garbageInvader
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the game**
   ```bash
   python game.py
   ```

### Deactivating the Virtual Environment

When you're done playing, you can deactivate the virtual environment:
```bash
deactivate
```

## How to Play

1. **Start the Game**: Click "START" on the main menu
2. **Move and Shoot**: Use arrow keys to move and spacebar to shoot
3. **Defend the Ocean**: Prevent trash from hitting the water by shooting it down
4. **Defeat Enemies**: Destroy all trash can enemies to advance to the next wave
5. **Collect Power-ups**: Grab red power-ups to move faster
6. **Survive**: You have 3 lives - don't let too much trash reach the ocean!

## Game Instructions

- **Objective**: Eliminate all trash can enemies while preventing trash from polluting the ocean
- **Scoring**: 
  - 20 points for destroying an enemy
  - 5 points for shooting down falling trash
- **Lives**: You lose a life each time trash hits the water
- **Waves**: Complete Wave 1 to unlock the more challenging Wave 2
- **Power-ups**: Speed boost power-ups occasionally drop from enemies

## Development Info

- **Developer**: Raj Hira
- **Course**: ICS3U1-01 Final Summative
- **Date**: June 7th, 2021
- **Language**: Python
- **Framework**: Pygame

Enjoy saving the ocean, one piece of trash at a time! 🌊♻️

