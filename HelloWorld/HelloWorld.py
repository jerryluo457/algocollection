"""
The input will start with a positive integer, giving the number
of instances that follow. For each instance,
there will be a string. fOr each string s, the
program should output Hello, s! on its own line.
"""
#number, toSayHello: list


def helloWorld():

    number_inputs = int(input())
    names = []
    for _ in range(number_inputs):
        names.append(input())

    # print(len(names))
    for i in range(len(names)):
        print(f"Hello, {names[i]}!")

if __name__ == "__main__":
    helloWorld()