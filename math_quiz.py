#!/usr/bin/python3

import time
import random
import operator
import argparse
from argparse import RawTextHelpFormatter


def build_questions():
    """Define and parse command line arguments to generate a list of dictionaries.

    Each dictionary defines a first and second term, and math operator method and symbol

    :return: List of questions
    """
    questions = []
    operators = {}

    description = (
        "Description:\n"
        "\n"
        "Runs a timed quiz of math equations based on a range from 1 to 10."
        "User can specify the start and end of the range for both terms.\n"
    )

    epilog = (
        "Examples:\n"
        "\n"
        "python3 math_quiz.py \n"
        "python3 math_quiz.py -r                     Randomize entire set of terms\n"
        "python3 math_quiz.py -as                    Add and Subtract entire set of terms\n"
        "python3 math_quiz.py -asr                   Add and Subtract randomized entire set of terms\n"
        "python3 math_quiz.py -s1 5 -e1 5            Add 5's\n"
        "python3 math_quiz.py -s1 5 -e1 5 -as        Add and Subtract 5's\n"
        "python3 math_quiz.py -s1 5 -e1 5 -e2 5 -md  Multipy and Divide 5 with 1 - 5\n"
    )

    parser = argparse.ArgumentParser(prog = 'python3 math_quiz.py', usage = '%(prog)s [options]',
                                     description = description, epilog = epilog, formatter_class = RawTextHelpFormatter)
    parser.add_argument("-r", "--random", help = "Randomize set of questions.", action = "store_true")
    parser.add_argument("-s1", "--start_first", help = "Specify start of range for first term",
                        type = int, default = 1)
    parser.add_argument("-e1", "--end_first", help = "Specify end of range for first term",
                        type = int, default = 10)
    parser.add_argument("-s2", "--start_second", help = "Specify start of range for second term",
                        type = int, default = 1)
    parser.add_argument("-e2", "--end_second", help = "Specify end of range for second term",
                        type = int, default = 10)
    parser.add_argument("-a", "--add", help = "(Default) Add the terms", action = "store_true")
    parser.add_argument("-s", "--subtract", help = "Subtract the terms", action = "store_true")
    parser.add_argument("-m", "--multiply", help = "Multiply the terms", action = "store_true")
    parser.add_argument("-d", "--divide", help = "Divide the terms", action = "store_true")
    parser.add_argument("-n", "--negative", help = "Allow negative equations", action = "store_true")
    args = parser.parse_args()

    if args.add or not (args.subtract or args.multiply or args.divide):
        operators['add'] = '+'
    if args.subtract:
        operators['sub'] = '-'
    if args.multiply:
        operators['mul'] = 'x'
    if args.divide:
        operators['floordiv'] = '/'

    terms_1 = list(reversed(range(args.start_first, args.end_first + 1)))
    terms_2 = list(reversed(range(args.start_second, args.end_second + 1)))
    for term_1 in terms_1:
        for term_2 in terms_2:
            for method, symbol in operators.items():
                tmp_1, tmp_2 = term_1, term_2
                if method == 'floordiv':
                    tmp_1 = term_1 * term_2
                if not args.negative and method == 'sub' and term_2 > term_1:
                    tmp_1, tmp_2 = term_2, term_1
                questions.append({'first': tmp_1, 'second': tmp_2, 'method': method, 'symbol': symbol})

    if args.random:
        random.shuffle(questions)

    return questions


def run_quiz(questions):
    """Loop through and display questions for user responses, and evaluate their correct answer.

    :param questions:
    :return:
    """
    time_0 = time.time()
    for question in questions:
        # evaluate an expression for the given terms and operation, e.g. operator.add(3, 4)
        expression = "operator.{}({}, {})".format(question['method'], question['first'], question['second'])
        correct = eval(expression)

        # prompt user with a neatly formatted math question
        question_str = "{} {} {} = ".format(str(question['first']), question['symbol'], str(question['second']))
        user_response = input(question_str)

        if str(correct) != user_response:
            # note the user's incorrect response
            print("Incorrect :( . . . The answer is " + str(correct))

    time_delta = time.time() - time_0
    m, s = divmod(time_delta, 60)
    print('Time: %02d:%02d' % (m, s))


def main():
    questions = build_questions()
    run_quiz(questions)


if __name__ == "__main__":
    main()
