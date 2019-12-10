def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	res = []
	nb = 0
	restant = n
	while restant > 0: 
		for coin in sorted(denoms, reverse= True):
			if coin <= restant:
				nb += int(restant/coin)
				res.append(str(coin)*int(restant/coin))
				restant = restant%coin
	print(res)
	return nb
