# Day 28: MLlib on retail data

Suggested date: 2026-11-02. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

features; Pipeline; VectorAssembler; temporal splits; regression; classification; ALS; evaluation.

## Before you begin

Complete Day 27; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Aggregate daily store/category units including zero-demand days.
2. Build lagged features available before prediction time.
3. Use early dates for training and later dates for evaluation.
4. Fit a simple LinearRegression pipeline and compare MAE with yesterday-demand baseline.
5. Sketch purchase classification and ALS recommendations, including leakage and cold-start risks.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
# Fit preprocessing only on training rows.
```

## More examples to solve

1. Random splitting leaks future behavior. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Customer-level label includes the target purchase. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Unseen product in recommendation serving. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a supervised learning label?
2. What is a feature?
3. What does VectorAssembler produce?
4. What is a Spark ML Pipeline?
5. What is a training set?
6. Why use a temporal split for daily retail demand?
7. What is target leakage?
8. What does MAE measure?
9. Why compare a model with a simple baseline?
10. Why are synthetic-data model results not proof of business value?

### Hands-on questions (11-20)

11. Aggregate daily units by store and category.
12. Fill missing calendar days with zero units where ingestion is complete.
13. Create yesterday's units as a lagged feature.
14. Split earlier dates for training and later dates for evaluation.
15. Build a yesterday-demand baseline.
16. Assemble numeric features into a vector.
17. Fit a LinearRegression model using training rows only.
18. Generate predictions for the evaluation dates.
19. Calculate baseline and model MAE on the same rows.
20. Save split dates, features, and model parameters in an experiment note.

### Advanced challenges (21-30)

21. Explain why random row splitting can leak future seasonality into evaluation.
22. Avoid including target-day sales totals in demand predictors.
23. Fit preprocessing on training data and explain why global fitting leaks information.
24. Design walk-forward evaluation across multiple time cutoffs.
25. Compare per-store MAE with global MAE to identify uneven performance.
26. Explain why MAPE is problematic when observed demand is zero.
27. Sketch a purchase-classification label with a prediction-time cutoff.
28. Sketch ALS user-item inputs and distinguish implicit feedback from explicit ratings.
29. Design cold-start behavior for unseen customers and products.
30. Deliver an experiment report including leakage checks, baseline results, and synthetic-data limitations.


## Completion checks

Report chronological split dates, baseline and model MAE, and no target-day information in predictors; tiny synthetic data is only a learning fixture.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-28/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-28/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day28/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-28/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
