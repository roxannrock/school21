p = 23
g = 19   

alice = 3  #secret который был сгенерировао рандомом
bob = 5

A = g**alice % p    #etim oni obmenivautsa
B = g**bob % p

a = B**alice % p     #obshiy klyuch
b = A**bob % p