from .models import Post
from django.contrib.auth.models import User

Post(title="Head Chef",
     description="""We are searching for a Head Chef that is certified and experienced. As the first person in charge, you will prepare and check food before they are served to clients to ensure excellent quality and satisfaction.""",
      responsibility = """1- the management and supervision of the food preparation process and any related operations.
      2- developing meals using innovative or classic dishes assuring the availability and caliber of the meals.""",
      qualifications = """1- A track record as a head chef
      2- Excellent kitchen management skills.
      3- Outstanding leading and verbal abilities.
      4- knowledge of relevant computer software (MS Office, restaurant management software, POS) """,
      posted_by= User.objects.get(username="Restaurant")).save()

Post(title="Remote Graphic designer",
     description="""We are searching for a Remote Graphic designer that is innovative and experienced. As a designer, you will create and improve clients' logos and brand identity.""",
      responsibility = """1- Desgining various types of Logos depending on clients need.
      2- Help in the branding of client's company from a marketing and design prespicitve.""",
      qualifications = """1- Great creative mind.
      2- Knolowdge on relevant software (Adobe Illustrator, Photoshop).
      3- Outstanding teamwork and communication skills.""",
      posted_by= User.objects.get(username="DesignCo")).save()

Post(title="Creative Director",
     description="""We are searching for a Creative Director""",
      responsibility = """1- Approving designs from the team.
      2- Hiring employees.
      3- Interviewing potential employees.
      4- Pitching new ideas.
      5- Maintaining good relations with investors.
      6- Responsible for storing and analysing company and employee records.
      7- Leading the marketing department.""",
      qualifications = """1- Great creative mind.
      2- 20 years of experiences.
      3- Outstanding leading and verbal ability """,
      posted_by= User.objects.get(username="aCompany")).save()

Post(title="Programmer intern",
     description="""We are searching for an intern""",
      posted_by= User.objects.get(username="aCompany")).save()

Post(title="Staff at food truck",
     description="""I am searching for a student with zero experience.""",
      qualifications = """Student with no experience and knowlodge """,
      posted_by= User.objects.get(username="Nasser")).save()

Post(title="Proggrammer Needed",
     description="""I am searching for a programmer to help me with one of my projects""",
      posted_by= User.objects.get(username="Hassan")).save()

Post(title="Graphics Designer Needed",
     description="""I am searching for a designer to help me with one of my projects""",
      posted_by= User.objects.get(username="Hassan")).save()

Post(title="Marketing expert Needed",
     description="""I am searching for a Marketing expert to help me with one of my projects""",
      posted_by= User.objects.get(username="Hassan")).save()
