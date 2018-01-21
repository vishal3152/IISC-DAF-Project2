

def sort(list):#this method definition
    i=0
    swap=False
    while i<len(list)-1:
        #print(list)
        if(list[i][0]>list[i+1][0]):#check for first char of pair
            swap=True
            list[i],list[i+1]=list[i+1],list[i]#swap
        elif(list[i][0]==list[i+1][0]):#is same first char then check for subsequent alphabet in the word and swap
            if(len(list[i])>len(list[i+1])):
                length=len(list[i+1])
            else:
                length=len(list[i])
            for pos in range(0,length-1):
                if(list[i][pos]>list[i+1][pos]):
                    swap=True
                    list[i],list[i+1]=list[i+1],list[i]
                    break
                
        i=i+1
       
    if(swap):#recusrion till the list is completely sorted
            sort(list)
    return list


nameList=['Vikas','Vishal']#input list

nameList=sort(nameList)# function invoke


print(nameList)




        
