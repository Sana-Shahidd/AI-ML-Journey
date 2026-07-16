# 50 Pandas Practice Questions

These questions are designed around the concepts you have been practicing in your cleaning notebooks, including DataFrames, missing values, string cleaning, dates, merging, concatenation, joins, MultiIndex, stack/unstack, melt, pivot tables, and core analysis workflows.

## 1) DataFrame Basics and Inspection

1. Load `products_dirty.csv` into a DataFrame and standardize all column names to lowercase with underscores.
2. Display the first 10 rows, last 7 rows, shape, columns, and dtypes of the dataset.
3. Find the number of unique values in each column and identify which columns look categorical.
4. Show a summary of missing values as both counts and percentages for every column.
5. Identify duplicate rows and duplicate column names. How would you remove them?
6. Reorder the columns so that `product_id`, `sku`, `category`, `sub_category`, `product_name` appear first.

## 2) Selection, Filtering, and Indexing

7. Select only `product_name`, `brand`, `list_price`, and `standard_cost` using both single-bracket and double-bracket syntax where appropriate.
8. Filter all rows where `category` is `electronics` and `product_status` is `active`.
9. Find all rows where `supplier_name` is missing but `brand` is present.
10. Use `.loc` to select rows from index 20 to 40 and columns from `brand` to `supplier_name`.
11. Use `.iloc` to select the first 15 rows and the last 4 columns.
12. Create a filtered DataFrame of products where `list_price > 1000` and `standard_cost < 800`.

## 3) Cleaning Text Columns

13. Standardize all object columns by removing extra spaces and converting text to lowercase.
14. Clean `product_id` by stripping spaces, converting to uppercase, and replacing letter `O` with digit `0` where needed.
15. Clean `sku` and fill missing SKU values using the pattern `SKU` + zero-padded row number.
16. Standardize `supplier_name` so variants like `gamma imports`, `GAMMA IMPORTS`, and `Gamma  Imports` become one consistent form.
17. Find rows where `product_name` is blank, `null`, `missing`, `unknown`, or only spaces, and convert them properly to `NaN`.
18. Identify text columns that should be converted to category dtype. Convert them and explain why it can help memory usage.

## 4) Missing Values

19. Write code to replace dirty placeholders like `"unknown"`, `"missing"`, `"null"`, `"none"`, `"n/a"`, and `"?"` across the entire DataFrame.
20. Drop rows where `product_id` or `product_name` is missing.
21. Fill missing `supplier_name` values with the mode of that column.
22. Fill missing `list_price` and `standard_cost` using a business-aware method instead of a plain mean.
23. Which columns would you drop if more than 60% of their values were missing? Write the logic.
24. Compare the result of using `dropna`, `fillna`, forward fill, backward fill, mean, median, and mode on different column types.

## 5) Numeric Cleaning and Validation

25. Clean `list_price` and `standard_cost` by removing `$`, `USD`, commas, invalid words, and converting them to numeric.
26. Find rows where `list_price` is negative, `standard_cost` is negative, or `standard_cost > list_price`.
27. Create a new column `profit` as `list_price - standard_cost` and `margin_pct` as `(profit / list_price) * 100`.
28. Find outliers in `list_price` using IQR and show those rows.
29. Bin `list_price` into groups such as budget, mid-range, premium, and luxury.
30. Rank products within each category by highest `list_price`.

## 6) Date and Time Handling

31. Clean `launch_date` and convert mixed formats into proper datetime values without losing valid dates.
32. Extract year, month, day, month name, quarter, and weekday from `launch_date`.
33. Find all products launched after January 1, 2023.
34. Count how many products were launched in each year and month.
35. Identify rows where the original `launch_date` text could not be parsed into a datetime.

## 7) GroupBy and Aggregation

36. Group by `category` and calculate count, mean, median, min, and max of `list_price`.
37. Group by both `category` and `product_status` and compute average `list_price`, average `standard_cost`, and total products.
38. For each `brand`, find the most expensive product and the least expensive product.
39. Create a grouped result showing total products by `supplier_name` and category.
40. Compare category-level average margin percentage and identify the most profitable category.

## 8) Merge, Join, and Concat

41. Create a second DataFrame called `suppliers` with supplier details and merge it with the products DataFrame on `supplier_name`. Show the difference between inner, left, right, and outer join.
42. Create another DataFrame containing discount information by `category` and join it to the products DataFrame using index-based join.
43. Split the products DataFrame into two parts by category and concatenate them back row-wise. Then concatenate selected columns column-wise and explain the difference.
44. After a merge, identify which rows matched and which did not by using the merge indicator option.

## 9) MultiIndex, Stack, and Unstack

45. Create a MultiIndex summary using `category` and `product_status`, with aggregated statistics for `list_price` and `standard_cost`.
46. Set `category` and `sub_category` as a MultiIndex. Practice selecting one category, one subcategory, and a cross-section.
47. Create a grouped table of counts by `category` and `product_status`, then unstack it into a matrix form.
48. Take the unstacked result and stack it back. What changes in structure do you observe?

## 10) Reshaping, Melt, Pivot, and Pivot Table

49. Create a small wide-format monthly sales DataFrame for each category, then use `melt` to convert it to long format. Explain identifier variables and value variables.
50. Build a pivot table showing average `list_price` by `category` and `product_status`, with margins enabled. Then create another pivot table showing count of products by `supplier_name` and `category`.
pd.pivotable{
table name
index=konse rows bnain gi
columns=kon se columns bnain gae
values= kis col ko summarize krna ha
}
---

# Extra Topics You Should Also Practice

These are the important areas students often miss while learning pandas:

- `sort_values`, `sort_index`, `nlargest`, `nsmallest`
- `value_counts`, `unique`, `nunique`
- `map`, `replace`, `apply`, `applymap`
- `duplicated`, `drop_duplicates`
- `query` and `eval`
- `crosstab`
- `cut` and `qcut`
- `reset_index` and `set_index`
- categorical dtype
- memory usage optimization
- exporting cleaned data using `to_csv` and `to_excel`

---

# Bonus Challenge Set

1. Build a complete cleaning pipeline function for `products_dirty.csv`.
2. Build a separate cleaning pipeline for `monthly_targets_dirty.csv`.
3. Merge both datasets using a shared business key you design yourself.
4. Create a dashboard-ready summary table using groupby and pivot_table.
5. Write 10 interview-style questions from your own cleaned dataset and solve them.

---

Source context from your uploaded notebook/code: fileciteturn2file0

