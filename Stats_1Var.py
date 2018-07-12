# This Calculator is to be used for Single Variable statistics!
import sys

print("Welcome to the 1-Var Stats Calculator!\nAll answers, except the sum, range,\
 and median,\nwill be rounded to two decimal places!")

while True:
    while True:
        try:
            listing = [float(i) for i in input("Please input your values and separate each \
value with a space:\n ").split(" ")]
            if len(listing) > 2:
                break
            if len(listing) <= 2:
                print("That is not enough values for calculations! Try again!")
        except ValueError:
            print("There was either an error in your input or you inputted nothing.\nTry again!")

    mean = sum(listing) / len(listing)

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

    def mode(set):
        from collections import Counter
        return Counter(set).most_common(1)

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

    def variance(set):
        total = 0
        for i in set:
            a = (i - mean) ** 2
            total = total + a
        return total / len(set)

    def variance_S(set):
        total = 0
        for i in set:
            a = (i - mean) ** 2
            total = total + a
        return total / (len(set) - 1)

    print("\nHere are your results:")
    print("Sum: %s" % sum(listing))
    print("Min & Max: %s &" % min(listing),max(listing))
    print("Range: %s" % (max(listing) - min(listing)))
    print("1st Quartile: %s" % quart1(listing))
    print("Median: %s" % median(listing))
    print("3rd Quartile: %s" % quart3(listing))
    print("Interquartile Range: %s" % (quart3(listing) - quart1(listing)))
    print("Mode (Value, Frequency): %s" % mode(listing))
    print("Mean: %s" % round(mean, 2))
    print("Population Variance: %s" % round(variance(listing), 2))
    print("Population Standard Deviation: %s" % round(variance(listing) ** 0.5, 2))
    print("Sample Variance: %s" % round(variance_S(listing), 2))
    print("Sample Standard Deviation: %s\n" % round(variance_S(listing) ** 0.5, 2))
    while True:
        ans = input("Do you want to use the calculator again? (y/n):\n")
        if str(ans) == "n" or str(ans) == "N":
            sys.exit("Thank you for using the calculator! Now shutting down...")
        elif str(ans) == "y" or str(ans) == "Y":
            break
        else:
            print("Sorry. I didn't understand.")