from faker import Faker
import pandas as pd

class DummyDataCreator:

    def get_dummy_profile_data(self):

        fake = Faker()
        data = [fake.profile() for i in range(100)]
        data = pd.DataFrame(data)
        data.to_csv('dummy.csv')


if __name__ == "__main__":

    obj_dummy_data_creator = DummyDataCreator()
    obj_dummy_data_creator.get_dummy_profile_data()