# we need to start from the leftmost digit and work our way to the right
class Solution:
    def romanToInt(self, s: str) -> int:
        # create a dictionary to store the values of the roman numerals
        roman_dict = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # create a variable to store the value of the roman numeral
        roman_value = 0
        # loop through the string
        for i in range(len(s)-1):
            # get the value of the current roman numeral
            current_value = roman_dict[s[i]]
            # check if the current value is less than the next value
            if current_value < roman_dict[s[i+1]]:
                # subtract the current value from the total value
                roman_value -= current_value
            else:
                # add the current value to the roman value
                # this is normal cases
                roman_value += current_value
        # since we didn't check the last value, we need to add it to the total value
        return roman_value + roman_dict[s[-1]]
