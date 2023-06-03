# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1898928

# Date: 18/04/2022


def validation():

    while True:
        try:
            # Pass volume of credits.
            passCredit = int(input('Please enter your credits at pass: '))
            if passCredit != 0 and passCredit != 20 and passCredit != 40 and passCredit != 60 and passCredit != 80 and \
                    passCredit != 100 and passCredit != 120:
                print('Out of range\n')
                continue

            # Defer volume of credits.
            defer = int(input('Please enter your credits at defer: '))
            if defer != 0 and defer != 20 and defer != 40 and defer != 60 and defer != 80 and defer != 100 and \
                    defer != 120:
                print('out of range\n')
                continue

            # Fail volume of credits.
            fail = int(input('Please enter your credits at fail: '))
            if fail != 0 and fail != 20 and fail != 40 and fail != 60 and fail != 80 and fail != 100 and fail != 120:
                print('Out of range\n')
                continue

            # Total volume of credit.
            total = passCredit + defer + fail
            if total > 120:
                print('total incorrect\n')
                continue
        except ValueError:
            print("Integer required\n")
            continue

        # Progression Outcome
        if fail > (passCredit + defer):
            print('Exclude')

        elif passCredit == 120 and defer == fail == 0:
            print('Progress')

        elif passCredit == 100 and passCredit > (defer + fail):
            print('Progress (module trailer)')
        else:
            print('Do not progress – module retriever')


validation()
