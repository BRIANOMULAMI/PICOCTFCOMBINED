# Python program to calculate memory address for win().

main = input("Enter hex: ")
main = int(main, 16) - 150
main = hex(main)
print(main)