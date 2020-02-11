# import all classes
from Passangers_sub_class import Passengers
from People_class import People
from Plane_sub_class import Plane
from Flight_class import Flight
# start empty list of what you want to track
    # airplanes
    # passengers -need to asign one person to flight
    # flights- need to lista all filghts


# Initialize 6 passengers (append to list)
passenger_list = []
passengers_1 =Passengers('Avraj', 'b1kjbf-098')
passengers_2 =Passengers('Alex', 'b1kjbf-098')
passengers_3 =Passengers('Lalia', 'b1kjbf-098')
passengers_4 =Passengers('Hamza', 'b1kjbf-098')
passengers_5 =Passengers('Jack', 'b1kjbf-098')
passengers_6 =Passengers('Nithin', 'b1kjbf-098')

passenger_list.append(passengers_1)
passenger_list.append(passengers_2)
passenger_list.append(passengers_3)
passenger_list.append(passengers_4)
passenger_list.append(passengers_5)
passenger_list.append(passengers_6)

# print(Passengers.get_name(passenger_list[0]))# print passenger list (only prints one)
# print(Passengers.get_passenger_id(passenger_list[1]))# print passenger list (only prints one)

# initialize 3 plane (append to list)
plane_list = []
plane_1 = Plane('JHyg8653256','British Airways')
plane_2 = Plane('809nmb53256','India Airways' )
plane_3 = Plane('JHyg8653256','China Airline' )

plane_list.append(plane_1)
plane_list.append(plane_2)
plane_list.append(plane_2)

print(Plane.get_air_line(plane_list[0]))
print(Plane.get_plane_serial(plane_list[0]))
# create 3 flights (append to list)
flight_list = []
flight_1 = Flight('GH65789', '01/01/20, 9:00', 'Avraj')
flight_2 = Flight('GH97339', '23/01/20, 9:00', 'Jack')
flight_3 = Flight('GH20489', '05/01/20, 9:00', 'Alex')

# add 2 passengers to each flight

# list passengers in one flight

# get the list form the flight and save is in a variable,