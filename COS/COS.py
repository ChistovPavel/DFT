import math
import cmath

def getRadianAngle(n, N, additionalVal):
	val = ((additionalVal * 2 * n) % N)

	if (val == 0 and n != 0):
		return 1
	else:
		return val/N

def signalFunction(N):
	numbers = []
	for n in range(0, N, 1):
		numbers.append(round(math.sin(getRadianAngle(n, N, 1) * math.pi) + math.cos(getRadianAngle(n, N, 7) * math.pi), 2))
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
		result.append(abs(complexNumbers[i]))
	return result

def getComplexPhase(complexNumbers):
	result = []
	for i in range(len(complexNumbers)):
		result.append(round(cmath.phase(complexNumbers[i])/math.pi, 2))
	return result

numbers = signalFunction(16)
result = DFT(numbers)

print("numbers:\n")
print(numbers)
print("\nresult:\n")
print(result)

args = getComplexAbs(result)
phases = getComplexPhase(result)

print("\nArgs:\n")
print(args)
print("\nPhases:\n")
print(phases)

