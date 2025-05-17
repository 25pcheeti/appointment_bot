# Data Science Lifecycle Option: Final Report (Sprints 1–3)

## Sprint 1: Problem Statement and Significance

In today’s fast-paced world, many businesses like restaurants, dental 
offices, and doctor offices face big challenges when it comes to managing 
customer interactions effectively. These businesses often rely on human 
operators for appointment booking, customer queries, and scheduling, which 
is time-consuming, expensive, and limited to working hours.

### Why This Problem Matters

* **Cost Efficiency**: AI chatbots and voice callers can reduce 
operational costs by automating repetitive tasks.
* **24/7 Availability**: AI systems ensure round-the-clock access to 
appointment booking and FAQs.
* **Scalability**: AI systems scale easily with customer demand.
* **Data-Driven Insights**: AI can extract trends from interaction data to 
improve operations.

All in all, developing AI chatbots and voice callers can streamline 
operations, reduce cost, and enhance customer experience.

## Review of Similar Solutions

* **Zocdoc**: Allows online appointment booking but still requires manual 
confirmation.
* **OpenTable**: AI-driven table management and scheduling.
* **Ada**: Automates customer support and FAQs.
* **Google Duplex**: AI system that can autonomously make appointments by 
phone.

Most existing tools are either platform-specific or hard to integrate. My 
solution focuses on customizability, affordability, and ease of 
implementation for small to medium businesses.

## Proposed Scope of Work

### Methodology

* **Data Collection**: Gather data from customer interactions.
* **Predictive Models**:

  * Intent Recognition
  * Time-Series Forecasting
  * Recommendation Systems
* **Integration**: API connectivity to existing platforms.
* **Evaluation**: Real-world testing and refinement.

### Preliminary Data & Metrics

* **Sources**: Customer logs, simulated datasets.
* **Metrics**: Accuracy, response time, satisfaction, cost savings.
* **Evaluation**: Usability testing with real businesses.

### Technical Skills

Already have the technical skills to develop and deploy AI chatbots and 
voice agents.

---

## Sprint 2: Data Preparation & Baseline Modeling

### Dataset Used

**Medical Appointment No Shows** 
([Kaggle](https://www.kaggle.com/datasets/joniarroba/noshowappointments)) 
with 100k+ records.

#### Key Variables

| Variable       | Type        | Description                                    
|
| -------------- | ----------- | 
---------------------------------------------- |
| PatientId      | String      | Unique identifier for each patient             
|
| AppointmentID  | String      | Unique identifier for each appointment         
|
| Gender         | Categorical | Patient's gender (F or M)                      
|
| ScheduledDay   | Datetime    | When the appointment was scheduled             
|
| AppointmentDay | Datetime    | Actual appointment date                        
|
| Age            | Integer     | Patient's age                                  
|
| Neighbourhood  | String      | Where the patient lives                        
|
| SMS\_received  | Integer     | If an SMS was sent (1 for yes, 0 for no)       
|
| No-show        | Categorical | If the patient missed the appointment 
(Yes/No) |

### Data Cleaning

* Converted dates to datetime and dropped incomplete rows.
* Removed irrelevant identifiers.
* Checked for missing data.

### Feature Engineering

* Extracted weekday and hour from appointment times.
* Grouped patients into age brackets.
* Created binary column for weekend appointments.

### Models Implemented

* **Logistic Regression** for interpretability.
* **Random Forest** for robustness to non-linearity.

### Evaluation

* Used accuracy, precision, recall, F1 score, and confusion matrix.
* Found random forest to be stronger than logistic regression.

### Dataset Limitations

* No text/voice data.
* No reason for no-shows (e.g., transportation, emergencies).

Still, the dataset provides strong predictive value for scheduling and 
optimization.

---

## Sprint 3: Final Tuning, Evaluation & Deployment Plan

### Executive Summary

This sprint focused on tuning and evaluating multiple models to predict 
patient no-shows. I tested Random Forest, Logistic Regression, and 
Gradient Boosting. The best model, Random Forest, offers a practical 
solution to improve scheduling and reduce missed appointments.

### Data Preparation

* Cleaned the Kaggle dataset.
* Converted datetime to epoch seconds.
* Encoded categorical variables.
* Removed irrelevant identifiers.

### Feature Engineering

* **Lead Time**: Days between scheduling and appointment.
* **Day/Hour**: Appointment weekday and hour.
* **Age Group**: Young (0–18), Adult (19–65), Senior (66+).
* **Weekend**: Binary flag (1 if weekend).

### Modeling Approaches

#### 1. Random Forest

* **Best Params**: `{'max_depth': None, 'min_samples_split': 2, 
'n_estimators': 100}`
* **Accuracy**: 80%
* **No-Shows**: Precision: 51%, Recall: 19%, F1: 27%
* **Shows**: Precision: 82%, Recall: 95%, F1: 88%

#### 2. Logistic Regression

* **Best Params**: `{'C': 0.01, 'class_weight': 'balanced', 'penalty': 
'l1'}`
* **Accuracy**: 67%
* **No-Shows**: Precision: 31%, Recall: 55%, F1: 40%
* **Shows**: Precision: 86%, Recall: 69%, F1: 77%

#### 3. Gradient Boosting

* **Best Params**: `{'learning_rate': 0.1, 'max_depth': 7, 'n_estimators': 
200}`
* **Accuracy**: 80%
* **No-Shows**: Precision: 57%, Recall: 8%, F1: 15%
* **Shows**: Precision: 81%, Recall: 98%, F1: 89%

### Final Selection

Random Forest showed the best overall performance, especially for show 
prediction and general reliability.

### Implementation & Business Value

* Can integrate via API into appointment systems.
* Helps reduce missed appointments and idle staff time.
* Improves patient satisfaction with smarter scheduling.

### Ethical Considerations

* Be transparent with patients about how their data is used.
* Avoid biases by auditing models frequently.
* Prevent discrimination by not penalizing patients from high no-show 
neighborhoods unfairly.

### Limitations

* Lacks data on why no-shows happen.
* Doesn’t include real-time communication data like SMS responses.

### Conclusion

By testing and tuning multiple models, I identified Random Forest as the 
best choice for predicting medical appointment no-shows. This solution 
provides measurable operational improvements and supports patient-first 
healthcare delivery.

