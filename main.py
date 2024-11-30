import random

# Defining some constants
QUESTIONS = 60  # number of questions in the paper
CORRECT_POINTS = 4  # points awarded for correct answer
WRONG_POINTS = -1  # points awarded for incorrect answer


def generate_answer_key():
    return {i + 1: random.choice(["A", "B", "C", "D"]) for i in range(QUESTIONS)}


def generate_response(attempt_no, answers, accuracy=100):
    response = {}
    for answer in answers:
        attempt_no -= 1
        if random.uniform(0, 100) < accuracy:
            response[answer] = answers.get(answer)  # put in the correct answer
        else:
            response[answer] = "X"  # wrong answer chosen

        if attempt_no <= 0:
            break

    return response


def calculate_score(responses, answers):
    score = 0
    for question, answer in responses.items():
        if answers[question] == answer:
            score += CORRECT_POINTS
        if answers[question] != answer:
            score += WRONG_POINTS
    return score


def run_simulation(papers, accuracy, attempt_questions):
    scores = []
    for _ in range(papers):
        answers = generate_answer_key()
        assert attempt_questions <= QUESTIONS

        response = generate_response(
            attempt_no=attempt_questions,
            accuracy=accuracy,
            answers=answers,
        )
        score = calculate_score(response, answers)
        scores.append(score)

    print(
        f"Ran a simulation on {papers} papers, attempting {attempt_questions} questions, assuming a {accuracy}% accuracy"
    )
    print("Average score simulated:", sum(scores) / len(scores))
    print("Highest simulated:", max(scores), "\t", "Lowest simulated:", min(scores))


run_simulation(papers=1000, accuracy=70, attempt_questions=60)  # total questions = 60
