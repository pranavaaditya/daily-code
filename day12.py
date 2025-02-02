# Alice needs to choose between two taxi services—Online Taxi and Classic Taxi—for her commute. Each taxi has a different cost structure: Online Taxi charges a base rate for a set distance and a per-km rate thereafter, while Classic Taxi considers base fare, speed-based cost, and distance-based charges. The goal is to calculate the total cost for both services and decide which is cheaper. If costs are the same, Online Taxi is preferred.

import math

D = int(input()) 
Oc, Of, Od = map(int, input().split())
Cs, Cb, Cm, Cd = map(int, input().split()) 

online_cost = Oc if D <= Of else Oc + (D - Of) * Od
classic_cost = Cb + math.ceil(D / Cs) * Cm + D * Cd
print("Online Taxi" if online_cost <= classic_cost else "Classic Taxi")
