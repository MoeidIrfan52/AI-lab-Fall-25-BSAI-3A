# Task 1: PEAS specifications
# 1) Delivery robot   2) LLM based student-support agent

delivery_robot = {
    "Performance": [
        "Percentage of parcels delivered to the correct place on time",
        "Number of collisions / near misses (should be zero)",
        "Battery energy used per delivery",
        "Delivery time per order",
    ],
    "Environment": [
        "University campus footpaths, corridors and lifts",
        "Pedestrians, cyclists and other moving obstacles",
        "Weather (rain, sunlight) and changing lighting",
        "Doors, ramps, stairs, road crossings",
    ],
    "Actuators": [
        "Drive wheels (speed and steering)",
        "Brakes",
        "Storage compartment lock / unlock",
        "Horn, lights and a small display for signalling people",
    ],
    "Sensors": [
        "Camera",
        "LiDAR / ultrasonic distance sensors",
        "GPS and wheel encoders (odometry), IMU",
        "Battery level sensor",
        "Touch screen / app input for the recipient's PIN",
    ],
}

delivery_tradeoff = (
    "Speed vs safety: driving faster lowers delivery time but gives less "
    "braking distance near pedestrians, so the robot slows down in crowded "
    "areas and accepts a lower on-time delivery rate."
)

delivery_assumptions = [
    "Robot works only inside a mapped campus, in daytime.",
    "Robot carries one parcel at a time.",
    "A map and the delivery address are given before the trip starts.",
    "Wi-Fi/4G is available most of the time but may drop.",
]

student_agent = {
    "Performance": [
        "Accuracy of answers (correct policy / deadline / fee information)",
        "Student satisfaction rating after the chat",
        "Percentage of queries resolved without a human",
        "Correct escalation of sensitive cases (e.g. mental health) to staff",
        "Response time",
    ],
    "Environment": [
        "Students sending text queries through a chat window",
        "University knowledge sources: FAQs, handbook, course pages",
        "University systems (timetable, LMS, fee portal)",
        "Rules about privacy and academic integrity",
    ],
    "Actuators": [
        "Text replies in the chat",
        "Creating a support ticket / forwarding to a human",
        "Sending a reminder or confirmation email",
        "Booking an advisor appointment",
    ],
    "Sensors": [
        "Student's typed message and chat history",
        "Student ID / login information",
        "Results returned by the tools (search results, database rows)",
        "Feedback buttons (thumbs up / down)",
    ],
}

student_tools = [
    "Search over the university handbook and FAQ (read only)",
    "Timetable / course catalogue lookup (read only)",
    "Fee and registration status lookup (only for the logged-in student)",
    "Ticket creation and appointment booking",
    "Email sender (templates only)",
]

student_tradeoff = (
    "Helpfulness vs safety/accuracy: if the agent always answers, it will "
    "sometimes invent a wrong policy (hallucination). If it escalates every "
    "doubtful query, it is safer but resolves fewer queries on its own "
    "and staff workload goes up."
)

student_assumptions = [
    "Agent can only use the tools listed above; it cannot change grades or payments.",
    "Student is authenticated before personal data is shown.",
    "Knowledge base is updated every semester.",
    "Any write action (ticket, booking) is logged and can be reviewed.",
]


def show(title, peas, tradeoff, assumptions, tools=None):
    print("=" * 60)
    print(title)
    print("=" * 60)
    for key, items in peas.items():
        print(key + ":")
        for it in items:
            print("   -", it)
    print("Trade-off:", tradeoff)
    print("Assumptions:")
    for a in assumptions:
        print("   -", a)
    if tools:
        print("Tools the agent can access:")
        for t in tools:
            print("   -", t)
    print()


if __name__ == "__main__":
    show("PEAS: DELIVERY ROBOT", delivery_robot, delivery_tradeoff, delivery_assumptions)
    show("PEAS: LLM STUDENT-SUPPORT AGENT", student_agent, student_tradeoff,
         student_assumptions, student_tools)
