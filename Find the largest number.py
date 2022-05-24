# Wir erstellen eine Variable, die den größten Wert enthält, den wir bis jetzt gesehen haben.  Wenn die aktuelle Zahl, die wir betrachten, größer ist, ist sie der neue größte Wert, den wir bisher gesehen haben.
largest_so_far = None
print('Before:')
for the_num in [9, 41, 12, 9, 74, 15]:
    if largest_so_far is None:
        largest_so_far = the_num
    elif the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After:', largest_so_far)