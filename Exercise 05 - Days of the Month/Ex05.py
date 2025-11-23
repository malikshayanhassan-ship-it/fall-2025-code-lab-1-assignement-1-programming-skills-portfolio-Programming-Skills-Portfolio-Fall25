guest_list=[]
def add_guest(name):
    name=str(input("Enter the name of the guest: "))
    guest_list.append(name)
    print(f"{name} has been added to the guest list.")


for i in range(5):
    add_guest(guest_list)

print("Final Guest List:",guest_list)
   
      
