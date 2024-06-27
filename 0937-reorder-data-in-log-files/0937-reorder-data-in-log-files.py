class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        for log in logs:
            seperatedLog = log.split(" ")
            identifier = seperatedLog[0]
            bodyLog = " ".join(seperatedLog[1:])
            isDigit = self.isDigitLog(seperatedLog[1:])
            if isDigit:
                digitLogs.append(log)
            else:
                letterLogs.append((bodyLog, identifier))

        letterLogs.sort()
        return [identifier + " " + log for log, identifier in letterLogs] + digitLogs
    
    def isDigitLog(self, seperatedLog: List[str]) -> bool:
        return "".join(seperatedLog).isnumeric()
