def solution(my_string, is_prefix):
    if len(is_prefix) > len(my_string):
        return 0
    else:
        string_prefix = my_string[:len(is_prefix)]
        if string_prefix == is_prefix:
            return 1
        else:
            return 0