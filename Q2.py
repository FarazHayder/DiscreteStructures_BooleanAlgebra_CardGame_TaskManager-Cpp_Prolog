def conjunction(p, q):
    if p == "T" and q == "T":
        return "T"
    else:
        return "F"


def disjunction(p, q):
    if p == "F" or q == "F":
        return "F"
    else:
        return "T"


def XOR(p, q):
    if p == q:
        return "F"
    else:
        return "T"


def implication(p, q):
    if p == "T" and q == "F":
        return "F"
    else:
        return "T"


def biconditional(p, q):
    if p == q:
        return "T"
    else:
        return "F"


def negation(p):
    if p == "T":
        return "F"
    else:
        return "T"


p = input("Enter the truth value of p (T for True and F for False): ")
while p != "T" and p != "F":
    print("Invalid input.")
    p = input("Enter the truth value of p (T for True and F for False): ")

q = input("Enter the truth value of q (T for True and F for False): ")
while q != "T" and q != "F":
    print("Invalid input.")
    q = input("Enter the truth value of q (T for True and F for False): ")

print("Choose the propositional logic (1-6): ")
print("1. Conjunction")
print("2. Disjunction")
print("3. Implication")
print("4. Biconditional")
print("5. XOR")
print("6. Negation")

logic = int(input())

if logic == 1:
    truthValue = conjunction(p, q)
elif logic == 2:
    truthValue = disjunction(p, q)
elif logic == 3:
    truthValue = implication(p, q)
elif logic == 4:
    truthValue = biconditional(p, q)
elif logic == 5:
    truthValue = XOR(p, q)
elif logic == 6:
    truthValue = negation(p)
else:
    print("Invalid input.")
    logic = int(input("Choose the propositional logic (1-6): "))

if truthValue == "T":
    print("The Boolean Expression is: True")
else:
    print("The Boolean Expression is: False")
