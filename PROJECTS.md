# Milestone projects and scoring

Each project has a daily assignment with full requirements. Starter code is not a finished project solution.

| Project | Day | Output | Key evidence |
| --- | --- | --- | --- |
| 1: Sales report | 7 | store/channel/product reports and cleaning audit | booked revenue equals manifest and excludes cancelled orders |
| 2: Customer mart | 14 | order and line facts, dimensions, RFM, cohorts | no join inflation; correct order-level frequency |
| 3: Reliable batch pipeline | 20 | bronze/silver/gold pipeline, tests, runbook | retries do not duplicate data; returns reconcile |
| 4: Live monitor | 29 | validated stream, windows, alerts, progress metrics | duplicates, lateness, and recovery demonstrated |
| 5: Integrated platform | 30 | all prior outputs, architecture, ML comparison, operational handoff | reproducible walkthrough and explained differences between stream and batch |

## Rubric for every project

- Correctness and reconciliation: 40 points. Defined grains, accurate amounts, correct null/status/return rules.
- Edge cases and meaningful checks: 20 points. Demonstrated duplicates, invalid rows, empty inputs, and project-specific failure cases.
- Reproducibility: 20 points. Clear commands, pinned dependencies, configuration, stable inputs and rerun behavior.
- Explanation and operating notes: 20 points. Saved evidence, assumptions, failure recovery and limitations.

Pass at 80/100, with correctness at least 30/40. A broken revenue reconciliation or unhandled duplicate replay must be fixed before advancing, even if the total score is high.

## Final submission structure

```text
submissions/capstone/
  README.md
  architecture.md
  contracts.md
  runbook.md
  reconciliation.md
  src/
  tests/
  evidence/
```

Include batch and streaming execution commands, representative output samples, plans, query progress, and ML baseline results. Use synthetic data only. Architecture may use Mermaid. Distinguish locally simulated snapshot publication from a transactional distributed sink. Discuss cluster deployment with spark-submit, driver/executor sizing, logs, and secrets supplied via runtime configuration. Do not put credentials into source files.

Kafka and lakehouse integrations are optional extensions, not prerequisites to earn core completion. For a stronger portfolio, implement one extension and document its additional dependencies and failure semantics.
