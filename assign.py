def tutions(sem1, sem2):   
    paid = sem1+sem2
    return paid
    #print(paid)
tutions(1.3,1.5)  

def clearance(yr1, yr2):
    cleared = int(tutions(1.3,1.5) + (yr1+yr2))
    return cleared
    #print(cleared)
clearance(1000, 1.85)  

def totalInvoice():
    amountDue = clearance(1000, 1.85)
    amountPaid = amountDue - 50
    print(amountPaid)
totalInvoice()    
      