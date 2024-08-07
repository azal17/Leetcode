class Solution:
    def reverse(self, x: int) -> int:
        x_string = str(x)
        is_negative = x_string[0] == '-'
        if is_negative:
            x_string = x_string[1:]
        
        x_char = list(x_string)
        x_char.reverse()
        while x_char and x_char[0] == '0':
            x_char.pop(0)
        x_list_string = ''.join(x_char)
        if x_list_string == '':
            x_list_string = '0'
        x_int = int(x_list_string)
        if is_negative:
            x_int = -x_int
        if x_int < -2**31 or x_int > 2**31 - 1:
            return 0
        return x_int
