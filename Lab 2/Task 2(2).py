# Task 2: Classify the environments of both systems
# Dimensions: observable (fully / partially) and deterministic / stochastic

classification = {
    "Delivery robot": {
        "observable": "Partially observable",
        "observable_why": "Sensors have limited range and can be blocked by objects.",
        "observable_example": {
            "observable": "Distance to the nearest obstacle from LiDAR",
            "hidden": "A pedestrian walking behind a corner; whether the door ahead will open",
        },
        "deterministic": "Stochastic",
        "deterministic_why": "People move randomly and wheels slip, so the next state is not fixed.",
        "outcome_example": {
            "predictable": "Command 'lock compartment' always locks it",
            "uncertain": "'Move forward 1 m' may end at a different place because of wheel slip or a person stepping in front",
        },
    },
    "LLM student-support agent": {
        "observable": "Partially observable",
        "observable_why": "Agent sees only the typed text and tool results, not the student's real situation.",
        "observable_example": {
            "observable": "The student's message and the timetable returned by the tool",
            "hidden": "Whether the student is stressed, or if they gave wrong details",
        },
        "deterministic": "Stochastic",
        "deterministic_why": "Student replies are unpredictable and the LLM can give different wording each time.",
        "outcome_example": {
            "predictable": "Calling create_ticket() adds one ticket in the system",
            "uncertain": "Whether the student understands or follows the answer; whether the LLM answer is correct",
        },
    },
}

simulator_note = {
    "Delivery robot": (
        "Real environment: partially observable and stochastic. "
        "A simple grid simulator with a known map, no moving people and "
        "perfect sensors would be fully observable and deterministic. "
        "This is only true if we assume no noise and no moving obstacles."
    ),
    "LLM student-support agent": (
        "Real environment: partially observable and stochastic. "
        "A simulator using a fixed list of questions with a fixed answer "
        "sheet and the tools returning the same data every time can be "
        "treated as fully observable and deterministic (if we set the LLM "
        "temperature to 0). This is only an approximation."
    ),
}


def report():
    for name, c in classification.items():
        print("=" * 60)
        print(name)
        print("=" * 60)
        print("Observability :", c["observable"])
        print("  Why         :", c["observable_why"])
        print("  Observable  :", c["observable_example"]["observable"])
        print("  Hidden      :", c["observable_example"]["hidden"])
        print("Determinism   :", c["deterministic"])
        print("  Why         :", c["deterministic_why"])
        print("  Predictable :", c["outcome_example"]["predictable"])
        print("  Uncertain   :", c["outcome_example"]["uncertain"])
        print("Real vs simulator:", simulator_note[name])
        print()


if __name__ == "__main__":
    report()
