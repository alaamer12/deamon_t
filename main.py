import sys
temp = sys.stdout
sys.stdout = open("text.txt", "w")
# print(open("text.txt").read())
print("testing")
print("testing2")
sys.stdout.close()
sys.stdout = temp
print("normal")