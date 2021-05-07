

class TrafficLight:
    """
    There is an intersection of two roads. First road is road A where cars travel from North to South in direction 1 and from South to North in direction 2. 
    Second road is road B where cars travel from West to East in direction 3 and from East to West in direction 4.

    There is a traffic light located on each road before the intersection. A traffic light can either be green or red.

    Green means cars can cross the intersection in both directions of the road.
    Red means cars in both directions cannot cross the intersection and must wait until the light turns green.
    The traffic lights cannot be green on both roads at the same time. That means when the light is green on road A, it is red on road B and when the light is green on road B, it is red on road A.

    Initially, the traffic light is green on road A and red on road B.
     
    When the light is green on one road, all cars can cross the intersection in both directions until the light becomes green on the other road.
    No two cars traveling on different roads should cross at the same time.

    Design a deadlock-free traffic light controlled system at this intersection.

    Implement the function carArrived(carId, roadId, direction, turnGreen, crossCar) where:
    carId is the id of the car that arrived.
    roadId is the id of the road that the car travels on.
    direction is the direction of the car.
    turnGreen is a function you can call to turn the traffic light to green on the current road.
    crossCar is a function you can call to let the current car cross the intersection.

    Example 1:
    Input: cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]

    Example 2:
    Input: cars = [1,2,3,4,5], directions = [2,4,3,3,1], arrivalTimes = [10,20,30,40,40]

        >>> main([1,3,5,2,4], [2,1,2,4,3], [10,20,30,40,50])
        Car 1 Has Passed Road A In Direction 2
        Car 3 Has Passed Road A In Direction 1
        Car 5 Has Passed Road A In Direction 2
        Traffic Light On Road B Is Green
        Car 2 Has Passed Road B In Direction 4
        Car 4 Has Passed Road B In Direction 3

        >>> main([1,2,3,4,5], [2,4,3,3,1], [10,20,30,40,40])
        Car 1 Has Passed Road A In Direction 2
        Traffic Light On Road B Is Green
        Car 2 Has Passed Road B In Direction 4
        Car 3 Has Passed Road B In Direction 3
        Car 4 Has Passed Road B In Direction 3
        Traffic Light On Road A Is Green
        Car 5 Has Passed Road A In Direction 1

    """
    def __init__(self):
        # Initial state: light_1 on Road A is green, light_2 on Road B is red.
        self.light_1 = "Green"
        self.light_2 = "Red"
    
    def turnGreen(self, roadId):
        self.light_1, self.light_2 = self.light_2, self.light_1
        if roadId == 1:
            print(f"Traffic Light On Road A Is Green") 
        else:
            print(f"Traffic Light On Road B Is Green")
        
    @staticmethod
    def crossCar(carId, roadId, direction):
        if roadId == 1:
            print(f"Car {carId} Has Passed Road A In Direction {direction}")
        else:
            print(f"Car {carId} Has Passed Road B In Direction {direction}")

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
    ) -> None:
        # The first car check if the light is green on its road.
        # If the light is green, call crossCar method to pass
        # Otherwise, call the turnGreen method first
        # when the light turns from red to green, call crossCar method to go
        if roadId == 1:
            if self.light_1 == "Red":
                self.turnGreen(roadId)
            self.crossCar(carId, roadId, direction)
        else:
            if self.light_2 == "Red":
                self.turnGreen(roadId)
            self.crossCar(carId, roadId, direction)

def get_roadId(direction):
    return 1 if direction in {1, 2} else 2

def main(cars, directions, arrivalTimes):   
    controller = TrafficLight()
    for i in range(len(cars)):        
        roadId = get_roadId(directions[i])
        controller.carArrived(
            cars[i],      
            roadId,       
            directions[i],
        )
        

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED! CONGRATS!***\n")
