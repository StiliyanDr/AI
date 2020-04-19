import sys

from eightpuzzle.astar.search import AStarSearch
from eightpuzzle.state import State


def find_solution(initial_state_path, goal_path):
    initial_state = State.from_CSV(initial_state_path)
    goal = State.from_CSV(goal_path)
    search = AStarSearch()

    return search(initial_state, goal)


def print_solution(s):
    if (s is not None):
        _do_print_solution(s)
    else:
        print("There is no solution!")


def _do_print_solution(s):
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


def log_error(message):
    sys.stderr.write(f"{message}\n")


if (__name__ == "__main__"):
    if (len(sys.argv) == 3):
        try:
            s = find_solution(
                initial_state_path=sys.argv[1],
                goal_path=sys.argv[2]
            )
        except Exception as e:
            log_error(str(e))
        else:
            print_solution(s)
    else:
        log_error(
            "Expected paths for initial and goal states!"
        )
