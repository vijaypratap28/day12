# created by vijay pratap singh
#created date 30-01-2017
# matrix addition program
class matrix:
	def __init__(self, array):
		self.array = array
		
	def __add__(self,other):
		self.other = other		
		
		new_matrix = []
		for i in range(len(self.array)):
			row = []
			for j in range(len(self.array[0])):
				row.append((self.array[i][j]) + (other.array[i][j]))

			new_matrix.append(row)

		return matrix(new_matrix)

	def __sub__(self,other):
		self.other = other		
		
		new_matrix = []
		for i in range(len(self.array)):
			row = []
			for j in range(len(self.array[0])):
				row.append((self.array[i][j]) - (other.array[i][j]))

			new_matrix.append(row)

		return matrix(new_matrix)
	def __mul__(self,other):
		self.other = other		
		
		new_matrix = []
		for i in range(len(self.array)):
			row = []
			for j in range(len(self.array[0])):
				row.append((self.array[i][j]) * (other.array[i][j]))

			new_matrix.append(row)

		return matrix(new_matrix)
	def __div__(self,other):
		self.other = other		
		
		new_matrix = []
		for i in range(len(self.array)):
			row = []
			for j in range(len(self.array[0])):
				row.append((self.array[i][j]) / (other.array[i][j]))

			new_matrix.append(row)

		return matrix(new_matrix)
	def __str__(self):
		return str(self.array)



num_row = int(raw_input("no of row"))
num_column = int(raw_input("no of column"))
matrix1 = []
for i in range(num_row):
	row = []
	for j in range(num_column):
		a = int(raw_input())
		row.append(a)
	matrix1.append(row)
num_row1 = int(raw_input("no of row"))
num_column1 = int(raw_input("no of column"))
matrix2 = []
for i in range(num_row1):
	row1 = []
	for j in range(num_row1):
		b = int(raw_input())
		row1.append(b)
	matrix2.append(row1)


		
		
m1 = matrix(matrix1)
m2 = matrix(matrix2)
print "matrix1"
print m1
print "matrix2"
print m2
print "Addition of two mayrix is",m1+m2
print "Substraction of two matrix is",m1-m2
print "Multiplication of two mayrix is",m1*m2
print "Division of two matrix is",m1/m2

