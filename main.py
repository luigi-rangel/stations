import csv
import ast

class Station:
    def __init__(self, name, connections) -> None:
        self.name = name
        self.connections = connections

class Line:
    def __init__(self, name, filename) -> None:
        self.name = name

        file = open(filename, "r", encoding="utf-8")
        plan = list(csv.reader(file, delimiter=";"))
        file.close()

        self.stations = [Station(row[0], ast.literal_eval(row[1])) for row in plan]
        self.length = len(self.stations)        
    
    def get_first_station(self, direction = 1):
        return self.stations[::direction][0]
    
    def get_last_station(self, direction = 1):
        return self.stations[::direction][-1]

    def get_next_station(self, station, direction = 1):
        i = self.stations.index(station)

        if i + direction < 0 or i + direction >= self.length: return None

        return self.stations[i + direction]
    
rer_b_2 = Line("RER B - branche 2", "plans/RER-B-b2.csv")
direction = -1

cur = rer_b_2.get_first_station(direction)
last = rer_b_2.get_last_station(direction)

print(f"What are the stations of the line {rer_b_2.name} in the direction {last.name}?")

while(cur):
    attempt_name = input("name: ")
    if attempt_name != cur.name: 
        print(f"The right answer was: {cur.name}")
        break

    cur = rer_b_2.get_next_station(cur, direction)