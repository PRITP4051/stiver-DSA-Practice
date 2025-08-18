# #capicity to ship packages  within d days
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# ...existing code...
# 5th day: 10

# A cleaner helper function to calculate the number of days needed for a given capacity.
def time(weights, capacity):
    days_needed = 1
    current_load = 0
    for weight in weights:
        if current_load + weight > capacity:
            days_needed += 1
            current_load = weight
        else:
            current_load += weight
    return days_needed

def shipwithdays(weights, days):
    # The search space for the capacity is from the heaviest item
    # to the sum of all items. This is the key correction.
    low = max(weights)
    high = sum(weights)
    
    while low <= high:
        mid = (low + high) // 2
        
        if time(weights, mid) <= days:
            # This capacity might be the answer, but let's try for an even smaller one.
            # So, we eliminate the right half.
            high = mid - 1
        else:
            # This capacity is too small, we must increase it.
            # So, we eliminate the left half.
            low = mid + 1
            
    # 'low' will be the smallest capacity that works (the lower bound).
    return low

weights = [3, 2, 2, 4, 1, 4]
days = 3
print(f"The minimum capacity is: {shipwithdays(weights, days)}")

weights2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days2 = 5
print(f"The minimum capacity is: {shipwithdays(weights2, days2)}")