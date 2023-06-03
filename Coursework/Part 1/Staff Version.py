# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1898928

# Date: 18/04/2022


Progress = []
Exclude = []
Retriever = []
Trailer = []

# Staff Version With Histogram
print('Staff Version With Histogram')
print('')


def progress():
    return 'Progress'


def exclude():
    return 'Exclude'


def retriever():
    return 'module retriever'


def trailer():
    return 'Progress (module trailer)'


def horizontalHistogram():
    # calling horizontalHistogram function to generate stars for each progression outcome and display the results.
    Progress1 = Progress.count('Progress')
    Trailer1 = Trailer.count('Progress (module trailer)')
    Retriever1 = Retriever.count('module retriever')
    Exclude1 = Exclude.count('Exclude')

    print('Progress', Progress1, ' = ', end='')
    for i in range(Progress1):
        print('*', end=' ')
    print('\nTrailer', Trailer1, ' = ', end='')
    for i in range(Trailer1):
        print('*', end=' ')
    print('\nRetriever', Retriever1, ' = ', end='')
    for i in range(Retriever1):
        print('*', end=' ')
    print('\nExclude', Exclude1, ' = ', end='')
    for i in range(Exclude1):
        print('*', end=' ')

    number = Progress1 + Retriever1 + Exclude1 + Trailer1   # calculate the total of all counting variables.
    print()
    print()
    print(number, 'outcomes in total.')  # display the total outcomes on the screen.
    print('------------------------------------------------------------')


def validation():
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

        # Progression Outcome
            # Exclude
        if fail > (passCredit + defer):
            result1 = exclude()
            print(result1)
            Exclude.append(result1)

            # Progress
        elif passCredit == 120 and defer == fail == 0:
            result2 = progress()
            print(result2)
            Progress.append(result2)

            # Progress (module trailer)
        elif passCredit == 100 and passCredit > (defer + fail):
            result4 = trailer()
            print(result4)
            Trailer.append(result4)

        else:
            # Do not progress – module retriever
            result3 = retriever()
            print(result3)
            Retriever.append(result3)

        print('')
        while True:
            print('Would you like to enter another set of data?')
            letter = str(input('Enter y for yes and q for quit and view result : '))
            if letter == 'y':  # Enter 'y' continue the code.
                print('')
                break
            elif letter == 'q':  # Enter 'q' print Horizontal Histogram and exit code.
                print('')
                print('------------------------------------------------------------')
                print('Horizontal Histogram')
                horizontalHistogram()
                exit()
            else:
                print("--------------------\nenter only y or q\n--------------------")


while True:
    validation()
