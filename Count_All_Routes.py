'''You are given: An array locations of distinct positive integers, 
where locations[i] represents the position of city i along a 1D map.
An integer start representing the starting city index.

An integer finish representing the destination city index.
An integer fuel representing the initial units of fuel available.

You may move from any city i to any other city j!=i, 
as long as you have enough fuel.The fuel cost to move from city i to 

city j is the absolute difference | locations[i] - locations[j] |
Your fuel must never go negative.You can visit the 
same city multiple times.

The route is counted as valid only if it ends at the finish city, 
regardless of remaining fuel.You are allowed to take 0 or more steps, 
as long as the fuel allows.

Objective: Return the total number of distinct valid routes 
from the starting city to the destination city using the given fuel. 

Since the result may be large, return it modulo 10^9 + 7'''

from functools import lru_cache
from typing import List
def all_routes(locations,start,finish,fuel):
    mod=10**9 +7
    n=len(locations)
    @lru_cache(None)  # Saves the output of dp(curr_city, remaining_fuel) 
    #so we never calculate it twice (memoization)
    def dp(cur_city,rem_fuel):
        # If fuel is negative, this route is invalid
        if rem_fuel < 0:
           return 0
        # If we reach the finish line, this state counts as 1 valid completed route.
    # Otherwise, it is counted as 0
        routes=1 if cur_city==finish else 0
        for nxt_city in range(n):
            if nxt_city!=cur_city:
               fuel_cost=abs(locations[cur_city]-locations[nxt_city])
               if rem_fuel>=fuel_cost:
                  routes=(routes + dp(nxt_city,rem_fuel-fuel_cost))%mod
        return routes
    return dp(start,fuel)

locations=list(map(int,input().split()))
input_line=list(map(int,input().split()))
start=input_line[0]
finish=input_line[1]
fuel=input_line[2]
print(all_routes(locations,start,finish,fuel))

'''Let's trace a tiny example step-by-step:locations = [1, 3] 
(City 0 is at position 1, City 1 is at position 3)
Distance between City 0 and City 1: | 1 - 3 | = 2 
start = 0
finish = 1
fuel = 4
We start our search call: dp(0, 4) (At City 0, with 4 fuel left)

Call 1: dp(0, 4)Is City 0 the finish city (City 1)? No 
routes = 0. Loop through possible next cities:
Try City 1:Cost = | 1 - 3 |= 2.
Fuel left = 4>=2, so we can travel!
We call dp(1, 2) (Fuel remaining: 4 - 2 = 2).

Call 2: dp(1, 2)Is City 1 the finish city (City 1)? Yes! 
routes = 1 (This means ending right here is 1 valid route: 0 -> 1).
Loop through possible next cities:Try City 0:Cost = | 3 - 1 | = 2.
Fuel left = 2>=2, so we can travel back!We call dp(0, 0)
(Fuel remaining: 2 - 2 = 0).

Call 3: dp(0, 0)Is City 0 the finish city (City 1)? No routes = 0.
Loop through possible next cities:Try City 1:Cost =| 1 - 3 | = 2.
Remaining fuel = 0 < 2(Not enough fuel!).Loop finishes 
with no available moves. Returns 0 back to Call 2.

Back in Call 2: dp(1, 2)
routes = 1 (from base check) + 0 (from Call 3) = 1.

Returns 1 back to Call 1

Back in Call 1: dp(0, 4)
routes = 0 (from base check) + 1 (from Call 2) = 1.

Returns 1.

Final Valid Route
In this simple trace, there was only 1 valid route:

City 0 -> City 1 (stops at destination with 2 fuel left).

(Note: Driving back to City 0 left us with 0 fuel, so we 
couldn't reach City 1 again, meaning 0 -> 1 -> 0 was not 
a completed valid route).'''
