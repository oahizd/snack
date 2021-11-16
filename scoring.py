from collections import Counter

def main():
    with open('scoring.db', 'r+') as f:
        a = f.readlines()
        for i in range(len(a)):
            a[i] = a[i].strip()

        b = []
        a = dict(Counter(a))
        for i in a.keys():
            b.append('%s\n' % i)


    f = open('scoring.db', 'w')
    f.writelines(b)

main()