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

Data Science Lifecycle Option Sprint 3

Executive Summary
In this sprint, I put my focus on optimizing as well as evaluating several 
predictive models to effectively predict patient no-shows for medical 
appointments. By utilizing a comprehensive dataset of over 100,000 
entries, I was able to refine Random Forest, Logistic Regression, and 
Gradient Boosting models. All in all, the evaluation conveyed that Random 
Forest is the most optimal model for this set of data as it had the 
highest overall accuracy while offering significant potential for 
improving appointment management efficiency, reducing operational costs, 
and enhancing patient satisfaction for healthcare providers.


Problem Statement and Business Context
There is a problem where healthcare providers such as dental and doctor's 
offices often experience appointment no-shows which lead to revenue 
losses, scheduling inefficiencies, and reduced availability for other 
patients. Usually, these offices rely a lot on human operators for booking 
appointments which leads to increased operational costs and limited 
availability outside normal business hours. As a result, addressing 
no-shows through predictive modeling can significantly improve efficiency, 
reduce costs, and ensure better resource allocation.

Methodology

(Data Preparation)
To begin with, I used the "Medical Appointment No Shows" dataset from 
Kaggle which included patient demographic details, appointment scheduling 
times, and no-show outcomes. After this, the dataset was cleaned and 
preprocessed, with date fields converted to epoch timestamps, categorical 
variables encoded numerically, and irrelevant identifiers removed to 
improve model accuracy.

(Feature Engineering)
To improve the predictive power of my models, I created several new 
features from the original data:
Lead time (in days): The number of days between when a patient schedules 
their appointment as well as the actual appointment date.
This helps capture whether longer waiting periods increase no-shows or 
not.

Appointment day and hour: The specific day of the week and the hour of the 
day when appointments are being scheduled.
This identifies patterns where certain days or even times might influence 
attendance.

Patient age groups: Categorizing patients into groups like young (0–18 
years), adult (19–65 years), and senior (66+ years).
Different age groups typically have varying attendance behaviors.

Weekend indicator (binary encoding): A simple binary feature indicating 
whether an appointment is scheduled on a weekend (Saturday or Sunday) or a 
weekday.
Weekends may have different attendance rates compared to weekdays.

(Modeling Approaches)
I evaluated three machine learning models to determine which one best 
predicts appointment no-shows better:
1. Random Forest
Random forests build multiple decision trees and combine their predictions 
to enhance accuracy.
I optimized the following hyperparameters using GridSearchCV (a systematic 
way of testing different combinations):
Number of estimators: Number of trees in the forest ([100, 200]).
Maximum depth: The maximum number of splits each tree can make ([None 
(unlimited), 10, 20]).
Minimum samples split: The minimum number of data points required before a 
tree splits further ([2, 5]).

2. Logistic Regression
Logistic regression predicts probabilities for binary outcomes, which is 
ideal for yes/no predictions such as no-shows.

The hyperparameters I tuned included:
Regularization strength (C values): Controls overfitting by penalizing 
overly complex models ([0.01, 0.1, 1, 10]).

Class weighting: Whether to treat classes equally or give more weight to 
underrepresented outcomes ("balanced" vs. "unbalanced").

Penalty types: Method of regularization to simplify the model ("l1" which 
reduces less important features, and "l2" which penalizes large 
coefficients).

3. Gradient Boosting
Gradient boosting combines multiple weak decision trees sequentially, each 
correcting the errors of the previous tree, resulting in improved 
predictive accuracy.

Hyperparameters I optimized:
Learning rates: Controls how quickly the model adapts ([0.01, 0.1]).
Maximum depths: Limits how complex each individual tree is ([3, 5, 7]).
Number of estimators: Number of boosting stages or trees ([100, 200]).
Model Evaluation and Selection

After optimization, I evaluated each model using accuracy, precision, 
recall, and F1-score:

Random Forest Results (Best performing model):
Best Parameters: {'max_depth': None, 'min_samples_split': 2, 
'n_estimators': 100}
Accuracy: 80% (Overall correct prediction rate)

No-shows:
Precision: 51% (51% of predicted no-shows were actually correct)
Recall: 19% (19% of actual no-shows were correctly identified)
F1-score: 27% (Balanced metric combining precision and recall)

Shows:
Precision: 82%, 
Recall: 95%, 
F1-score: 88%

Logistic Regression Results:
Best Parameters: {'C': 0.01, 'class_weight': 'balanced', 'penalty': 'l1'}
Accuracy: 67%

No-shows: Precision: 31%, 
Recall: 55%, 
F1-score: 40%

Shows: Precision: 86%, 
Recall: 69%, 
F1-score: 77%

Gradient Boosting Results:
Best Parameters: {'learning_rate': 0.1, 'max_depth': 7, 'n_estimators': 
200}
Accuracy: 80%

No-shows: Precision: 57%, 
Recall: 8%, 
F1-score: 15%

Shows: Precision: 81%, 
Recall: 98%, 
F1-score: 89%

Selected Model:
The Random Forest demonstrated the most balanced performance, as it 
offered strong overall accuracy as well as reliable predictive capability, 
making it the most practical choice for deployment.

Implementation Strategy and Business Value
As the Random Forest model was the best, it can be integrated into 
existing appointment management systems through API connections. By 
accurately predicting appointment no-shows, healthcare providers can now 
proactively adjust schedules, reduce idle time, and even optimize patient 
flow. This implementation is promising because it offers significant cost 
savings by minimizing unused appointment slots as well as improving staff 
productivity. On top of that, patient satisfaction can be greatly enhanced 
by offering timely and more flexible scheduling options.

Ethical Considerations and Limitations

(Ethical Implications)
Deploying predictive models in healthcare requires a lot of transparency 
with regards to how predictions affect patient interactions as well as 
appointment availability. Patients should be informed if predictive 
algorithms influence scheduling flexibility or priority. Also, they should 
know if their personal data is being used with AI or not, which they 
should be able to choose to opt into or avoid depending on their personal 
preferences.

(Potential Biases)
The models may inherently reflect biases present in the dataset, 
particularly in demographic segments such as age groups, neighborhoods, or 
gender. For example, if certain neighborhoods systematically have higher 
no-show rates, the model may unintentionally reinforce scheduling biases 
against these communities. Regular audits and updates are necessary to 
mitigate these biases. For example, if there are higher no-shows with 
indians like me, the model may unintentionally have extra scheduling bias 
for no-shows being indians.

(Limitations and Edge Cases)
The dataset lacked detailed reasons for patient no-shows as it did not 
include certain events, such as emergencies or transportation issues, 
which limits the precision of model predictions. Additionally, text-based 
communication data (like SMS or voice interactions) was not available in 
the dataset, limiting the model's ability to predict based on real-time 
interactions or reminders.

Conclusion
Through meticulous tuning as well as evaluation of several predictive 
modeling techniques, the Random Forest classifier emerged as the most 
effective tool for addressing the significant challenge of appointment 
no-shows in healthcare settings. As a result, from this conclusion, 
implementing this predictive system can substantially improve operational 
efficiency, reduce costs, and enhance patient satisfaction by enabling 
more informed, proactive scheduling decisions as there is now more data 
available to make those types of decisions.


