# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1898928

# Date: 18/04/2022

# open new Text file for writing purpose.
f = open('Combine.txt', 'w')
f.close()

print('Staff Version With Text File')
print('')


def progress():
    return 'Progress'


def exclude():
    return 'Exclude'


def retriever():
    return 'Module retriever'


def trailer():
    return 'Progress (module trailer)'


def outcomeList():
    if fail > (passCredit + defer):
        result1 = exclude()
        print(result1)
        excludeList = ""
        excludeList = "{0} - {1}, {2}, {3}".format(result1, passCredit, defer, fail)
        # open new Text file for append purpose.append
        f = open('Combine.txt', 'a')
        f.write(excludeList)
        f.write('\n')
        f.close()

    elif passCredit == 120 and defer == fail == 0:
        result2 = progress()
        print(result2)
        progressList = ""
        progressList = "{0} - {1}, {2}, {3}".format(result2, passCredit, defer, fail)
        # open new Text file for append purpose.append
        f = open('Combine.txt', 'a')
        f.write(progressList)
        f.write('\n')
        f.close()

    elif passCredit == 100 and passCredit > (defer + fail):
        result4 = trailer()
        print(result4)
        trailerList = ""
        trailerList = "{0} - {1}, {2}, {3}".format('Progress (module trailer)', passCredit, defer, fail)
        # open new Text file for append purpose.append
        f = open('Combine.txt', 'a')
        f.write(trailerList)
        f.write('\n')
        f.close()

    else:
        result3 = retriever()
        print(result3)
        retrieverList = ""
        retrieverList = "{0} - {1}, {2}, {3}".format('Module retriever', passCredit, defer, fail)
        # open new Text file for append purpose.append
        f = open('Combine.txt', 'a')
        f.write(retrieverList)
        f.write('\n')
        f.close()


def validation():
    global fail, passCredit, defer
    while True:
        try:
            passCredit = int(input('Enter Your total PASS credits: '))

            if passCredit != 0 and passCredit != 20 and passCredit != 40 and passCredit != 60 and passCredit != 80 and \
                    passCredit != 100 and passCredit != 120:
                print('Out of range')
                continue
            defer = int(input('Enter Your total DEFER credits: '))

            if defer != 0 and defer != 20 and defer != 40 and defer != 60 and defer != 80 and defer != 100 and \
                    defer != 120:
                print('out of range')
                continue
            fail = int(input('Enter Your total FAIL credits: '))

            if fail != 0 and fail != 20 and fail != 40 and fail != 60 and fail != 80 and fail != 100 and fail != 120:
                print('Out of range')
                continue

            total = passCredit + defer + fail
            if total > 120:
                print('total incorrect')
                continue
        except ValueError:
            print("Integer required")
            continue

        outcomeList()

        print('')
        print('Would you like to enter another set of data?')
        while True:
            letter = str(input('Enter y for yes and q for quit and view result : '))
            print('')
            if letter == 'y':   # Enter 'y' continue the code.
                break
            elif letter == 'q':  # Enter 'q' print Vertical Histogram and exit code.
                print('')
                f = open('Combine.txt', 'r')
                for line in f:
                    print(line, end='')
                f.close()
                exit()
            else:
                print("--------------------\nenter only y or q\n--------------------")


while True:
    validation()
