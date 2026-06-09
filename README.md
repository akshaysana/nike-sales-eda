# Nike India Sales Analysis

## The Problem
Raw sales data is useless.
Inconsistent city names, missing prices, broken dates,
duplicate orders — the data was a mess before it 
could tell any story.

This project fixes that. Then asks the real questions.

## What I Built
A two-stage Python/Pandas pipeline that takes dirty 
Nike India sales data, cleans it with justified 
decisions, engineers financial metrics, and produces 
an executive-level pivot table — ready for any 
analyst or dashboard to consume.

No manual fixes. No Excel. Just code.

## What the Data Actually Revealed
- Kolkata, Delhi, and Mumbai are the top 3 profit 
  generating regions — not the metros you'd expect
- Flex Trainer leads revenue across all product lines
- Discount_Applied had silent nulls being treated as 
  100% discount — a data bug that would have corrupted 
  every revenue calculation
- City names had 4 different spellings for the same 
  location — standardized before any analysis ran

## Pipeline
Nike_Sales_Uncleaned.csv
       ↓
cleaner.py → drops duplicates, imputes nulls,
             standardizes regions, fixes discounts
       ↓
Nike_sales_audit.csv
       ↓
analysis.py → engineers revenue, unifies dates,
              builds executive pivot table by 
              Region × Product Line

## Tech Stack
Python, Pandas, NumPy

## How to Run
1. Clone the repo
2. Run cleaner.py → produces Nike_sales_audit.csv
3. Run analysis.py → prints executive pivot table

## Dataset
Synthetic Nike India sales data
2,386 orders across 5 product lines
8 Indian cities, 2 sales channels (Online, Retail)
