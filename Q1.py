def simplify(string):
    len_str = len(string)
    temp_str = string + " "
    for i in range(len_str):
        if string[i] == "~" and string[i + 1] == "(":
            for j in range(i + 2, len_str):
                if string[j] == "(" or string[j] == ")":
                    temp_str = temp_str[:i] + "(" + temp_str[i + 1 :]
                    temp_str = temp_str[: i + 1] + "~" + temp_str[i + 2 :]
                    if temp_str[i + 3] == "^":
                        temp_str = temp_str[: i + 3] + "v" + temp_str[i + 4 :]
                    elif temp_str[i + 3] == "v":
                        temp_str = temp_str[: i + 3] + "^" + temp_str[i + 4 :]
                    temp_str = temp_str[: i + 4] + "~" + temp_str[i + 5 :]
                    temp_counter = 5
                    for k in range(4, len_str):
                        temp_str = (
                            temp_str[:temp_counter]
                            + string[k]
                            + temp_str[temp_counter + 1 :]
                        )
                        temp_counter += 1

    simplified_str = temp_str + " "
    len_of_temp_str = len_str + 1
    for i in range(len_of_temp_str):
        if temp_str[i] == "(" and i == 0:
            pass
        elif temp_str[i] == "(":
            simplified_str = simplified_str[: i - 1] + "(" + simplified_str[i:]
            simplified_str = simplified_str[:i] + "~" + simplified_str[i + 1 :]
            if temp_str[i + 2] == "^":
                simplified_str = simplified_str[: i + 2] + "v" + simplified_str[i + 3 :]
            elif temp_str[i + 2] == "v":
                simplified_str = simplified_str[: i + 2] + "^" + simplified_str[i + 3 :]
            simplified_str = simplified_str[: i + 3] + "~" + simplified_str[i + 4 :]
            temp_counter = 9
            for k in range(8, len_of_temp_str):
                simplified_str = (
                    simplified_str[:temp_counter]
                    + temp_str[k]
                    + simplified_str[temp_counter + 1 :]
                )
                temp_counter += 1

    return simplified_str


# ~(A^(BvC)) -> (~Av(~B^~C))
# propositional_formula = "~(A^(BvC))"
propositional_formula = "~(AvB)"
print("\nEnter a propositional formula: ", propositional_formula)
simplified_formula = simplify(propositional_formula)
print("Simplified formula: ", simplified_formula, "\n")
