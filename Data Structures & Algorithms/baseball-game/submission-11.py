class Solution:
    
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        finalScore=0

        for i in range(len(operations)):
            if operations[i] == "+":
                sumOfTwo = int(record[-1]) + int(record[-2])
                record.append(sumOfTwo)
                finalScore += sumOfTwo
            elif operations[i] == "C":
                #record.pop()
                finalScore -= int(record.pop())
            elif operations[i] == "D":
                newScore = int(record[-1])*2
                record.append(newScore)
                finalScore += newScore
            else:
                record.append(int(operations[i]))
                finalScore += int(operations[i])
            

        #for j in range(len(record)):
            #finalScore += int(record[j])
        #    finalScore += record[j]

        return finalScore