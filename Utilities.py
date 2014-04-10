import random

def genInitialGrid(cells, weight, height) :
	
	if weight*height < len(cells) :
		raise Exception("More cells than the grid supports!")


	fixed_locations = [[c.getX(),c.getY()] for c in cells if c.getStatus() == 'fixed']
	locations = [[x,y] for x in range (1,weight+1) for y in range(1,height+1) if [x,y] not in fixed_locations]

	for cell in cells :
		
		if cell.getStatus is 'fixed' :
			continue

		if len(locations) > 0 :
			pos = random.randint(0, len(locations)-1)
		else :
			break

		x, y = locations[pos]
		del locations[pos]

		cell.setX(x)
		cell.setY(y)

	return cells

def genNeighbor(cells) :

	#get all cells with status different than fixed
	unfixedcells = [c for c in cells if c.getStatus() is not 'fixed']
	
	if unfixedcells == [c for c in unfixedcells if c.getStatus() is 'moved'] or len([c for c in unfixedcells if c.getStatus() is 'free']) == 1 :
		map(lambda c : c.setStatus('free'), [c for c in unfixedcells])

	else :
		unfixedcells = [c for c in unfixedcells if c.getStatus() is 'free']
		
	c1, c2 = random.sample(unfixedcells, 2)
	c1.setStatus('moved')
	c2.setStatus('moved')
	ty = c1.getY()
	tx = c1.getX()
	c1.setX(c2.getX()) 
	c1.setY(c2.getY()) 
	c2.setX(tx) 
	c2.setY(ty) 

	return cells

def cost(cells, nets) :

	return 0