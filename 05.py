#use a Debugger 
def mutate(a_list):
    b_list=[]
    for item in a_list:
        new_item=item*2
        b_list.append(new_item)
    print(b_list)

c_list=[1,2,3,4,5,6]
mutate(c_list)
