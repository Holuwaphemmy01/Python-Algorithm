
def task1(number):
    string_number=''
    string_number += '('
    for index in range(3):
        string_number += str(number[index])
    string_number += ')'
    string_number += " "
    for index in range(3):
        string_number += str(number[index+3])
    string_number += "-"
    for index in range(4):
        string_number += str(number[index+6])
    return string_number







    


