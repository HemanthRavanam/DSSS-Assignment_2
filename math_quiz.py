import random

def generate_random_integer(min_value, max_value):
    """Generate a random integer between min_value and max_value (inclusive)."""
    return random.randint(min_value, max_value)

def choose_random_operator():
    """Return a random choice among the operators '+', '-', and '*'."""
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """Create a math problem as a string and calculate the correct answer."""
    problem_str = f"{num1} {operator} {num2}"
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return problem_str, answer

def math_quiz():
    score = 0
    total_questions = 5  # Adjusted to a reasonable number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = choose_random_operator()

        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
