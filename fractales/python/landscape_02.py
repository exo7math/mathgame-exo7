
# Landscape generation 1D
# Recursive version


import matplotlib.pyplot as plt
import random

Ha = 0   # initial value for start
Hb = 1   # initial value for end
h = 1    # max variation for first middle point
r = 0.9    # rugosity (lower is higher!)

random.seed(1234)  # for reproducibility

def landscape(n,Hleft,Hright,h):
    if n == 0:
        return [Hleft,Hright]
    else:
        variation = h * (2*random.random()-1)
        Hmid = (Hleft + Hright)/2 + variation
        h = h/(2**r)
        landscape_left = landscape(n-1,Hleft,Hmid,h)
        landscape_right = landscape(n-1,Hmid,Hright,h)

        return landscape_left + landscape_right[1:]

hauteurs = landscape(2,Ha,Hb,h)
print(hauteurs)

ax = plt.subplot(1,1,1)
plt.plot(hauteurs)


# plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.95, hspace=1.0,wspace=0.5)
plt.tight_layout()
# plt.savefig('landscape-02-a.png')
plt.show()
