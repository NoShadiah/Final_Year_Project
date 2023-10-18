# Import flask and datetime module for showing date and time
from flask import Flask
from models import create_app, db
from models.admins.model import Admin
from models.user_roles.model import UserRole
from models.FieldCategories.model import Sub_Field
from models.users.model import User
from models.company_profile.model import CompanyProfile
from models.internships.model import InternShip
from models.interview_QN_categories.model import InterviewQuestionCategory
from models.interview_questions.model import InterviewQuestion
from models.students_profile.model import StudentProfile
from models.student_internship_matches.model import SavedInternship
from models.tips.model import Tip
from models.applications.model import Application
from models.reviews.model import Review
from models.testimonials.model import Testimonial
from models.FAQs.model import FAQ
from models.messages.model import Message
# import datetime
from flask_migrate import Migrate
from flask_cors import CORS
# from flask_jwt_extended import JWTManager
  
# x = datetime.datetime.now()
  
app = create_app('development')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
   return dict(db=db, 
               Admin = Admin,
               UserRole = UserRole,
               Sub_Field=Sub_Field,
               User = User,
               CompanyProfile = CompanyProfile,
               InternShip = InternShip,
               InterviewQuestionCategory = InterviewQuestionCategory, 
               InterviewQuestion =InterviewQuestion,
               StudentProfile = StudentProfile,
               SavedInternship = SavedInternship,
               Tip = Tip,
               Application=Application,
               Review=Review,
               Testimonial=Testimonial,
               FAQ = FAQ,
               Message = Message
               )