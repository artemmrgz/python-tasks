def is_lucky_moscow(ticket):
    first_part, second_part = ticket[:3], ticket[3:]
    first_numbers = map(int, list(first_part))
    second_numbers = map(int, list(second_part))
    return sum(first_numbers) == sum(second_numbers)


def is_lucky_piter(ticket):
    numbers = map(int, list(ticket))
    even = filter(lambda x: x % 2 == 0, numbers)
    odd = filter(lambda x: x % 2 != 0, numbers)
    return sum(even) == sum(odd)


def file_reader(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content


def find_valid_tickets(text):
    tickets = text.split()
    valid_tickets = filter(lambda x: len(x) == 6, tickets)
    return valid_tickets


def find_lucky_tickets(tickets, method):
    counter = 0
    for ticket in tickets:
        if method(ticket):
            counter += 1
    return counter


def main():
    path_to_file = input('Please enter path to file: ')
    method = input('Please choose method of selecting lucky tickets (Moscow or Piter): ')
    content = file_reader(path_to_file)
    tickets = find_valid_tickets(content)
    if method == 'Moscow':
        return find_lucky_tickets(tickets, is_lucky_moscow)
    if method == 'Piter':
        return find_lucky_tickets(tickets, is_lucky_piter)
    return 'No tickets found'


if __name__ == '__main__':
    try:
        result = main()
        print(result)
    except FileNotFoundError:
        print("File can't be found, please check and try again")
