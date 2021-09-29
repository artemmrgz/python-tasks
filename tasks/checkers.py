def is_valid(value):
    return value >= 0


def is_yes(question):
    answer = input(question).lower()
    return answer in ['y', 'yes']
