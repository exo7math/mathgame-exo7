
# Landscape generation 1D
# Loop version

import matplotlib.pyplot as plt
import random



n = 9
N = 2**n # N+1 values
Ha = 0   # initial value for start
Hb = 1   # initial value for end
h = 3.0    # max variation for first middle point
r = 0.8    # rugosity (lower is higher!)
random.seed(1001)  # for reproducibility

hauteurs = [0] * (N+1) 
hauteurs[0] = Ha
hauteurs[N] = Hb

for i in range(n):
    k = 2**(n-i-1)
    x = 0
    for j in range(2**i):
        variation = h/(2**(r*i)) * (2*random.random()-1)
        hauteurs[x+k] = (hauteurs[x] + hauteurs[x+2*k])/2 + variation
        x = x + 2*k


ax = plt.subplot(1,1,1)
plt.plot(hauteurs)


# plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.95, hspace=1.0,wspace=0.5)
plt.axis('off')
ax.set_ylim([-0.5, 3.5])
plt.tight_layout()
# plt.savefig('landscape-05-07.png')
plt.show()


# lanscape-01
# n = 7    
# N = 2**n # N+1 values
# Ha = 0   # initial value for start
# Hb = 1   # initial value for end
# h = 1    # max variation for first middle point
# r = 0.9    # rugosity (lower is higher!)
# random.seed(1234)  # for reproducibility

# lanscape-02
# n = 4    
# N = 2**n # N+1 values
# Ha = 0   # initial value for start
# Hb = 1   # initial value for end
# h = 1    # max variation for first middle point
# r = 0.7    # rugosity (lower is higher!)
# random.seed(1236)  # for reproducibility


# lanscape-03
# n = 10
# N = 2**n # N+1 values
# Ha = 1   # initial value for start
# Hb = 0   # initial value for end
# h = 1    # max variation for first middle point
# r = 0.8    # rugosity (lower is higher!)
# random.seed(2022)  # for reproducibility


# lanscape-04
# n = 9
# N = 2**n # N+1 values
# Ha = 0   # initial value for start
# Hb = 0   # initial value for end
# h = 1    # max variation for first middle point
# r = 0.8    # rugosity (lower is higher!)
# random.seed(2023)  # for reproducibility

# ax.set_ylim([-1, 1])


# lanscape-05
# n = 9
# N = 2**n # N+1 values
# Ha = 0   # initial value for start
# Hb = 1   # initial value for end
# h = 3.0    # max variation for first middle point
# r = 0.8    # rugosity (lower is higher!)
# random.seed(1001)  # for reproducibility
# ax.set_ylim([-0.5, 3.5])

# lanscape-06
n = 8
N = 2**n # N+1 values
Ha = 0   # initial value for start
Hb = 1   # initial value for end
h = 1.0    # max variation for first middle point
r = 0.2   # rugosity (lower is higher!)
random.seed(1003)  # for reproducibility