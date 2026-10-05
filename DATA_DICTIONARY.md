# Retail dataset and business rules

All people and transactions are synthetic. Currency is INR; times are UTC. Sales cover 1 July-28 September 2026. IDs are strings. CSV blanks read as null under the normal CSV options. Monetary fields should be read as DecimalType(12,2); discount_pct as DecimalType(5,2); timestamps as TimestampType; quantities as integers. State your output decimal precision explicitly.

| Table | Grain/key | Fields |
| --- | --- | --- |
| customers | one customer / customer_id | customer_id, name, email, city, signup_date (date), updated_at (timestamp) |
| products | one product / product_id | product_id, product_name, category, list_price, cost_price |
| stores | one store / store_id | store_id, store_name, city |
| orders | one order / order_id | order_id, customer_id, store_id, order_ts, status, channel |
| order_items | one order line / line_id, with deliberate raw exceptions | line_id, order_id, product_id, quantity, unit_price, discount_pct |
| returns | one return event / return_id | return_id, line_id, return_quantity, return_ts, reason |

Orders reference customers and stores; lines reference orders and products; returns reference lines. Do not join dimensions until their keys are unique. Repeated order_id in lines is expected and is not a duplicate.

## Canonical cleaning rules

1. Trim IDs; reject null/blank line_id, order_id, or product_id.
2. Reject missing/nonpositive quantity, missing/negative unit_price, and missing/out-of-range discount_pct (valid range 0 through 1 inclusive).
3. Reject unknown order and product references. Use anti joins to identify them.
4. Keep a reason array for invalid rows. Quarantine first; then remove identical line duplicates by line_id. The supplied duplicates are identical; create your own changed duplicate for Day 5.
5. Normalize customer city and email. Blank email is allowed and does not invalidate a sale. Avoid arbitrary replacement of missing monetary fields.

There are 10 invalid line additions and 8 duplicated valid lines. `manifest.json` gives exact raw counts and expected cleaned statistics. Classification before deduplication obeys raw = accepted-before-dedup + quarantine. After deduplication: raw = clean-unique + removed-duplicates + quarantine.

## Metric definitions

- Line gross = quantity × unit_price. Line net = round(line gross × (1 − discount_pct), 2), using half-up rounding.
- **Booked revenue** = sum of clean, deduplicated line net for completed orders only. Cancelled orders contribute zero.
- Order net = sum of its accepted line net. AOV = booked revenue / number of distinct completed orders with accepted lines. If none, AOV is null.
- Cancellation rate = cancelled orders / all orders, at order grain.
- Accepted return units must be positive, reference a completed valid line, and not exceed its sold quantity after aggregating returns by line. Duplicate return_id is removed before aggregation.
- Return deduction = accepted return units × unit_price × (1 − discount_pct). Round line-level deduction to two places. Return-adjusted revenue = booked revenue − deductions; use returned units, not the whole order amount. The fixture has no tax/shipping and no partial-cent prices, so prorating net line amounts also reconciles here.
- RFM recency is days since latest completed purchase at fixed as-of date 2026-10-01. Frequency counts distinct orders; monetary uses booked revenue. Customers without completed orders have null recency and zero frequency/monetary.

## Streaming events

Each archive file is newline-delimited JSON. `examples/schemas.py` defines its full types. Events contain event_id, event_time, customer_id, order_id, event_type (view or purchase), items (array of product_id, quantity, unit_price), device struct, and attributes map. Purchase amounts have no discount in this fixture. Purchase-event revenue is distinct from batch booked revenue: events are a separate simulation and do not encode batch order status, full contents, or return adjustments.

Six batches advance event time from 10:00 to 10:57 on 30 September 2026. Batch 2 repeats E0001. Batch 3 adds LATE_WITHIN at 10:16; batch 5 adds LATE_BEYOND at 10:00. Batch 6 adds BAD_EVENT with an invalid timestamp and empty purchase items. Timestamp parsing under permissive JSON reading can produce null; explicitly quarantine invalid events. Event-time progress depends on when batches are processed, so use controlled publishing for lateness experiments.

Payment events contain payment_id, order_id, payment_time, amount. They arrive two event-time minutes after purchase events, with one payment per generated purchase. Added late/malformed fixtures do not have extra payments. Copy events before mutating nested fields in your own examples.

Validate event_id, parsed timestamp, known event type, and nonempty positive-quantity items for purchases. Event IDs are unique except the intentional repeat. Bounded streaming deduplication can forget old IDs; permanent uniqueness needs additional storage semantics.
