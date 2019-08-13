# I believe the author of this problem wants us to perform digit-wise
# multiplication, but there's no point not to convert the string to int at the
# beginning. I'm gonna ignore the note.

class Solution(object):
    def stringToInt(self, num):
        ans = 0
        zero = ord("0")
        for digit in num:
            ans *= 10
            realDigit = ord(digit) - zero
            ans += realDigit
        return ans
    
    def intToString(self, realNum):
        if realNum == 0:
            return "0"
        ans = ""
        zero = ord("0")
        while realNum:
            digit = realNum % 10
            realNum /= 10
            ans = chr(digit + zero) + ans
        return ans

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        realNum1 = self.stringToInt(num1)
        realNum2 = self.stringToInt(num2)
        return self.intToString(realNum1 * realNum2)
