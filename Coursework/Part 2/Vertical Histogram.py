# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1898928

# Date: 18/04/2022

Progress = []
Exclude = []
Retriever = []
Trailer = []

table = [Progress, Trailer, Retriever, Exclude]

PassCredit = []
Defer = []
Fail = []

# Staff Version With Histogram
print('Staff Version With Histogram')
print('')


def progress():
    return 'Progress'


def exclude():
    return 'Exclude'


def retriever():
    return 'Module retriever'


def trailer():
    return 'Progress (module trailer)'


def histogramTable(table):
    # calling Vertical_histogram function to generate stars for each progression outcome and display the results.

    Progress1 = Progress.count('Progress')
    Trailer1 = Trailer.count('Progress (module trailer)')
    Retriever1 = Retriever.count('Module retriever')
    Exclude1 = Exclude.count('Exclude')

    global number
    number = Progress1 + Retriever1 + Exclude1 + Trailer1  # calculate the total of all counting variables.

    print("Progress", "\tTrailer", "\tRetriever", "\tExclude")
    for i in range(number):
        for x in table:
            if len(x) > 0:
                print("   ", "*", "   ", end="  ")
                x.pop()
            else:
                print("   ", " ", "   ", end="  ")
        print()


def verticalHistogram():

    histogramTable(table)
    print("\n")
    print(number, "outcomes in total.")              # display the total outcomes on the screen.
    print('------------------------------------------------------------')


def validation():
    while True:
        try:
            # Pass volume of credits.
            passCredit = int(input('Enter Your total PASS credits: '))
            PassCredit.append(passCredit)
            if passCredit != 0 and passCredit != 20 and passCredit != 40 and passCredit != 60 and passCredit != 80 and \
                    passCredit != 100 and passCredit != 120:
                print('Out of range')
                continue

            # Defer volume of credits.
            defer = int(input('Enter Your total DEFER credits: '))
            Defer.append(defer)
            if defer != 0 and defer != 20 and defer != 40 and defer != 60 and defer != 80 and defer != 100 and \
                    defer != 120:
                print('out of range')
                continue

            # Fail volume of credits.
            fail = int(input('Enter Your total FAIL credits: '))
            Fail.append(fail)
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

        # Progression Outcome.
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
            print('')
            if letter == 'y':  # Enter 'y' continue the code.
                break
            elif letter == 'q':  # Enter 'q' print Vertical Histogram and exit code.
                print('')
                print('------------------------------------------------------------')
                print('Vertical Histogram')
                verticalHistogram()
                exit()
            else:
                print('print("--------------------\nenter only y or q\n--------------------")')


while True:
    validation()


