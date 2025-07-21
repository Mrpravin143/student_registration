from faker import Faker
import random 
from studd.models import *
#generate The Fake data Using This "from faker import Faker"
fake = Faker()
def Seed_DB(n=10)->None:
    try:
        for i in range(0,n):
            student_id=f'PVP-0{random.randint(100,900)}'
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(20,30)
            stud_id_obj=StudentID.objects.create(student_id=student_id)

            Student_Info.objects.create(
                student_id=stud_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                
                )
    except Exception as e:
        print(e)


def demo(n=20)->None:
    try:
        for i in range(0,n):
            fake_id=f'DNY-0{random.randint(100,1000)}'
            username=fake.name()
            email=fake.email()
            address=fake.address()

            data=Fake.objects.create(
                id=fake_id,
                username=username,
                email=email,
                address=address,
                
                
                )
    except Exception as e:
        print(e)
