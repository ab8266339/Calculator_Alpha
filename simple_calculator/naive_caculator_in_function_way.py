import re

#---------------------input



#

def initialize():
    
    add_words = ['add', 'plus']
    subtract_words = ['subtract','minus']
    level_1_operators_list = add_words + subtract_words
    level_2_operators_list = []
    #level_2_operators_list = ['mutiply', 'divide']

    operators_seq_validation_list = []
    operators_seq_validation_list.append(level_2_operators_list)
    operators_seq_validation_list.append(level_1_operators_list)

    operators_list = level_1_operators_list + level_2_operators_list
    operators_set = set(operators_list)
    
    re_operators = ''
    for i in operators_set:
        re_operators = re_operators + "|{}".format(i)
        re_operators = re_operators[1:]
    #print (operators)
    return add_words, subtract_words , operators_seq_validation_list, operators_list, operators_set, re_operators





def get_cleaned_value_list_and_user_operater(raw_string, operators):
    value_list_raw = raw_string.split(' ')
    value_list = []
    user_operators = []
    for word in value_list_raw:
        try:
            number = int(word)
            value_list.append(number)
        except ValueError:
            if word in operators:
                value_list.append(word)
                user_operators.append(word)
    return value_list, user_operators

def operators_validation(valid_operators_set, user_operators):
    if not valid_operators_set.intersection(set(user_operators)):
        return False
    else:
        return True


def simple_calculate(num1, num2, operator, operator_index, add_words, subtract_words ):
    if operator in add_words:
        return (num1 + num2)
    elif coperator in subtract_words:
        return (num1 - num2)
    #TODO
    else:
        pass
    

def arithmetic(input_string):
    initialize()
    add_words, subtract_words , operators_seq_validation_list, operators_list, operators_set, re_operators = initialize()
    value_list,user_operators = get_cleaned_value_list_and_user_operater(input_string, operators_set)

    #TODO raise error
    if operators_validation(operators_set, user_operators):
        pass
    else:
        pass
    #----------------
    
    if len(user_operators) > 1:
        #TODO
        pass

    elif len(user_operators) == 1:
        operator = user_operators[0]
        operator_index = value_list.index(operator)
        num1 = value_list[operator_index - 1]
        num2 = value_list[operator_index + 1]
        cal_result = simple_calculate(num1, num2, operator, operator_index, add_words, subtract_words )
        
    return cal_result



#test
intent = {
      "name": "Add",
      "slots": {
        "number": {
          "name": "number",
          "value": "1 plus 2"
        }
      }
    }
input_string = intent['slots']['number']['value']
b = arithmetic(input_string)
