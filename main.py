import random


def generate_answer_key():
    return {i + 1: random.choice(["A", "B", "C", "D"]) for i in range(60)}


def generate_response(attempt_no, answers, correct_percent=100):
    response = {}
    for answer in answers:
        attempt_no -= 1
        if random.uniform(0, 100) < correct_percent:
            response[answer] = answers.get(answer)  # put in the correct answer
        else:
            response[answer] = "X"

        if attempt_no <= 0:
            break

    return response


def calculate_score(responses, answers):
    score = 0
    for question, answer in responses.items():
        if answers[question] == answer:
            score += 4
        if answers[question] != answer:
            score -= 1
    return score


answers = generate_answer_key()
response = generate_response(4, answers)
print(calculate_score(response, answers))
