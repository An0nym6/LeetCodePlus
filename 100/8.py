class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        # Remove whitespaces
        for i in range(len(string)):
            if string[i] != " ":
                string = string[i:]
                break
        # Empty check
        if not string:
            return 0
        # Check sign
        sign = 1
        if string[0] == "+":
            string = string[1:]
        elif string[0] == "-":
            sign = -1
            string = string[1:]
        # Get value
        val = 0
        for letter in string:
            if letter >= "0" and letter <= "9":
                val *= 10
                val += ord(letter) - ord("0")
            else:
                break
        val *= sign
        # Apply limits
        return max(-2147483648, min(2147483647, val))
