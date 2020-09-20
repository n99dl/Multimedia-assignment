import math

def prob(n, p):
    return p*(1.0-p)**(n-1)

def infoMeasure(n, p):
    return math.log2(prob(n, p)) * (-1.0)

def sumProb(N, p):
	sum_prob = 0
	for i in range (1, N+1):
		sum_prob += prob(i, p)
	return sum_prob
    
def approxEntropy(N, p):
	approx = 0
	for i in range (1, N+1):
		approx += (-1.0 * prob(i, p) * math.log2(prob(i, p)))
	return approx
	
if __name__ == "__main__":
  print(approxEntropy(5, 0.5))