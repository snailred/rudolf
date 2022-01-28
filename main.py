def main():
    steepan = int(input())
    coefs = [int(input()) for i in range(steepan + 1)]
    final_str = ""
    steepan_2 = steepan
    for coef in coefs:
        if coef != 0:
            monom = ""
            if coef > 0:
                if final_str != "":
                    monom += " + "
            elif coef < 0:
                monom += " - "
            if abs(coef) != 1:
                monom += str(abs(coef))
            if steepan_2 != 0:
                if abs(coef) != 1:
                    monom += " * "
                monom += "x"
            if steepan_2 > 1:
                monom += "^" + str(steepan_2)
            steepan_2 -= 1
            final_str += monom

    print(final_str)

if __name__ == "__main__":
    main()
