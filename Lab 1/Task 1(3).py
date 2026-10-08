# Conversational Test vs General Intelligence
# Scholarship case comparison

def scholarship_case_response(score, documents_complete, attendance, interview_score):
    if score >= 70 and documents_complete and attendance >= 75 and interview_score >= 60:
        return "The applicant passes the scholarship rules."
    return "The applicant does not pass the scholarship rules."


print("CONVERSATIONAL TEST VS GENERAL INTELLIGENCE")
print("=" * 60)

print("\nWhat a conversational test observes:")
print("It observes whether a system can produce responses that appear human-like in conversation.")

print("\nWhat it does not establish:")
print("A fluent conversation alone does not prove reliable reasoning, factual accuracy, learning ability, or performance across different tasks.")

print("\nScholarship example:")
print("A system may explain a scholarship decision fluently, but it can still make an incorrect calculation or apply a rule incorrectly.")

print("\nAdditional reliable-performance test:")
print("Repeat the scholarship task with many unseen cases and compare the system's decisions with a verified answer key.")
