# importing important libraries
import numpy as np # numpy library for high-level mathematical operations functions
import matplotlib.pyplot as plt # matplotlib library for draw figure
import math # math library for mathematical basic operations like sin, cos, pi 

# defining the Pde variables
lowercase_lambda = 0.71420 # lowercase lambda is ( λ ) equal 0.71420
lowercase_alpha = 100 # lowercase alpha is ( α ) equal 100
lowercase_gamma = lowercase_lambda / lowercase_alpha # lowercase_gamma is ( γ ) equal lowercase_lambda(λ) division lowercase_alpha(α)
lowercase_phi = 0.313 # lowercase phi is ( φ )
Z = 1000 # Z equal 1000
b = 10 # b equal 10
R = (b / (lowercase_phi**(1/3)) ) # R is b division lowercase_phi power 1/3
n0 = 1 # n0 equal 1

h = 0.25 # the change in r
r = np.arange(0,1+h,h) # set r values
boundary_conditions = [0,0] # initialize boundary conditions
initial_conditions = 0 # initialize initial conditions

L = len(r) # L is length of r
Y = np.zeros((L,b)) # initialize Y matrix
Y[0,:15] = boundary_conditions[0] # setting the initial Bcs
Y[0,lowercase_alpha:Z] = boundary_conditions[1] # setting the final Bcs
Y[:,0] = initial_conditions # setting the initial condition
factor = 1/h**2 # calculate the change in r

# defining the pde equation using the central difference method
for j in range(1,L): # steps is from 1 to L
  for i in range(1,L-1): # steps is from 1 to L - 1
    # writing the pde equation converted by central difference method
    Y[i,j] = -max(r)/2*(factor*(Y[i+1,j] - 2*Y[i,j] +Y[i-1,j])+4*math.pi*lowercase_gamma*n0*math.exp(-Y[0,0])) 

# Plotting the Y solutions
for i in range(L): # The steps is from 0 to L
  plt.plot(r,Y[:,i]) # plot Y Axis
plt.title("The Y solution for: '0 < r < alpha(α)' (Blue) and 'alpha(α) < r < R' (Purple)\n")  # The title of plot
plt.xlabel('distance [r]') # The x label text
plt.ylabel('Y solution') # The y label text
plt.show() # show the plt
