import random

def simulate_monty_hall(total_doors, simulation_iterations):
    """Simulates the Monty Hall problem.

    Args:
        total_doors: The total number of doors.
        simulation_iterations: The number of simulation runs.

    Returns:
        The winning percentage when switching doors.
    """

    num_wins_with_switch = 0

    for _ in range(simulation_iterations):
        car_door = random.randint(1, total_doors)
        initial_choice = random.randint(1, total_doors)

        if initial_choice != car_door:
            num_wins_with_switch += 1

    return (num_wins_with_switch / simulation_iterations) * 100

if __name__ == "__main__":
    total_doors = 25
    simulation_iterations = 10000

    while total_doors >= 3:
        winning_chance_on_switch = simulate_monty_hall(total_doors, simulation_iterations)
        print(f"When you have {total_doors} doors, you win {winning_chance_on_switch:.2f}% of the times if you switch the door later")
        total_doors -= 1


# Output
# When you have 25 doors, you win 96.06% of the times if you switch the door later
# When you have 24 doors, you win 95.98% of the times if you switch the door later
# When you have 23 doors, you win 95.61% of the times if you switch the door later
# When you have 22 doors, you win 95.10% of the times if you switch the door later
# When you have 21 doors, you win 95.46% of the times if you switch the door later
# When you have 20 doors, you win 95.15% of the times if you switch the door later
# When you have 19 doors, you win 94.98% of the times if you switch the door later
# When you have 18 doors, you win 94.62% of the times if you switch the door later
# When you have 17 doors, you win 94.19% of the times if you switch the door later
# When you have 16 doors, you win 94.00% of the times if you switch the door later
# When you have 15 doors, you win 93.30% of the times if you switch the door later
# When you have 14 doors, you win 93.16% of the times if you switch the door later
# When you have 13 doors, you win 92.01% of the times if you switch the door later
# When you have 12 doors, you win 91.54% of the times if you switch the door later
# When you have 11 doors, you win 90.89% of the times if you switch the door later
# When you have 10 doors, you win 89.67% of the times if you switch the door later
# When you have 9 doors, you win 88.26% of the times if you switch the door later
# When you have 8 doors, you win 87.57% of the times if you switch the door later
# When you have 7 doors, you win 86.21% of the times if you switch the door later
# When you have 6 doors, you win 83.29% of the times if you switch the door later
# When you have 5 doors, you win 79.96% of the times if you switch the door later
# When you have 4 doors, you win 75.17% of the times if you switch the door later
# When you have 3 doors, you win 67.08% of the times if you switch the door later