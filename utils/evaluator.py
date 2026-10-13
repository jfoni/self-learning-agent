
def evaluate_response(response):
    if not response or not response.strip():
        return {
            "score": 0,
            "feedback": "The response is empty."
        }

    score = 5
    feedback = []

    if len(response.split()) >= 10:
        score += 2
    else:
        feedback.append("Provide a more detailed explanation.")

    if response.strip()[-1] in ".!?":
        score += 1
    else:
        feedback.append("End the response with proper punctuation.")

    if len(response.split()) >= 20:
        score += 2

    score = min(score, 10)

    if not feedback:
        feedback.append("The response meets the basic quality checks.")

    return {
        "score": score,
        "feedback": " ".join(feedback)
    }
