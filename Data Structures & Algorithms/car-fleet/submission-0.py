class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        per_car = []
        for i in range(len(speed)):
            per_car.append([position[i],speed[i]])
        per_car.sort()
        per_car.reverse()

        fleets = 0
        current_fleet = 0 
        i = 0
        stack = []
        while i < len(per_car):
            if current_fleet == 0:
                current_fleet+=1 
                stack.append((target-per_car[i][0])/per_car[i][1])
                i += 1
                fleets +=1 
                continue
            
            arrival_time = (target-per_car[i][0])/per_car[i][1]
            if arrival_time <= stack[-1]:
                current_fleet +=1 
            else:
                stack.append((target-per_car[i][0])/per_car[i][1])
                fleets+=1

            i+=1 

        return fleets

