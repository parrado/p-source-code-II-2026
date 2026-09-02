def computeAverage(l):    
    acc=0.0 # Local var
    for s in l:
        acc=acc+s

    #average=acc/nGuests # Better
    average=acc/len(l) # Local var
    return average



nGuests=int(input('Enter number of guests: '))

reviews=[]
for g in range(nGuests):
    while True:
        stars=int(input(f'Enter number of stars for guest {g+1}: '))   
        if stars>=1 and stars<=5:
            reviews.append(stars)
            break


avg=computeAverage(reviews)
print(f'You got {avg} stars')


