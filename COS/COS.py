import math
import cmath

def signalFunction(N):
	numbers = []
	for n in range(0, N, 1):
		numbers.append(round(math.sin(2 * math.pi * n / N) + math.cos(7 * 2 * math.pi * n / N), 2))
	return numbers


def DFTFunc(k, numbers):
	result = 0;
	for n in range(0, len(numbers), 1):
		result += numbers[n] * math.e ** (complex(0, -1) * 2 * math.pi * k * n / len(numbers))
	return complex(round(result.real, 2), round(result.imag, 2))
	
def DFT(numbers):
	result = []
	for k in range(0, len(numbers), 1):
		result.append(DFTFunc(k, numbers))
	return result

def getComplexAbs(complexNumbers):
	result = []
	for i in range(len(complexNumbers)):
		result.append(round(abs(complexNumbers[i]), 2))
	return result

def getComplexPhase(complexNumbers):
	result = []
	for i in range(len(complexNumbers)):
		result.append(round(cmath.phase(complexNumbers[i])/math.pi, 2))
	return result

def printWithRowNumber(arr):
	for i in range(0, len(arr), 1):
		print("{0}) {1}".format(i, arr[i]))

numbers = signalFunction(16)
result = DFT(numbers)

print("Function values:\n")
printWithRowNumber(numbers)
print("\nDFT values:\n")
printWithRowNumber(result)

args = getComplexAbs(result)
phases = getComplexPhase(result)

print("\nAbs:\n")
printWithRowNumber(args)
print("\nPhase:\n")
printWithRowNumber(phases)

