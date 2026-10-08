# Rule-Based Scholarship Example
# Thresholds used here are synthetic lab assumptions.

def scholarship_decision(score, documents_complete, attendance, interview_score):
    # Original conditions
    if score < 70:
        return "Fail", "Score is below 70"

    if not documents_complete:
        return "Fail", "Documents are incomplete"

    # Additional named conditions
    if attendance < 75:
        return "Fail", "Attendance is below 75%"

    if interview_score < 60:
        return "Fail", "Interview score is below 60"

    return "Pass", "All conditions are satisfied"


# Four core test cases:
# 1. Pass
# 2. Failure of first new condition
# 3. Failure of second new condition
# 4. Threshold boundary (score exactly 70)

test_cases = [
    {
        "name": "Case 1 - Normal Pass",
        "score": 80,
        "documents_complete": True,
        "attendance": 85,
        "interview_score": 75,
        "expected": "Pass"
    },
    {
        "name": "Case 2 - Attendance Failure",
        "score": 80,
        "documents_complete": True,
        "attendance": 70,
        "interview_score": 80,
        "expected": "Fail"
    },
    {
        "name": "Case 3 - Interview Failure",
        "score": 80,
        "documents_complete": True,
        "attendance": 85,
        "interview_score": 50,
        "expected": "Fail"
    },
    {
        "name": "Case 4 - Score Boundary",
        "score": 70,
        "documents_complete": True,
        "attendance": 85,
        "interview_score": 75,
        "expected": "Pass"
    }
]

for case in test_cases:
    actual, reason = scholarship_decision(
        case["score"],
        case["documents_complete"],
        case["attendance"],
        case["interview_score"]
    )

    print("\n" + case["name"])
    print("Input:", {
        "score": case["score"],
        "documents_complete": case["documents_complete"],
        "attendance": case["attendance"],
        "interview_score": case["interview_score"]
    })
    print("Expected Result:", case["expected"])
    print("Actual Result:", actual)
    print("Reason:", reason)
