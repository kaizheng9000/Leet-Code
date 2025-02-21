


filterCost = [2, 3, 4]

startDay = [1,1,2]

endDay = [2,3,4]

discountPrice = 6

def solve(filterCost, startDay, endDay, discountPrice):
    MOD = 10**9 + 7
    
    # Step 1: Create Events
    events = []
    for i in range(len(filterCost)):
        events.append((startDay[i], filterCost[i]))   # Start processing
        events.append((endDay[i] + 1, -filterCost[i])) # Stop processing
    
    # Step 2: Sort events by day
    events.sort()
    
    # Step 3: Process events using a Sweep Line approach
    prev_day = 0
    active_cost = 0
    min_cost = 0
    
    for day, cost in events:
        duration = day - prev_day  # Number of days the previous cost was active
        
        # Apply the minimum cost for the previous duration
        if duration > 0:
            min_cost += min(active_cost * duration, discountPrice * duration)
            min_cost %= MOD
        
        # Update the active filter cost
        active_cost += cost
        prev_day = day  # Move to the next event day
    
    return min_cost

    # dayCostMap = {}

    # imagesLength = len(filters)

    # for key in range(min(startDay), max(endDay) + 1):
    #     dayCostMap[key] = []
    
    # for day in range(min(startDay), max(endDay) + 1):
    #     # Which images need to be filtered on this day?
        

    #     # Sum up the cost of processing required images for this day
    #     # If the cost is more than the discount price, use the discount instead for the day

    
    # # Sum up all days in the map

    # print(dayCostMap)
    


print(solve(filterCost, startDay, endDay, discountPrice))
