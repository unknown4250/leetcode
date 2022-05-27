class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        #return command.replace("()", "o").replace("(al)", "al")
        
        res = ""
        idx = 0

        while idx < len(command):
            if command[idx] == "G":
                res += "G"
                idx += 1
            if command[idx:idx+2] == "()":
                res += "o"
                idx += 2
            if command[idx:idx+4] == "(al)":
                res += "al"
                idx += 4
        return res
        