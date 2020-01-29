"""
thomas dufour
dufour.thomas@hotmail.fr
technical challenge originally done for Pearl Bridge Partners.

-------------------
instructions:

You live in a remote settlement where bread sellers come through periodically at irregular intervals.
Whenever you buy fresh bread, it lasts for 30 days until it becomes too stale to eat. 
Your family eats one loaf of bread per day.
You are given a calendar of when the bread sellers will be visiting over the coming days 
and the price each bread seller will charge per loaf. You currently have 10 fresh loaves, 
and at the end of the calendar you'll get a bunch of free bread, so you won't need to 
have any left on hand. Write a function that tells you how much bread to buy from each of the sellers

-------------------  

notes:

It is needed to buy at least total_days-10 loafs of gas.
But no more than toal_days in order to minimize the coast.

mathematically, the problme is minimizying total_price,
with total_price = breads dot prices'
satisfying conditions:
	breads[i] <= 30
	breads[i] >= stocks - delta days
	and sum(breads) = total_days-10

startegy: while planning to buy from the cheapest to the least, 
	buy as much cheap bread as you can/need.

the algorithm filled the result array (aka breads) in order of the cheapest 
sellers, and plan to buy just what is needed or stock is the next_seller is more expensive.


O(n^2) in time 

"""


def calculate_purchasing_plan(total_days, sellers):
    # if there are already enough breads, return None
    need = total_days-10
    if need <= 0: 
        return None
    
    # initialization at 0 because we have not planned anything yet.
    breads = [0 for day in sellers] 
    
    # the idea is to buy as much as possible to the cheapest.
    # to do so, I sorted the sellers by price and then do the plan for each.
    for cheapest in sorted(sellers, key= lambda seller: seller[1]):
        n = sellers.index(cheapest)
    
        # next seller planned on the calendar
        next_seller = [elem for elem in sellers
            if elem[0] > sellers[n][0]
        ]
        next_seller =next_seller[:1]
        # handle last seller on calendar
        if not next_seller:
            next_seller = [total_days]
            max_need = min(
                30, 
                next_seller[0] - cheapest[0]
            )
            # it has be less than 30 else, we starve :-(
            
        else :
            next_seller = next_seller[0]
            # if next seller is cheaper than today' seller, we just need the time delta 
            if next_seller[1] < cheapest[1]:
                max_need = next_seller[0] - cheapest[0]
                
            # is he is more expensive than today' seller, buy as many as possible
            else :
                max_need = max(
                    30, 
                    next_seller[0] - cheapest[0]
                )
        # stocks are all the bread we had - what we ate
        stocks = max(sum(breads[:n]) +10 - sellers[n][0], 0)
        breads[n] = max( 
            max_need- stocks,
            0
        )
    return breads