
# from faker import Faker
# from models.question import Question
# from sqlmodel import Session
# from database import engine
# from time import sleep
# ###############

# # Create object 
# fake = Faker()

# # Genarate a fake data 
# def gen_question():
#     answer = fake.city()
#     options = ''
#     for i in range(3):
#         opt = fake.city()
#         options += f'{opt},'
#     options += answer
#     return {
#         "question":fake.text(),
#         "answer":answer,
#         "options":options
#     }


# for i in range(10):
#     # Add to database
#     with Session(engine) as session:
#         question = gen_question()
#         q = Question(**question)
#         session.add(q)
#         session.commit()
#         session.refresh(q)
#         print(q)
#         sleep(1)



