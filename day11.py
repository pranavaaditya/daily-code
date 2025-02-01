

#A group of students wants to visit a tour in some city. In total, the group has boys and girls. To do this, they need to stay in a hotel.

#Calculate the number of rooms you need to book in the hotel, if each hotel room hasseats, provided that the boys can not live with the girls in the same room.



import math

def solve():
    n, m, k = map(int, raw_input().split())
    
   
    rooms_boys = int(math.ceil(float(n) / k)) 
     # Use math.ceil to round up

   
    rooms_girls = int(math.ceil(float(m) / k))  
    # Use math.ceil to round up

   
    total_rooms = rooms_boys + rooms_girls
    
    print total_rooms
t = int(raw_input())
for _ in range(t):
    solve()

