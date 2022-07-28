#Code written by Clovis Hatungimana for modeling the cockroach on a continuously expanding wire

import matplotlib.pyplot as plt
import numpy as np

# defining variables

Lt = [1000]   # the total length of the wire after stretch
Tt =[0]       # traveled distance after stretch
Rt = [1000]        # remaining distance after stretch

period_of_observation= 100  # time in seconds
# setting the values for t (time) as a list that will contain values from 0 to 100 seconds.
t=[0]
counter=1

while counter < period_of_observation:
    
    #calculating by regression the traveled length
    traveled_distance = (Tt[counter-1]+1)* (counter+1)/counter
    
    #storing the traveled distance in our list
    Tt.append(traveled_distance)
    
    #calculating by regression the remaining length
    remaining_distance= (1+counter)*(Lt[0])-Tt[counter]
    
    new_total_length=(counter+1)*Lt[0]
    
    #Storing lists of values
    Lt.append(new_total_length)
    
    Rt.append(remaining_distance)
    
    t.append(counter)
    counter=counter+1
    

traveled_dist = np.array(Tt)
total_lengt = np.array(Lt)

ratio = traveled_dist/total_lengt

#print ("L values:\n",Lt)
print()
#print("t values:\n",t)
print()
print("total length:", Lt)
print()
#print("remaining dist", Rt)
print()
print("traveled dist", Tt[counter-1])

#now we plot our values for the traveled and remaining distances

 # plotting our values
plt.plot(t, ratio,'g')   
#plt.plot(t, Lt,'r')      #total length
#plt.plot(t, Tt,'y')      #traveled distance
#plt.plot(t, Rt,'b')      # remaining distance

plt.title("Cockroach on a contuously expanding wire")
plt.xlabel('Time in seconds')
plt.ylabel('Distance in meters')
plt.legend({'ratio'})
#plt.legend({'Total length'})
#plt.legend({'Traveled distance'})
#plt.legend({'Remaining distance'})


plt.show()


