li = [10,2,8,7,5,4,3,11,0, 1]
lg = lambda x: x < 10
filtered_result = filter (lg, li)
print(list(filtered_result))



x = lambda a: a + 10
print(x(100))


x = lambda a, b : a * b
print(x(5, 6))


double = lambda x: x * 2

# Output: 10
print(double(10))





f = open("C:\Users\Rama Subhrahamanyam\Documents\CV_Hari krishna_B.Tech_Mech.docx")
print(f.read())

for data in f:
    print(data)

