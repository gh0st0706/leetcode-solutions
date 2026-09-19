class Solution(object):
    def checkOverlap(self, radius, xCentre, yCentre, x1, y1, x2, y2):
        if xCentre < x1:
            closestX = x1
        elif xCentre > x2:
            closestX = x2
        else: 
            closestX = xCentre

        if yCentre < y1:
            closestY = y1
        elif yCentre > y2:
            closestY = y2
        else:
            closestY = yCentre
        
        dx = xCentre - closestX
        dy = yCentre - closestY

        distanceSquared = dx**2 + dy**2

        return distanceSquared <= radius **2
        
        