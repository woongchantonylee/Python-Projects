#   Q1: A secretary writes letters to A, B, C, and D. She also prepares four
#   envelopes addressed to A, B, C, and D. She manages to put all the letters
#   in the wrong envelopes. Enumerate (list) all the ways she can do that.


def permute(a, lo, hi):
    if lo == hi:
        wrong = True
        for j in range(len(a)):
            if ord(a[j]) == j + 65:
                wrong = False
                break
        if wrong:
            print(a)
    else:
        for i in range(lo, hi):
            a[i], a[lo] = a[lo], a[i]
            permute(a, lo + 1, hi)
            a[i], a[lo] = a[lo], a[i]


def main():

    a = ['A', 'B', 'C', 'D']

    print('Testing all permutations')
    permute(a, 0, len(a))


main()
