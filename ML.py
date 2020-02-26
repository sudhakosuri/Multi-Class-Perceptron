import numpy as np
data = open("mnist_data_training.csv",'r')


weights = [[0 for _ in range(784)] for _ in range(10)]

wrong_classification_count = 0
count = 0

for _ in range(0,3):

    print(_)
    for row in data:
        row_weights = []
        lst_row = (row.rstrip('\n').split(','))
        lst_row = [int(k) for k in lst_row]
        list_row = lst_row[:-1]

        for w in range(0,10):

            weight = np.dot(list_row, weights[w])
            row_weights.append(weight)

        max_weight = max(row_weights)
        max_weight_index = row_weights.index(max_weight)


        if (max_weight_index != (lst_row[784])):
            print("Hello")

            weights[lst_row[784]] = np.add(weights[lst_row[784]],list_row)

            weights[max_weight_index] = np.subtract(weights[max_weight_index],list_row)






data1 = open("mnist_data_test.csv",'r')

total_misclassified = 0


for row in data1:

    row_weights = []
    list_row = (row.rstrip('\n').split(','))[:-1]
    lt_row = (row.rstrip('\n').split(','))
    lt_row = [int(i) for i in lt_row]
    list_row = [int(i) for i in list_row]

    for w in range(0,10):

        weight = [(a*b) for a,b in zip(list_row, weights[w])]
        total_weight = 0

        for i in weight:
            total_weight += i


        row_weights.append(total_weight)


    max_weight = max(row_weights)

    max_weight_index = row_weights.index(max_weight)
    if (max_weight_index == (lt_row[784])):
        continue
    else:
        total_misclassified += 1


print("total_misclassified_test"+str(total_misclassified/5000))