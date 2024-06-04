import math

class FooPhysics:
    #If user wants to initialize arguments or set up
    #add variable in here 
    def __init__(self):
        """
        if user need needs to initialize certain attributes or set up
        you can add something in here.
        """
        pass
    #Calculate the volume of a sphere. The argument is radius
    def calculate_volume_sphere(self, radius):
        """
        Argument 'radius' can take any numeric value using parameterization.
        Returns volume of sphere.
        """
        if radius < 0:
            raise ValueError("Negative number not allowed.")
        
        #formula for volume of Sphere
        #V = 4/3 π r³
        #Using import math
        volume = (4/3) * math.pi * radius**3 
        return volume

# Main function to declare radius variable
#Example to run the code
if __name__ == "__main__":
    foo = FooPhysics()
    radius = 3
    radius_f = 65.12
    volume = foo.calculate_volume_sphere(radius)
    volume_f = foo.calculate_volume_sphere(radius_f)
    print("Radius value: {}\nVolume of sphere: {}\n".format(radius,volume))
    print("Radius value: {}\nVolume of sphere: {}".format(radius_f,volume_f))