i=6
while i>=1:
    print(i* '*')
    i-=1








i=6
while i>=6:
    print(i * '*')
    break
print("*   *")
print("*  *")
print("* *")
print("**")
print("*")










i=1
j=6
while i<=6:
   print (j*" "+ "* "*i)
   i+=1
   j-=6











def half_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Example: To print a half pyramid with 5 rows
half_pyramid(5)







i=1
j=6
while i<=6:
    print(j*" "+ "*" "*i")
    i+=1+int(" ")
    j=-1