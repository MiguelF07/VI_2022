import csv
import geopandas as gpd

from geopy.geocoders import Nominatim

def main():
    print("1")
    locator = Nominatim(user_agent="myGeocoder")
    print("2")

    with open('airplane_crashes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif line_count == 1:
                print(f'\tIndex : {row[0]}\n Date : {row[1]}\n Time : {row[2]}\n Location : {row[3]}\n Operator : {row[4]}\n Flight # : {row[5]}\n Route : {row[6]}\n Type : {row[7]}\n Registration : {row[8]}\n cn/In : {row[9]}\n Aboard : {row[10]}\n Fatalities : {row[11]}\n Ground : {row[12]}\n Summary : {row[13]}.')
                line_count += 1
            else:
                #print(f'\tindex is {row[0]}, Date is {row[1]}, Time is {row[2]}, Location is {row[3]}, Operator is {row[4]}, Flight # is {row[5]}, Route is {row[6]}, Type is {row[7]}, Registration is {row[8]}, cn/In is {row[9]}, Aboard is {row[10]}, Fatalities is {row[11]}, Ground is {row[12]}, Summary is {row[13]}.')
                # location = locator.geocode(row[3])
                #print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
                # location = locator.geocode(row[3])
                # print(row[3])
                # if location is not None:
                #     print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
                line_count += 1
        print(f'Processed {line_count} lines.')

#  Index : 0
#  Date : 09/17/1908
#  Time : 17:18
#  Location : Fort Myer, Virginia
#  Operator : Military - U.S. Army
#  Flight # : 
#  Route : Demonstration
#  Type : Wright Flyer III
#  Registration : 
#  cn/In : 1
#  Aboard : 2.0
#  Fatalities : 1.0
#  Ground : 0.0
#  Summary : During a demonstration flight, a U.S. Army flyer flown 
#  by Orville Wright nose-dived into the ground from a height of approximately 75 feet, killing Lt. Thomas E. Selfridge who was a passenger. This was the first recorded airplane fatality in history.  One of two propellers separated in flight, tearing loose the wires bracing the rudder and causing the loss of control of the aircraft.  Orville Wright suffered broken ribs, pelvis and a leg.  Selfridge suffered a crushed skull and died a short time later..

if __name__ == "__main__":
    main()