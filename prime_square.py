# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_primes(till):
    primes = [2]
    for i in range (3, till):
        isPrime =  True
        for j in range(len(primes)):
            if i % primes[j] == 0:
                isPrime = False
        if isPrime:
            primes.append(i)
    return primes

def square_shit(initial_list):
    squared_list = []
    for number in initial_list:
        squared_list.append(number * number)
    return squared_list

def preserve_delta_increase(initial_list):
    output = [0, 1]
    for number in initial_list:
        if output[-1] - output[-2] < number - output[-1]:
            output.append(number)
    return output


def give_delta(initial_list):
    delta_list = []
    for i in range(len(initial_list)-1):
        delta_list.append(initial_list[i+1] - initial_list[i])
    return(delta_list)


def get_days():
    square_prime = preserve_delta_increase(square_shit(get_primes(200)))
    reps_today = [0] * 80000
    for i in range(36500):
        for j in range(len(square_prime)):
            reps_today[square_prime[j] + i] += 1
    return reps_today


def find_max(input_list):
    max = input_list[0]
    for number in input_list:
        if number > max:
            max = number
    return max

def find_change(input_list):
    change_list = []
    for i in range(len(input_list)-1):
        if input_list[i] != input_list[i+1]:
            change_list.append(i)
    return change_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(preserve_delta_increase(square_shit(get_primes(200))))
    print(give_delta(preserve_delta_increase(square_shit(get_primes(200)))))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
