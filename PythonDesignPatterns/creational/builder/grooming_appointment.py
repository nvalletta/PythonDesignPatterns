class GroomingAppointment(object):
    """description of class"""

    def __init__(self, 
                 appointment_date, 
                 phone_number, 
                 customer_name,
                 address="",
                 dog_name="",
                 dog_breed="",
                 dog_age="",
                 dog_size="",
                 bath=False,
                 nails=False,
                 ears=False,
                 hair_cut=False):

        self.appointment_date = appointment_date
        self.phone_number = phone_number
        self.customer_name = customer_name

        self.address = address

        self.dog_name = dog_name
        self.dog_breed = dog_breed
        self.dog_age = dog_age
        self.dog_size = dog_size

        self.bath = False
        self.nails = False
        self.ears = False
        self.hair_cut = False


    def print_appointment_details(self):
        message = """
            Date: {}
            Phone Number: {}
            Customer Name: {}
            Address: {}
            Dog Name: {}
            Dog Breed: {}
            Dog Age: {}
            Dog Size: {}
            Bath: {}
            Nails: {}
            Ears: {}
            Hair Cut: {}
            """.format(self.appointment_date, self.phone_number, self.customer_name, self.address, self.dog_name, self.dog_breed, self.dog_age, self.dog_size, self.bath, self.nails, self.ears, self.hair_cut)

        print(message)