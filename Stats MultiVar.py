# This Calculator is to be used for Multi-variable Variable statistics!
import sys
import numpy

print("Welcome to the Multi-Var Stats Calculator!\nRegression will be round to "
      "four decimal places!\nNote: Variance/Standard Deviation are samples.")

while True:
    while True:
        try:
            listingY = [float(i) for i in input("Please input your dependent (Y) values \n"
                                                "and separate each one with a space:\n").split(" ")]
            if len(listingY) > 2:
                print("Number of values: %s" % len(listingY))
                while True:
                    try:
                        listingXs = {}
                        numX = int(input("Please input how many independent variables (Xs) you " 
                                         "will use\n in this calculation:\n"))
                        if numX > 0:
                            np = 1
                            while numX > 0:
                                try:
                                    listingXs["X{0}".format(np)] = [float(i) for i in input("Please "
                                                                    "input your independent values "
                                                                    "for variable #%s:\n" %
                                                                    str(np)).split(" ")]
                                    if len(listingXs["X{0}".format(np)]) == len(listingY):
                                        np += 1
                                        numX -= 1
                                    else:
                                        print("That is not the same amount of values. Try again!")
                                except ValueError:
                                    print("There's an error inputting variable #%s or inputted nothing. "
                                          "Try again!" % str(np))
                        else:
                            print("That's not a valid number of X values. Try again")
                        break
                    except ValueError:
                        print("There's an error inputting the number of X variables or you inputted nothing "
                              "Try again!")
            break
        except ValueError:
            print("There's an error inputting your Y values or you inputted nothing. Try again!")

    # insert stuff
    def var(set):
        total = 0
        for i in set:
            total += (i - (sum(set)/len(set))) ** 2
        return total/(len(set) - 1)

    length = len(listingY)
    n = []
    while length > 0:
        n.append(1.0)
        length -= 1
    X = list(zip(n,*listingXs.values()))
    Xt = []
    Xt.append(n)
    for p in listingXs.values():
        Xt.append(p)
    XtX = numpy.matmul(Xt, X)
    XtXinv = numpy.linalg.inv(XtX)
    Y = [[i] for i in listingY]
    XtY = numpy.matmul(Xt, Y)
    B = numpy.matmul(XtXinv,XtY)

    reg = "Y = " + str(round(*B[0], 4)) + " "
    for i in range(1, np):
        p = "+ " + str(round(*B[i], 4)) + "(X" + str(i) + ") "
        reg += p

    def mean_var(set):
        n = 1
        for i in set:
            m = sum(i)/len(i)
            print("Mean of X%s: %s" % (n, round(m, 4)))
            t = 0
            for z in i:
                t += (z - m) ** 2
            v = t / (len(i) - 1)
            print("Variance of X%s: %s" % (n, round(v, 4)))
            print("Standard deviation of X%s: %s" % (n, round(v ** 0.5, 4)))
            n += 1

    print("\nHere are the results:")
    print("Mean of Y: %s" % (sum(listingY)/len(listingY)))
    print("Variance of Y: %s" % round(var(listingY), 4))
    print("Standard deviation of Y: %s" % round(var(listingY) ** 0.5, 4))
    print()
    print(mean_var(listingXs.values()))
    print()
    print("Regression Formula:")
    print(reg)
    print()
    while True:
        ans = input("Do you want to use the calculator again? (y/n):\n")
        if str(ans) == "n" or str(ans) == "N":
            sys.exit("Thank you for using the calculator! Now shutting down...")
        elif str(ans) == "y" or str(ans) == "Y":
            break
        else:
            print("Sorry. I didn't understand.")

