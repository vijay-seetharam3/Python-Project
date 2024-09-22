b = input()
ch1 = input()
ch2 = input()
a = list(b)
for i in range(len(a)):
    if a[i].lower() == ch1.lower():
        if a[i].isupper():
            a[i] = ch2.upper()
        else:
            a[i] = ch2.lower()
    elif a[i].lower() == ch2.lower():
        if a[i].isupper():
            a[i] = ch1.upper()
        else:
            a[i] = ch1.lower()
print(''.join(a))
