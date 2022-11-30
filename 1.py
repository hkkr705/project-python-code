# list of all destinations
from math import*
destination =['China','Singapore','Srilanka','Malaysia','Bangladesh']
# weight of corrsopponding destination
destinationwt=[0.073,0.02,0.075,0.073,0.0695]

goods =['fertilizer','coal','rice','iron','sand']  # list of all goods
# types of containers according to length
containerswt = {'20':21727,'40':26780,'45':29050,'48':32650}

# weight for corrosponding goods in all the given destinations

China = [0.461,0.532,0.383,0.635,0.421]
Singapore = [0.03,0.05,0.01,0.05,0.01]
Srilanka = [0.106,0.039,0.507,0.093,0.077]
Malaysia = [0.209,0.305,0.358,0.461,0.342]
Bangladesh = [0.066,0.177,0.285,0.033,0.335]

lambda1 = 0.4321        # priority factor for change in volume of container
lambda2 = 0.3210        # priority factor for destination
lambda3 = 0.1542        # priority factor stands for the goods which is shipping
lambda4 = 0.0927        # priority factor stands for company

# dictionary for accessing the list from user input
accessinglist = {"China": China,"Singapore":Singapore,"Srilanka":Srilanka}

# dictionary for list of shipping companies and their corrodponding weight
companywt={"Roy Shipping Agency":0.079,"Star Container Services":0.065,"Res Trans- Logis":0.042}
D=input('Enter the destination: ')
G=input('Enter the goods: ')
C=input('Enter the length of container(in ft): ')
W = int(input('Enter the weight of container(kg): '))
Company = input('Enter the name of shipping company: ')
wtchange=0
wtchange = W-containerswt[C]
wtchange = abs(wtchange)

# if there is weight change (kg) then the factor
if wtchange <=50 :
    wtfactor = 0.01
elif wtchange >50 and wtchange<=100:
    wtfactor = 0.07
elif wtchange >100 and wtchange<=200:
    wtfactor = 0.4
elif wtchange >200 and wtchange<=300:
    wtfactor = 0.6
else:
    wtfactor = 0.8

D1=destination.index(D)
D1=destinationwt[D1] # D1 is factor for destination
w1=goods.index(G)

# accessinglist[D][w1] is factor of goods
result=0
result=lambda1*wtfactor + lambda2*D1 + lambda3*(accessinglist[D][w1]) + lambda4*companywt[Company]
print('Change in weight of goods vs container is : %i kg'%wtchange)
print('The Value of R is : %.2f' %result)
if result<=0.3:
    print("Store to ship.")
else:
    print("Proceed to further check.")
