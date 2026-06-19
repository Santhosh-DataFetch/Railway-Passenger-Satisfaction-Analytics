# Railway Passenger Satisfaction Analysis

## Objective

The objective of this project is to identify the factors that influence passenger satisfaction in railway transportation using travel and survey datasets.

## Research Questions

### RQ1

What factors most influence passenger satisfaction?

### RQ2

How do departure and arrival delays affect passenger satisfaction?

### RQ3

Are loyal customers more satisfied than disloyal customers?

### RQ4

Do business travelers and personal travelers value different service attributes?

### RQ5

Can passenger satisfaction be predicted using travel characteristics and service quality metrics?

## Dataset

Traveldata_train.csv

Surveydata_train.csv


## Dataset Summary

The project uses two datasets:

Travel Data
Passenger Survey Data

The datasets were merged using the common key: ID


## Data Quality Assessment

The merged dataset contains 94,379 passenger records.

Most variables contain complete data.

A small number of missing values were identified in survey rating fields. For example:

* Seat_comfort: 61 missing values

The proportion of missing values is extremely small (<0.1%) and is unlikely to significantly affect analysis results.
## Preliminary Findings

Initial analysis compared average service ratings between satisfied and unsatisfied passengers.

The largest differences were observed in:

* Onboard Entertainment
* Online Support
* Online Booking Ease
* Cleanliness
* Baggage Handling

These factors appear to have a stronger relationship with passenger satisfaction.

Platform Location showed almost no difference between satisfied and unsatisfied passengers, suggesting it may have limited influence on overall satisfaction.



## Project Status

Completed:

* Dataset merging and cleaning
* Missing value treatment
* Feature engineering
* Exploratory Data Analysis (EDA)
* Correlation analysis
* Delay analysis
* Customer segmentation analysis
* Power BI dashboard development

Dashboard Pages:

1. Executive Summary
2. Service Quality & Satisfaction Drivers
3. Delay Analysis & Operational Performance
4. Actionable Insights & Recommendations
      
