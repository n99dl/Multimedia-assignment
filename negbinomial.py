import math

def combination(n, k):
	if k == 0:
		return 1
	if n == k:
		return 1
	return combination(n - 1, k - 1) + combination(n - 1, k)

def prob(n, p, r):
	return combination(n - 1, r - 1) * p ** r * (1 - p) ** (n - r)

def infoMeasure(n ,p, r):
	return math.log2(prob(n ,p, r)) * (-1)
  
def sumProb(N, p, r):
	sum_prob = 0
	for i in range (r, N+1):
		sum_prob += prob(i, p, r)
	return sum_prob


def approxEntropy(N, p, r):
	approx = 0
	for i in range (r, N+1):
		approx += (-1.0 * prob(i, p, r) * math.log2(prob(i, p, r)))
	return approx
    
if __name__ == "__main__":
  print(approxEntropy(5, 0.5, 3))