first_class = [x for x in range(160, 177, 2)]
second_class = [x for x in range(162, 181, 3)]

both_classes = (first_class + second_class)
both_classes.sort()
print(both_classes)