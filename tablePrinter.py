
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)

for i in range(len(colWidths)):
	colWidths[i] = len(max(tableData[i], key=len))


for i in range(len(tableData[0])):
	for j in range(len(tableData)):
		print(tableData[j][i].rjust(colWidths[j]), end=' ')
	print()


#print(colWidths)
