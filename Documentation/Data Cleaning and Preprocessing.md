# Data Cleaning and Preprocessing

## Dataset Merge

The travel and survey datasets were merged using the common key:

ID

## Missing Value Treatment

### Removed Columns

Platform_location was removed because:

* More than 80% of values were missing
* Remaining values showed no variation
* The variable provided no analytical value

### Categorical Variables

Missing values in:

* Gender
* CustomerType
* TypeTravel

were replaced with:

Unknown

### Service Rating Variables

Ordinal rating variables were encoded using the following scale:

* Extremely Poor = 1
* Poor = 2
* Need Improvement = 3
* Acceptable = 4
* Good = 5
* Excellent = 6

Missing values were replaced using the median rating.

### Numerical Variables

Missing values in:

* Age
* ArrivalDelay_in_Mins
* DepartureDelay_in_Mins

were replaced using median values.

* Data cleaning and preprocessing were performed in Power Query before dashboard development.
## Feature Engineering

The following derived variables were created for dashboard analysis:

* Delay Bucket
* Satisfaction Status
* Age Group

These variables were used to support segmentation and visualization.

## Result

The final cleaned dataset contained 94,379 passenger records and was prepared for exploratory and statistical analysis.
