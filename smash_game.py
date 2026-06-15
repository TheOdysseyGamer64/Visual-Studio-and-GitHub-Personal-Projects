"""
Super Smash Bros Ultimate - Python Edition
A text-based fighting game where players choose characters and execute moves.
Uses selection, iteration, and sequences as programming constructs.
"""

import random
import time

# Define character movesets as sequences
MOVESETS = {
    "Cloud": {
        "neutral": "Slash (5 damage)",
        "side": "Limit Break Cross Slash (15 damage)",
        "up": "Climhazzard (8 damage)",
        "down": "Limit Break Final Heaven (20 damage)"
    },
    "Mii Swordfighter": {
        "neutral": "Jab Combo (4 damage)",
        "side": "Blade Counter (12 damage)",
        "up": "Rising Slash (7 damage)",
        "down": "Neutral Special (10 damage)"
    },
    "Mario": {
        "neutral": "Fireball (6 damage)",
        "side": "Cape Spin (8 damage)",
        "up": "Super Jump Punch (9 damage)",
        "down": "F.L.U.D.D (11 damage)"
    },
    "Sora": {
        "neutral": "Keyblade Slash (5 damage)",
        "side": "Sonic Blade (13 damage)",
        "up": "Spiral Slice (8 damage)",
        "down": "Sealing Spell (16 damage)"
    }
}

# Character stats as sequences
CHARACTERS = {
    "Cloud": {"hp": 100, "attack_speed": 0.8, "description": "A mercenary with powerful limit break abilities"},
    "Mii Swordfighter": {"hp": 85, "attack_speed": 1.0, "description": "A customizable fighter with balanced stats"},
    "Mario": {"hp": 90, "attack_speed": 0.9, "description": "The classic hero with fire-based attacks"},
    "Sora": {"hp": 95, "attack_speed": 0.95, "description": "A keyblade master with magical abilities"}
}

# Move direction options
MOVE_OPTIONS = {
    "1": "neutral",
    "2": "side",
    "3": "up",
    "4": "down"
}


def display_title():
    """Display the game title and instructions."""
    print("\n" + "="*60)
    print("     SUPER SMASH BROS ULTIMATE - PYTHON EDITION")
    print("="*60)
    print("Welcome to the ultimate fighting experience!")
    print("Choose your fighter and battle for victory!\n")


def display_characters():
    """Display all available characters using iteration."""
    print("--- SELECT YOUR CHARACTER ---")
    print("Available Fighters:\n")
    
    # Iterate through character options
    for index, (character_name, stats) in enumerate(CHARACTERS.items(), 1):
        print("{index}. {character_name}")
        print("   HP: {stats['hp']} | Attack Speed: {stats['attack_speed']}")
        print("   {stats['description']}\n")


def select_character():
    """Selection construct: Player chooses their character."""
    valid_choices = ["1", "2", "3", "4"]
    character_list = list(CHARACTERS.keys())
    
    while True:  # Iteration construct
        display_characters()
        choice = input("Enter the number of your fighter (1-4): ").strip()
        
        if choice in valid_choices:
            selected_character = character_list[int(choice) - 1]
            print(f"\n✓ You selected {selected_character}!")
            return selected_character
        else:
            print("\n✗ Invalid choice! Please enter 1-4.\n")


def display_moves(character):
    """Display available moves for a character using iteration."""
    print(f"\n--- {character.upper()}'S MOVESET ---")
    print("Choose your move:")
    print("1. Neutral Special (Fast, Low Damage)")
    print("2. Side Special (Medium Speed, Medium Damage)")
    print("3. Up Special (Medium Speed, Medium Damage)")
    print("4. Down Special (Slow, High Damage)\n")


def select_move(character):
    """Selection construct: Player selects a move."""
    valid_moves = ["1", "2", "3", "4"]
    
    while True:  # Iteration construct
        display_moves(character)
        choice = input("Choose your move (1-4): ").strip()
        
        if choice in valid_moves:
            direction = MOVE_OPTIONS[choice]
            move_info = MOVESETS[character][direction]
            
            # Extract damage value from move info string
            damage = int(move_info.split("(")[1].split()[0])
            
            return direction, move_info, damage
        else:
            print("✗ Invalid move! Please select 1-4.\n")


def battle_round(player_character, player_hp, enemy_character, enemy_hp, round_num):
    """Execute one round of battle with sequence and selection constructs."""
    print(f"\n{'='*60}")
    print(f"ROUND {round_num}")
    print(f"{'='*60}")
    print(f"Your HP: {player_hp} | Enemy HP: {enemy_hp}\n")
    
    # Player's turn
    print(f"Your turn! Playing as {player_character}")
    _, player_move, player_damage = select_move(player_character)
    
    print(f"\n→ You used: {player_move}")
    
    # Enemy's turn (random selection)
    enemy_move_direction = random.choice(list(MOVESETS[enemy_character].keys()))
    enemy_move_info = MOVESETS[enemy_character][enemy_move_direction]
    enemy_damage = int(enemy_move_info.split("(")[1].split()[0])
    
    print(f"→ Enemy used: {enemy_move_info}")
    
    # Determine hit chance (80%)
    time.sleep(1)
    player_hits = random.random() < 0.8
    enemy_hits = random.random() < 0.8
    
    # Apply damage sequence
    if player_hits:
        enemy_hp -= player_damage
        print(f"✓ Hit! Dealt {player_damage} damage!")
    else:
        print("✗ Missed!")
    
    time.sleep(0.5)
    
    if enemy_hits:
        player_hp -= enemy_damage
        print(f"✗ Enemy hit! Took {enemy_damage} damage!")
    else:
        print("✓ Enemy missed!")
    
    # Ensure HP doesn't go below 0
    player_hp = max(0, player_hp)
    enemy_hp = max(0, enemy_hp)
    
    return player_hp, enemy_hp


def get_enemy_character(player_choice):
    """Selection construct: Pick an opponent different from player choice."""
    available_opponents = [char for char in CHARACTERS.keys() if char != player_choice]
    opponent = random.choice(available_opponents)
    print(f"\n→ You face {opponent}!")
    return opponent


def play_battle(player_character):
    """Main battle loop using iteration and selection."""
    enemy_character = get_enemy_character(player_character)
    
    # Initialize HP using sequence values from CHARACTERS
    player_hp = CHARACTERS[player_character]["hp"]
    enemy_hp = CHARACTERS[enemy_character]["hp"]
    
    round_num = 1
    max_rounds = 15
    
    # Battle iteration loop
    while player_hp > 0 and enemy_hp > 0 and round_num <= max_rounds:
        player_hp, enemy_hp = battle_round(player_character, player_hp, 
                                           enemy_character, enemy_hp, round_num)
        round_num += 1
        
        if player_hp > 0 and enemy_hp > 0:
            input("\nPress ENTER to continue to next round...")
    
    # Determine and display battle result
    print(f"\n{'='*60}")
    print("BATTLE OVER!")
    print(f"{'='*60}\n")
    
    if player_hp > 0 and enemy_hp <= 0:
        print(f"🏆 VICTORY! {player_character} wins!")
        print(f"Remaining HP: {player_hp}\n")
        return True
    elif enemy_hp > 0 and player_hp <= 0:
        print(f"💀 DEFEAT! {enemy_character} wins!")
        print(f"Enemy Remaining HP: {enemy_hp}\n")
        return False
    else:
        print("⚔️ DRAW! Both fighters fall!")
        return None


def play_again():
    """Selection construct: Ask if player wants to play again."""
    while True:  # Iteration construct
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.\n")


def main():
    """Main game loop using iteration and selection."""
    display_title()
    
    # Main game iteration loop
    while True:  # Iteration construct
        player_character = select_character()
        
        print(f"\nCharacter Selected: {player_character}")
        print(f"Description: {CHARACTERS[player_character]['description']}")
        print(f"Starting HP: {CHARACTERS[player_character]['hp']}\n")
        
        input("Press ENTER to begin battle...")
        
        # Play battle and store result
        victory = play_battle(player_character)
        
        # Display battle result
        if victory is True:
            print("Congratulations! You've achieved victory!")
        elif victory is False:
            print("Train harder and try again!")
        else:
            print("A worthy opponent!")
        
        # Selection: Ask to play again
        if not play_again():
            print("\n" + "="*60)
            print("Thanks for playing Super Smash Bros Ultimate - Python Edition!")
            print("="*60 + "\n")
            break


if __name__ == "__main__":
    main()
