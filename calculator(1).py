"""
file: calculator.py
calculator with four simple operations
"""
def input_num(prompt,datatype_for_input):
    """
    prompt the user for a numeric input
    prompt again if the input is not numeric
    return an integer or a float
    """
    while True:
        # strip() removes any leading or trailing whitespace
        num_str = input(prompt).strip()
        num_flag = True
        for c in num_str:
            # check for non-numerics
            if c not in datatype_for_input:
                num_flag = False
                print ("Incorrect number. Please try again or press ctrl+c to exit")
                break
        if num_flag:
            break
    # a float contains a period (US)
    if '.' in num_str:
        return float(num_str)
    else:
        return int(num_str)

    
def result(first_number,operator,second_number):
    """
    return result of math operation
    """
    operator_types = {1 : first_number + second_number,
                      2 : first_number - second_number,
                      3 : first_number * second_number,
                      4 : first_number / second_number
    }
    result_inDef = operator_types.get(operator)
    return result_inDef
    
    
print ('Welcome to Calculator')
 
first_number = input_num("Input first number(like 2 or 2.0)-->",'+-.0123456789')
operator = input_num("Input a number equal to math operator 1(+), 2(-), 3(*), 4(/) -->",'1234')
second_number = input_num("Input second number(like 2 or 2.0)-->",'+-.0123456789')

assert second_number != 0, "You can't divide into zero"

result_inProgramm = result(first_number,operator,second_number)
print (result_inProgramm)
print ("Thank you for using Calculator. Bye")
