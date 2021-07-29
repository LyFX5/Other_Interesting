def deside(a,b,c,d,e):
    q = sorted([a,b,c])
    p = sorted([d,e])
    if(q[0] == q[1]) and (p[0] < q[0]):
        return "No"
    else:
        delta2 = q[0]**2 + q[1]**2
        delta = delta2**(1/2)
        if(delta <= p[0]):
            return "Yes"
        else:
            pred1 = (q[0] <= p[0]) and (q[1] <= p[1])
            pred2 = (q[1] <= p[0]) and (q[0] <= p[1])
            if(pred1 or pred2):
                return "Yes"
            else:
                if((delta > p[0]) and (delta < p[1])):
                    #print("Вот это поворот")
                    return "No"
                else: # delta >= p[1]
                    alfa = (p[1] - (delta2 - p[0]**2)**(1/2))/2
                    beta = (p[0] - (delta2 - p[1]**2)**(1/2))/2
                    if((alfa**2 + beta**2)**(1/2) >= q[0]):
                        return "Yes"
                    else:
                        return "No"
                    

abc = input()
de = input()
abcar = abc.split(" ")
dear = de.split(" ")
 
a = int(abcar[0])
b = int(abcar[1])
c = int(abcar[2])
d = int(dear[0])
e = int(dear[1])
 
print(deside(a,b,c,d,e))
