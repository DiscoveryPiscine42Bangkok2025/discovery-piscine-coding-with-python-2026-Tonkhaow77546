from sys import argv

if len(argv) > 1:
    print("none")
    exit(0)

for i in range(11):
    result = ""
    for j in range(11):
        result += f"{i * j} "
    print(f"Table de {i}: {result}")