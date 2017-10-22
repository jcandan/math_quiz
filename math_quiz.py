#!/usr/bin/python3

import time
import random
import argparse


def main():
    questions = []
    time_0 = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--random", help = "Randomize set of questions.", action = "store_true")
    parser.add_argument("-s1", "--start_one", help = "Specify start of range for first term",
                        type = int, default = 1)
    parser.add_argument("-e1", "--end_one", help = "Specify end of range for first term",
                        type = int, default = 10)
    parser.add_argument("-s2", "--start_two", help = "Specify start of range for second term",
                        type = int, default = 1)
    parser.add_argument("-e2", "--end_two", help = "Specify end of range for second term",
                        type = int, default = 10)
    args = parser.parse_args()

    factors_1 = list(reversed(range(args.start_one, args.end_one + 1)))
    factors_2 = list(reversed(range(args.start_two, args.end_two + 1)))
    for factor_1 in factors_1:
        for factor_2 in factors_2:
            questions.append({'one': factor_1, 'two': factor_2})

    if args.random:
        random.shuffle(questions)

    for question in questions:
        correct = question['one'] + question['two']
        user_response = input(str(question['one']) + " + " + str(question['two']) + " = ")
        if str(correct) != user_response:
            print("Incorrect :( . . . The answer is " + str(correct))

    time_delta = time.time() - time_0
    m, s = divmod(time_delta, 60)
    print('Time: %02d:%02d' % (m, s))


if __name__ == "__main__":
    main()