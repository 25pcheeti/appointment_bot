Data Science Lifecycle Option Sprint 1

Problem Statement and Significance
In today’s fast-paced world, many businesses like restaurants, dental 
offices, and doctor offices face big challenges when it comes to managing 
customer interactions effectively and efficiently. Many of these 
businesses place heavy reliance on human operators to handle appointment 
bookings, customer queries, and schedules. This process is a pain because 
it is not only time-consuming but also costly, especially for businesses 
that have a high amount of customers. Additionally, human operators are 
limited by their working hours, which can result in missed opportunities 
for businesses that operate outside of standard business hours or have 
customers that may be in different time zones. 

The problem is worth solving because of:
Cost Efficiency: Maintaining a large customer service team costs a lot of 
money, and AI chatbots as well as voice callers can reduce operational 
costs by automating repetitive tasks like appointment scheduling as well 
as FAQ’s.
24/7 Availability: AI systems are able to operate all day making sure that 
customers can book appointments or get information at any time which is 
able to improve customer satisfaction.
Scalability: As businesses become bigger and bigger, their customer 
service demands increase. As a result, AI systems can scale effortlessly 
to handle higher volumes of interactions with minimum or no additional 
cost. 
Data-Driven Insights: AI systems have the ability to collect and analyze 
customer interaction data which can provide businesses with actionable 
insights in order to improve services as well as optimize operations. 
All in all, by developing AI chatbots as well as voice callers, businesses 
can streamline their operations, reduce costs, and enhance customer 
experience which makes this a highly impactful problem to solve.

Review of Similar Solutions
There are some businesses and platforms that have already implemented 
AI-driven solutions for customer service as well as appointment 
scheduling:
Zocdoc: This allows patients to book appointments online but even though 
it automates scheduling the user still has to manually book it.
OpenTable: This uses AI to manage bookings and optimize table 
availability.
Ada: This is a chatbot used by businesses in order to automate customer 
support and FAQ’s.
Google Duplex: This is an AI-system that can book appointments on behalf 
of users. 
While these solutions each have their own purpose, most of them are 
platform specific or require integration with existing system to be used. 
My solution could be different by being more customizable and more 
tailored towards small to medium sized businesses with a higher focus on 
affordability as well as ease of implementation. 


Proposed Scope of Work
Methodology
Data Collection: Gather data from customer interactions such as common 
queries, appointment booking patterns, and customer preferences. 
Predictive Models
Intent Recognition: Figure out whether customers want to book, cancel, or 
ask about FAQ’s.
Time-Series Forecasting: Predict when the peak booking times are occurring 
to optimize resource utilization.
Recommendation Systems: Suggest appropriate appointment slots based on 
customer preferences and when the business is available to meet with them.
Integration: Integrate API’s to link the AI system to existing business 
platforms.
Evaluation: Test the AI-system with real world data and and refine it 
based on the feedback received. 

Preliminary Data Sources, Success Metrics, and Evaluation Criteria
Data Sources
Customer Interaction Logs if businesses have them
Simulated Data on the business using limited real world data
Success Metrics of the AI bot
Accuracy 
Response Time
Customer Satisfaction
Cost Savings
Evaluation Criteria
Real-world testing on potential businesses to measure usability and 
effectiveness

Technical Skills Development Plan
I already have the technical skills to develop AI chatbots and voice 
callers so there doesn’t need to be a technical skills development plan 
for this project.


Data Science Lifecycle Option Sprint 2

This section of the project involves continuing to focus on the AI system 
for automating customer interactions, but specifically the "Medical 
Appointment No Shows" dataset from Kaggle in order to better figure out 
customer interactions for the AI. By using some Python code, I was able to 
address data gathering, cleaning, visualization, feature engineering, 
baseline model implementation, and evaluation. As far as the data set 
goes, it contains over 100,000 data entries with fields such as PatientId, 
AppointmentID, Gender, ScheduledDay, AppointmentDay, Age, Neighbourhood, 
SMS_received, and No-show (indicating whether the patient did not attend, 
with values "No" or "Yes"). This dataset is relevant for 
healthcare-related appointment scheduling, aligning with the project's 
focus on dental and doctor offices for customer service.

Gather datasets
"Medical Appointment No Shows" dataset from Kaggle
https://www.kaggle.com/datasets/joniarroba/noshowappointments 
Data Dictionary


Variable
Type
Description
PatientId
String
Unique identifier for each patient


AppointmentID
String
Unique identifier for each appointment


Gender
Categorical
Patient's gender (F or M)


ScheduledDay
Datetime
Day and time when the appointment was scheduled


AppointmentDay
Datetime
Day and time of the appointment


Age
Integer
Patient's age


Neighbourhood
String
Patient's neighbourhood


SMS_received
Integer
Whether an SMS reminder was sent (1 for yes, 0 for no)


No-show
Categorical
Whether the patient did not show up (Yes or No)


Data cleaning and preprocessing
The images below show the importing steps as well as the data cleaning and 
organization steps as well as the output to check if there are any missing 
values.


Data visualization
The code for all of the data visualizations that were created are shown 
below and this has been done in order to see the different relationships 
between the several variables to find correlations.


Feature engineering and selection
The code is shown below and when I run it, it takes around a minute to 
finish running.
New Features:
Day of the week from AppointmentDay.
Whether it's a weekend (1 for Saturday/Sunday, 0 otherwise).
Time of day (morning, afternoon, evening, night) based on appointment 
hour.
Age group categories (young: 0-18, adult: 19-65, senior: 66+).


Baseline model implementation
I implemented logistic regression and random forest classifier to predict 
no-shows, using cross-validation for robust performance assessment:
Models:
Logistic Regression for interpretability.
Random Forest for handling non-linear relationships.


Model evaluation and comparison
I evaluated both models using accuracy, precision, recall, and F1 score, 
comparing performance to document strengths and weaknesses:
Metrics: Applied confusion matrices, precision, recall, and F1 scores for 
comprehensive evaluation.


All of the Outputs for the Segments of Code
For most of the charts, yes means 1 and no means 0, and for the gender 
chart Female is 0 and Male is 1.


Addressing Project Alignment and Limitations
Given the project’s focus on customer interactions, one limitation of the 
dataset is that it does not include text messages or voice interactions 
which are important for training the chatbot to understand natural 
language inputs for FAQ responses. Fortunately, it is possible to train 
the chatbot without this but it might not be as good at the start of its 
use and will get better over time. Another factor in the data is the 
assumption made in the dataset where the no-show field is treated as an 
outcome of a booking but does not specifically state if there were 
cancellations or if they just did not show up. As a result, a no-show 
could mean the customer forgot, was unable to attend, or did not cancel, 
rather than actively canceling, which introduces potential inaccuracies if 
these are interpreted as cancellations. However, for scheduling 
optimization and no-show prediction, it still provides valuable insights, 
aligning with the project's goals of improving appointment management. All 
in all, the models that were developed from the dataset can be implemented 
into the chatbot in order to predict no-shows as well as optimize 
appointment scheduling resulting in improved operational efficiency as 
well as improved customer satisfaction.

