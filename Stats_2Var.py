# This Calculator is to be used for Two Variable statistics!
import sys

print("Welcome to the 2-Var Stats Calculator! \nAll answers will be rounded to two decimal places. \n")

while True:
    while True:
        try:
            listingX = [float(i) for i in input("Please input your independent (x) values \n"
                                                "and separate each one with a space:\n").split(" ")]
            if len(listingX) > 2:
                while True:
                    try:
                        listingY = [float(j) for j in input("Please input your dependent (y) values \n"
                                "in order/respect to the independent values. \n"
                                "Separate each value with a space as well.\n").split(" ")]
                        if len(listingX) == len(listingY):
                            break
                        if len(listingX) != len(listingY):
                            print("There isn't the same amount of X values and Y values. Try again!")
                    except ValueError:
                        print("There was an error inputting your Y values or you inputted nothing. Try again!")
            else:
                print("That is not enough values for calculations. Try again!")
            break
        except ValueError:
            print("There was an error inputting your X values or you inputted nothing. Try again!")

    def Var(set):
        total = 0
        for i in set:
            a = (i - (sum(set)/len(set))) ** 2
            total = total + a
        return total / len(set)

    def VarS(set):
        total = 0
        for i in set:
            a = (i - (sum(set)/len(set))) ** 2
            total = total + a
        return total / (len(set) - 1)

    def median(set):
        sortedset = sorted(set)
        if len(sortedset) % 2 != 0:
            result = len(sortedset) // 2
            return sortedset[result]
        elif len(sortedset) % 2 == 0:
            part_1 = (len(sortedset)//2) - 1
            part_2 = len(sortedset)//2
            result_A = (sortedset[part_1] + sortedset[part_2])/2.0
            return result_A

    def quart1(set):
        part = (len(set) + 1) * 0.25
        set = sorted(set)
        n = int(part)
        if part == n:
            return set[n - 1]
        return set[n - 1] + (set[n] - set[n - 1]) * (part - n)

    def quart3(set):
        part = (len(set) + 1) * 0.75
        set = sorted(set)
        n = int(part)
        if part == n:
            return set[n - 1]
        return set[n - 1] + (set[n] - set[n - 1]) * (part - n)

    def CoVar(set1, set2):
        Total = 0
        for (x, y) in zip(set1, set2):
            a = (x - (sum(set1)/len(set1))) * (y - (sum(set2)/len(set2)))
            Total = Total + a
        return Total / (len(set1) - 1)


    Corr = CoVar(listingX, listingY) / ((VarS(listingY) ** 0.5) * (VarS(listingX) ** 0.5))

    RegB = Corr * (VarS(listingY) ** 0.5 / VarS(listingX) ** 0.5)

    RegA = (sum(listingY)/len(listingY)) - RegB * (sum(listingX)/len(listingX))

    CorrDet = Corr ** 2

    print("\nHere are your results:")
    print("1st Quartile of X / Y: (%s / %s)" % (quart1(listingX),quart1(listingY)))
    print("Median of X / Y: (%s / %s)" % (median(listingX), median(listingY)))
    print("3rd Quartile of X / Y: (%s / %s)" % (quart3(listingX), quart3(listingY)))
    print("Mean of X / Y: (%s / %s)" % ((sum(listingX)/len(listingX)), sum(listingY)/len(listingY)))
    print("Population Variance of X / Y: (%s / %s)" % (round(Var(listingX), 4),
                                                       round(Var(listingY), 4)))
    print("Sample Variance of X / Y: (%s / %s)" % (round(VarS(listingX), 4),
                                                   round(VarS(listingY), 4)))
    print("Sample Standard Deviation of X / Y: (%s / %s)" % (round(VarS(listingX) ** 0.5, 4),
                                                             round(VarS(listingY) ** 0.5, 4)))
    print("Covariance: %s" % (round(CoVar(listingX, listingY), 4)))
    print("Correlation Coefficient: %s" % round(Corr, 4))
    print("Coefficient of Determination: %s" % round(CorrDet, 4))
    print("Linear Regression Formula: Y = %s + %s(X)" % (round(RegA, 4), round(RegB, 4)))

    while True:
        ans = input("Do you want to use the calculator again? (y/n):\n")
        if str(ans) == "n" or str(ans) == "N":
            sys.exit("Thank you for using the calculator! Now shutting down...")
        elif str(ans) == "y" or str(ans) == "Y":
            break
        else:
            print("Sorry, I didn't understand that.")