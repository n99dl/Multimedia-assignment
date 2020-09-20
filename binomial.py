import math

def combination(n, k):
	if k == 0:
		return 1
	if n == k:
		return 1
	return combination(n - 1, k - 1) + combination(n - 1, k)

def prob(n, p, N):
	return combination(N, n) * p ** n * (1 - p) ** (N - n)

def infoMeasure(n ,p, N):
	return math.log2(prob(n ,p, N)) * (-1)
  
def sumProb(N, p):
	sum_prob = 0
	for i in range (0, N+1):
		sum_prob += prob(i, p, N)
	return sum_prob


def approxEntropy(N, p):
	approx = 0
	for i in range (0, N+1):
		approx += (-1.0 * prob(i, p, N) * math.log2(prob(i, p, N)))
	return approx
    
if __name__ == "__main__":
  print(approxEntropy(5, 0.5))