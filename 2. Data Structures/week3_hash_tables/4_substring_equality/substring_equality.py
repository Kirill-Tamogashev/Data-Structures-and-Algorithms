import sys

class Solver:

	def __init__(self, s):
		self.s = s
		self.len = len(s)
		self.h_1 = [0] * (self.len + 1)
		self.h_2 = [0] * (self.len + 1)
		self.x = 43
		self.p_1 = 1000000007
		self.p_2 = 1000000009
		self.precomputeHashes()
		


	def precomputeHashes(self):
		for i in range(1, self.len + 1):
			self.h_1[i] = self.x * self.h_1[i-1] % self.p_1 + ord(self.s[i - 1]) 
			self.h_2[i] = self.x * self.h_2[i-1] % self.p_2 + ord(self.s[i - 1]) 


	def ask(self, a, b, l):
		power = pow(self.x, l) % self.p_1
		H1_a = (self.h_1[a + l] - power * self.h_1[a]) % self.p_1
		H1_b = (self.h_1[b + l] - power * self.h_1[b]) % self.p_1
		H2_a = (self.h_2[a + l] - power * self.h_2[a]) % self.p_2
		H2_b = (self.h_2[b + l] - power * self.h_2[b]) % self.p_2
		return H1_a == H1_b and H2_a == H2_b


s = sys.stdin.readline()
q = int(sys.stdin.readline())
#s = input()
#q = int(input())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
#	a, b, l = map(int, input().split())
	print("Yes" if solver.ask(a, b, l) else "No")
