# =====================================================

# Railway Passenger Satisfaction Analysis

# Author: Santhosh S

# =====================================================

# =====================================================

# IMPORT LIBRARIES

# =====================================================

import pandas as pd

# =====================================================

# EXTRACT

# Load Datasets

# =====================================================

travel_train = pd.read_csv(
r"C:\Users\santh\Downloads\japan_railway_dataset\Traveldata_train.csv"
)

survey_train = pd.read_csv(
r"C:\Users\santh\Downloads\japan_railway_dataset\Surveydata_train.csv"
)

# =====================================================

# TRANSFORM

# Merge Datasets

# =====================================================

merged_ds = pd.merge(
travel_train,
survey_train,
on="ID"
)

print("Dataset Shape:")
print(merged_ds.shape)

# =====================================================

# Target Variable Distribution

# =====================================================

print("\nOverall Experience Distribution")
print(
merged_ds["Overall_Experience"]
.value_counts()
)

# =====================================================

# Convert Service Ratings to Numeric Values

# =====================================================

rating_map = {
"extremely poor": 1,
"poor": 2,
"need improvement": 3,
"acceptable": 4,
"good": 5,
"excellent": 6
}

service_cols = [
"Seat_comfort",
"Arrival_time_convenient",
"Catering",
"Platform_location",
"Onboardwifi_service",
"Onboard_entertainment",
"Online_support",
"Onlinebooking_Ease",
"Onboard_service",
"Leg_room",
"Baggage_handling",
"Checkin_service",
"Cleanliness",
"Online_boarding"
]

for col in service_cols:
merged_ds[col] = merged_ds[col].map(rating_map)

# =====================================================

# EDA 1

# Service Quality Analysis

# =====================================================

comparison = (
merged_ds
.groupby("Overall_Experience")[service_cols]
.mean()
.T
)

comparison["Difference"] = (
comparison[1] - comparison[0]
)

print("\nService Quality Comparison")
print(
comparison.sort_values(
"Difference",
ascending=False
)
)

# =====================================================

# EDA 2

# Delay Analysis

# =====================================================

delay_analysis = (
merged_ds
.groupby("Overall_Experience")
[
[
"DepartureDelay_in_Mins",
"ArrivalDelay_in_Mins"
]
]
.mean()
)

print("\nDelay Analysis")
print(delay_analysis)

# =====================================================

# EDA 3

# Customer Loyalty Analysis

# =====================================================

loyalty_analysis = (
pd.crosstab(
merged_ds["CustomerType"],
merged_ds["Overall_Experience"],
normalize="index"
) * 100
)

print("\nCustomer Loyalty Analysis")
print(loyalty_analysis)

# =====================================================

# EDA 4

# Travel Purpose Analysis

# =====================================================

travel_analysis = (
pd.crosstab(
merged_ds["TypeTravel"],
merged_ds["Overall_Experience"],
normalize="index"
) * 100
)

print("\nTravel Type Analysis")
print(travel_analysis)

# =====================================================

# EDA 5

# Correlation Analysis

# =====================================================

corrs = (
merged_ds[
service_cols +
["Overall_Experience"]
]
.corr(numeric_only=True)
)

print("\nCorrelation with Satisfaction")
print(
corrs["Overall_Experience"]
.sort_values(ascending=False)
)

# =====================================================

# LOAD

# Export Dataset for Power BI

# =====================================================

merged_ds.to_csv(
r"C:\Users\santh\Downloads\railway_satisfaction_cleaned.csv",
index=False
)

print("\nDataset Exported Successfully")
