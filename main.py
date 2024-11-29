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


def run_simulation(papers, correct_percent, attempt_questions):
    scores = []
    for _ in range(papers):

        answers = generate_answer_key()
        response = generate_response(
            attempt_no=attempt_questions,
            correct_percent=correct_percent,
            answers=answers,
        )
        score = calculate_score(response, answers)
        scores.append(score)

    print(
        f"Ran a simulation on {papers} papers, attempting {attempt_questions} questions, assuming a {correct_percent}% accuracy"
    )
    print("Highest simulated:", max(scores))
    print("Lowest simulated:", min(scores))
    print("Average score simulated:", sum(scores) / len(scores))
