from canvas import Canvas

if __name__ == '__main__':
    #obj = Canvas("https://csus.instructure.com/api/v1/", "11299~LMYUCn8olYHTl1soCXfp9yAA4ybJ46aY2OgZ2IGsFrN4yBQ23j6ZC6BMAAOTYcr0")
    obj = Canvas("https://csus.instructure.com/api/v1/", "11299~GFTiZM75LzbqkieoWC5o0Vb2gJRaaYoSAEeH9ctPVQv0E832F8hLYIZhHONoRAtI")
    #print(obj.getClassData())
    print(obj.getClassNames())
    #print(obj.getAllAssignments())
    #print(obj.getAllAssignments()[1][0].keys())

    #print(obj.getUpcomingAssignments().keys())

