from creational.builder.grooming_appointment import GroomingAppointment

class BuilderPattern(object):
    """description of class"""

    def __init__(self):
        self.appointment_one = GroomingAppointment("11/01/2015", "435-123-4567", "Shawn", "123 Awesome Street", "", "", 10, "big", True)
        self.appointment_two = GroomingAppointment("01/20/2016", "808-572-2472", "Nora", "", "Derps", "Dragon", 800, "lol it's huge", False, True)

    def demonstrate(self):
        print(self.appointment_one.print_appointment_details())
        print(self.appointment_two.print_appointment_details())
