class Applicants:
    def __init__(self, first_name, last_name, gender, drive):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.drive = drive

    def getName(self, first_name, last_name):
        return first_name + " " + last_name

    def getGender(self, gender):
        return gender

    def getDrive(self, drive):
        return drive
    
    def __repr__(self):
        return "{} {} is a {} who drives a {}".format(self.first_name, self.last_name, self.gender, self.drive)
