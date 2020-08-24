import numpy as np

n_machine = 5
m_timeTable = [0]*n_machine

print(m_timeTable)

a = [2,3,4,5,6]
print(np.mean(a))

mu = 5
sigma = 0.15
for i in range(10):
    print(np.random.normal(mu,sigma))


count = 5
FE = 20

 outer:
while(count < FEs):
