import random

def randomBit():
        if random.uniform(0,1) < 0.5 :
                return '1'
        else:
                return '0'

def qOne(bits_x: str, chi, repetitions):
        bits = list(bits_x)
        for j in range(0, repetitions):
                mutationRate = chi/float(len(str(bits_x)))
                for i in range(0, len(str(bits_x))):
                        if (random.uniform(0,1) < mutationRate):
                                if (int(bits[i]) == 1):
                                        bits[i] = '0'
                                else:
                                        bits[i] = '1'
                print(bits)

def mutate(bits_x, chi):
        bits = list(bits_x)
        mutationRate = chi/float(len(str(bits_x)))
        for i in range(0, len(str(bits_x))):
                if (random.uniform(0,1) < mutationRate):
                        if (int(bits[i]) == 1):
                                bits[i] = '0'
                        else:
                                bits[i] = '1'
        return "".join(bits)
        
def qTwo(bits_x, bits_y, repetitions):
        lbits_x = list(bits_x)
        lbits_y = list(bits_y)
        bits = lbits_x
        for i in range(0, repetitions):
                for j in range(0, len(lbits_x)):
                               if bits_x[j] != bits_y[j]:
                                       bits[j] = randomBit()
                print(bits)

def crossover(bits_x, bits_y):
        lbits_x = list(bits_x)
        lbits_y = list(bits_y)
        bits = lbits_x
        for j in range(0, len(lbits_x)):
                       if bits_x[j] != bits_y[j]:
                               bits[j] = randomBit()
        return "".join(bits)

                
def qThree(bits_x):
        lbits_x = list(bits_x)
        value = 0
        for i in range(0, len(lbits_x)):
                value += int(lbits_x[i])
        #print(value)
        return value

def qFour(k, population, repetitions):
        poplist = population.split()
        for j in range(0,repetitions):
                tournSet = []
                for i in range(0,k):
                        tournSet.append(poplist[random.randint(0,len(poplist)-1)])
                print("Tournament for " + str(tournSet))
                maximum = 0
                winner = ""
                for i in range(0,k):
                        if qThree(tournSet[i]) >= maximum:
                                winner = tournSet[i]
                                maximum = qThree(tournSet[i])
                print(winner)

def tournSelection(k, poplist):
        tournSet = []
        for i in range(0,k):
                tournSet.append(poplist[random.randint(0,len(poplist)-1)])
        maximum = 0
        winner = ""
        for i in range(0,k):
                if qThree(tournSet[i]) >= maximum:
                        winner = tournSet[i]
                        maximum = qThree(tournSet[i])
        return winner

def generateRandomBitString(nbits):
        bitString = ""
        for i in range(0, nbits):
                if (random.uniform(0,1) < 0.5):
                        bitString += "0"
                else:
                        bitString += "1"
        return bitString
        
                
def qFive(n, chi, k, arg_lambda, repetitions):
        poplist = []
        t = 0
        for i in range(0, arg_lambda):
                poplist.append(generateRandomBitString(n))
        for t in range(0, repetitions):
                optimalfound = False
                while not optimalfound:
                        newpoplist = []
                        for i in range(0, arg_lambda):
                                x = tournSelection(k, poplist)
                                y = tournSelection(k, poplist)
                                mx = mutate(x, chi)
                                my = mutate(y, chi)
                                child = crossover(mx, my)
                                if qThree(child) == n:
                                        optimalfound = True
                                        fbest = qThree(child)
                                        xbest = child
                                newpoplist.append(child)
                        t += 1
                        print("Gen " + str(t) + ": " + str(newpoplist))
                print(str(n) + "     " + str(chi) + "     " + str(k) + "       " + str(t) + "       " + str(fbest) + "   " + str(xbest)) 
