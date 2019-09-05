

def sub_sets(a, b, c, idx):
    if idx == len(a):
        set_sum.append([abs(find_sum(b) - find_sum(c)), b, c])
        # print(b, c)
        return
    else:
        d = b[:]
        e = c[:]
        b.append(a[idx])
        c.append(a[idx])
        sub_sets(a, b, e, idx + 1)
        sub_sets(a, d, c, idx + 1)


# This function computes all combinations of a given size
def combine(a, b, lo, size):
    hi = len(a)
    if lo == hi:
        if len(b) == size:
            check_relationships(b)
        return
    if len(b) == size:
        check_relationships(b)
    else:
        c = b[:]
        b.append(a[lo])
        combine(a, c, lo + 1, size)
        combine(a, b, lo + 1, size)


def check_relationships(b):
    if b.__contains__('A') and not b.__contains__('B'):
        return
    elif b.__contains__('C') and b.__contains__('D'):
        return
    print(b)


def find_sum(a):
    sum = 0
    for num in a:
        sum += num
    return sum


set_sum = []


def main():
    #   Q4: Home owners A, B, C, D, E, and F have all agreed to serve on the Home
    #   Owners' Association. But the Home Owners' Association just needs three
    #   people. A is willing to serve only if B serves, though B has not made
    #   that same condition. C and D both refuse to serve if the other is in the
    #   association. Enumerate the different associations that you can form.

    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    empty = []
    combine(letters, empty, 0, 3)

'''
    # Find subsets of list of numbers such that the difference between two sets are the smallest
    p1 = []
    p2 = []
    nums = [15, 36, 72, 80, 40, 19, 12]
    sub_sets(nums, p1, p2, 0)
    min_dif = set_sum[0]
    for set in set_sum:
        if set[0] < min_dif[0]:
            min_dif = set
        elif set[0] == min_dif[0]:
            min_dif.append(set[0])
            min_dif.append(set[1])
            min_dif.append(set[2])
    print(min_dif)
'''

main()

