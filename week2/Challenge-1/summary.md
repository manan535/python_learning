# Titanic EDA — Insight Summary

## Key Insights

### 1. Sex and passenger class interact strongly

Survival differed substantially by both sex and passenger class. Female survival was 96.8% in first class, 92.1% in second class, and 50.0% in third class. Male survival was much lower at 36.9%, 15.7%, and 13.5% respectively.

This shows that sex and passenger class should be considered together when analyzing survival rather than treating either variable in isolation.

### 2. Small-to-medium family groups had higher observed survival

Passengers travelling in groups of 2–4 had higher observed survival rates than solo travellers and very large groups. Survival was 55.3% for family size 2, 57.8% for size 3, and 72.4% for size 4, compared with 30.4% for passengers travelling alone.

Survival dropped substantially for groups of 5 or more. However, the largest family-size categories contain relatively few observations, so these results should be interpreted cautiously.

### 3. Survivors paid substantially higher fares

The average fare for survivors was 48.40 compared with 22.12 for passengers who did not survive.

Fare therefore contains useful information for predicting survival. However, fare is also related to passenger class, so this relationship should not be interpreted as evidence that paying a higher fare directly caused survival.

## Data-Quality and Modeling Risk

### Cabin Missingness

The Cabin column contains substantial missing information. Missing values were replaced with `"Unknown"` so that passenger records were retained. However, the missingness itself may contain information about the passengers or how the records were collected.

A model could therefore learn from the pattern of missing cabin information rather than actual cabin characteristics.

### Related Features

Pclass, Fare, and Cabin contain related information about passenger circumstances. A model may therefore use several correlated variables to capture similar underlying patterns.

These relationships should be considered when interpreting model results. The observed associations in this dataset do not establish causation.

## Overall Recommendation

The strongest signals observed in this EDA are passenger sex, passenger class, and fare. These variables should be considered in further modeling, while interactions between variables should also be examined.

The analysis should be treated as observational: the relationships found in the Titanic dataset identify patterns associated with survival, not causal effects.