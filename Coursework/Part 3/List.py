# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1898928

# Date: 18/04/2022

Progress = []
Exclude = []
Retriever = []
Trailer = []
Combine = []

table = [Progress, Trailer, Retriever, Exclude]

# Staff Version With Histogram list
print('Staff Version With List')
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
        # get the progression data, format of "Progression Outcome - Pass Credit,Defer Credit,fail Credit".
        excludeList = "{0} - {1}, {2}, {3}".format(result1, passCredit, defer, fail)
        # append progression data to a List.
        Combine.append(excludeList)

    elif passCredit == 120 and defer == fail == 0:
        result2 = progress()
        print(result2)
        progressList = ""
        # get the progression data, format of "Progression Outcome - Pass Credit,Defer Credit,fail Credit".
        progressList = "{0} - {1}, {2}, {3}".format(result2, passCredit, defer, fail)
        # append progression data to a List.
        Combine.append(progressList)

    elif passCredit == 100 and passCredit > (defer + fail):
        result4 = trailer()
        print(result4)
        trailerList = ""
        # get the progression data, format of "Progression Outcome - Pass Credit,Defer Credit,fail Credit".
        trailerList = "{0} - {1}, {2}, {3}".format('Progress (module trailer)', passCredit, defer, fail)
        # append progression data to a List.
        Combine.append(trailerList)

    else:
        result3 = retriever()
        print(result3)
        retrieverList = ""
        # get the progression data, format of "Progression Outcome - Pass Credit,Defer Credit,fail Credit".
        retrieverList = "{0} - {1}, {2}, {3}".format('Module retriever', passCredit, defer, fail)
        # append progression data to a List.
        Combine.append(retrieverList)


def validation():
    global fail, passCredit, defer
    while True:
        try:
            # Pass volume of credits.
            passCredit = int(input('Enter Your total PASS credits: '))
            if passCredit != 0 and passCredit != 20 and passCredit != 40 and passCredit != 60 and passCredit != 80 and \
                    passCredit != 100 and passCredit != 120:
                print('Out of range')
                continue

            # Defer volume of credits.
            defer = int(input('Enter Your total DEFER credits: '))
            if defer != 0 and defer != 20 and defer != 40 and defer != 60 and defer != 80 and defer != 100 and \
                    defer != 120:
                print('out of range')
                continue

            # Fail volume of credits.
            fail = int(input('Enter Your total FAIL credits: '))
            if fail != 0 and fail != 20 and fail != 40 and fail != 60 and fail != 80 and fail != 100 and fail != 120:
                print('Out of range')
                continue

            # Total volume of credit.
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
            if letter == 'y':  # Enter 'y' continue the code.
                break
            elif letter == 'q':  # Enter 'q' print Vertical Histogram and exit code.
                print('')
                if Combine:
                    for index, result in enumerate(Combine):
                        print(result)
                exit()
            else:
                print("--------------------\nenter only y or q\n--------------------")


while True:
    validation()
