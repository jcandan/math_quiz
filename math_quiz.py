#!/usr/bin/python3

import time
import random
import argparse


def main():
    questions = []
    time_0 = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--random", help = "Randomize set of questions.", action = "store_true")
    parser.add_argument("-s1", "--start_first", help = "Specify start of range for first term",
                        type = int, default = 1)
    parser.add_argument("-e1", "--end_first", help = "Specify end of range for first term",
                        type = int, default = 10)
    parser.add_argument("-s2", "--start_second", help = "Specify start of range for second term",
                        type = int, default = 1)
    parser.add_argument("-e2", "--end_second", help = "Specify end of range for second term",
                        type = int, default = 10)
    args = parser.parse_args()

    terms_1 = list(reversed(range(args.start_first, args.end_first + 1)))
    terms_2 = list(reversed(range(args.start_second, args.end_second + 1)))
    for term_1 in terms_1:
        for term_2 in terms_2:
            questions.append({'first': term_1, 'second': term_2})

    if args.random:
        random.shuffle(questions)

    for question in questions:
        correct = question['first'] + question['second']
        user_response = input(str(question['first']) + " + " + str(question['second']) + " = ")
        if str(correct) != user_response:
            print("Incorrect :( . . . The answer is " + str(correct))

    time_delta = time.time() - time_0
    m, s = divmod(time_delta, 60)
    print('Time: %02d:%02d' % (m, s))


if __name__ == "__main__":
    main()