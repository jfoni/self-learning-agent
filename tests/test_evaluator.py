
from utils.evaluator import evaluate_response


def test_empty_response():
    result = evaluate_response("")

    assert result["score"] == 0
    assert result["feedback"] == "The response is empty."


def test_short_response():
    result = evaluate_response("Hello there")

    assert result["score"] == 5
    assert "more detailed" in result["feedback"]


def test_detailed_response():
    response = (
        "A Python loop repeats a block of code "
        "while a condition is true. It helps automate "
        "repetitive tasks and reduces duplicated code."
    )

    result = evaluate_response(response)

    assert result["score"] == 10
