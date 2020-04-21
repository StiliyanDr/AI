import sys

from eightpuzzle.astar.search import AStarSearch
from eightpuzzle.state import State


DEFAULT_GOAL = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", " "],
]


def determine_initial_and_goal_states(
    command_line_arguments
):
    if (command_line_arguments):
        initial_state_path, goal_path = \
            command_line_arguments

        return (State.from_CSV(initial_state_path),
                State.from_CSV(goal_path))
    else:
        return (State.random(),
                State.from_list(DEFAULT_GOAL))


def log_error(message):
    sys.stderr.write(f"{message}\n")


def print_states(initial, goal):
    print("Initial state:",
          initial,
          "Goal state:",
          goal,
          sep="\n")


def find_solution(initial_state, goal):
    search = AStarSearch()

    return search(initial_state, goal)


def print_solution(s):
    if (s is not None):
        _do_print_solution(s)
    else:
        print("No solution")


def _do_print_solution(s):
    print("Solution:")
    rest = _print_initial_state_from(s)

    for action, state in rest:
        _print_action_generated_state(action, state)


def _print_initial_state_from(solution):
    _, initial_state = solution.pop(0)

    print("Initial state:", initial_state, sep="\n")

    return solution


def _print_action_generated_state(action, state):
    print("\n",
          f"Action: move {action.name.lower()}",
          "New state:",
          state,
          sep="\n")


if (__name__ == "__main__"):
    command_line_args = sys.argv
    number_of_arguments = len(command_line_args)

    if (number_of_arguments in [1, 3]):
        try:
            initial_state, goal = \
                determine_initial_and_goal_states(
                    command_line_args[1:]
                )
        except Exception as e:
            log_error(str(e))
        else:
            print_states(initial_state, goal)
            s = find_solution(initial_state, goal)
            print_solution(s)
    else:
        log_error(
            "Invalid number of command line "
            f"arguments for {command_line_args[0]!r}!"
        )
