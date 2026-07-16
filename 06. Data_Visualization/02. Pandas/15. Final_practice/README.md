# Dirty Pandas Practice Pack

This pack was built for **end-to-end pandas practice** from Series to datetime, including **groupby, merge/join/concat, MultiIndex, vectorized strings, and pivot tables**.

## Files
- `orders_dirty_full.csv` → main transactional dataset (~100,000 rows)
- `orders_dirty_part_a.csv` → first half of orders for concat practice
- `orders_dirty_part_b.csv` → second half of orders for concat practice
- `customers_dirty.csv` → messy customer master
- `products_dirty.csv` → messy product master
- `warehouses_dirty.csv` → messy warehouse master
- `returns_dirty.csv` → messy returns/refunds log
- `monthly_targets_dirty.csv` → messy monthly sales targets by region and category
- `practice_questions_100.md` → 100 practice questions

## What kind of dirt was intentionally added?
- Leading/trailing spaces in both column names and values
- Mixed uppercase/lowercase/title case
- Duplicate-like columns
- Multiple null markers: empty string, spaces, `N/A`, `null`, `NULL`, `None`, `?`, `missing`, etc.
- Numeric columns stored partly as strings, with commas, currency symbols, text tokens, and some negatives/outliers
- Percentage columns stored as both decimals and percent strings
- Date columns stored in many formats, with some invalid dates
- Boolean columns stored as Yes/No/Y/N/1/0/True/False variants
- Dirty emails and phone numbers
- Duplicate rows and duplicate order IDs
- Inconsistent categorical labels and abbreviations
- Text columns with messy punctuation and multiple spaces

## Suggested workflow
1. Load the raw files.
2. Clean column names.
3. Standardize missing values.
4. Clean text columns.
5. Convert datatypes.
6. Validate relationships and duplicates.
7. Merge all supporting tables.
8. Solve the 100 questions.
9. After you finish, send me your cleaned outputs or code and I can review your solutions or give you the answer key.

## Tip
Do **not** try to clean everything in one line. Build reusable cleaning functions.