from canvas import Canvas
from secrets import url, api_key

if __name__ == '__main__':
    #obj = Canvas("https://csus.instructure.com/api/v1/", "11299~LMYUCn8olYHTl1soCXfp9yAA4ybJ46aY2OgZ2IGsFrN4yBQ23j6ZC6BMAAOTYcr0")
    obj = Canvas(url, api_key)
    #print(obj.getClassData())
    print(obj.getClassNames())
    print(obj.getAllAssignments())
    #print(obj.getAllAssignments()[1][0].keys())

    #print(obj.getUpcomingAssignments().keys())

