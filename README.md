# README.md

# XBorder Due Diligence Directory (X3D) V1.0.

## Purpose & Scope
This capstone project is a simple, menu-driven Python console app designed to manage Customer Due Diligence (CDD) records for cross-border payment services. It leverages Python fundamentals — lists, dictionaries, functions, loops, and basic input handling — to simulate a real-world fintech scenario, particularly on maintaining customer records and risk classifications for risk and compliance operations.

The application enables users to:
- Create, Read, Update, and Delete customer records (CRUD)
- Manually input due diligence results or records (no automation)
- Navigate through the main and sub-menus

Note: ***Transaction monitoring*** is outside the project’s scope. This means there is no handling of transaction amounts, sender/beneficiary details, originating countries, screening results, or other granular transaction-level data.

---

## Features
- CRUD operations for business customer records
- Table view and detailed single record view
- Simple input validation for formatting (uppercase ISO-2 country, title case risk ratings)
- 12 dummy records preloaded for demonstration

---

## Data Model (Using Dummy Data)
```python
{
  "business_id": "XBP10001",  # unique
  "cust_name": "Marinex Global LLC",
  "cust_trading_name": "Marinex",
  "cust_type": "Licensed",       # or Non-licensed
  "industry": "Logistics",
  "country": "US",               # ISO-2
  "country_risk": "Low",         # Low | Medium | High
  "overall_risk": "Medium"         # Low | Medium | High
}
```

---

##  Getting Started

### Run (standard)
```bash
Capstone_X3D_App_V1.py
```

Main Menu You’ll see:
```
========== XBorder Due Diligence Directory (X3D) V1.0 ==========
Main Menu
1. Read Menu
2. Create Menu
3. Update Menu
4. Delete Menu
5. Exit
```

### Run by Sections in VS Code (Shift+Enter)
1. Run `%1` → `%3` to load UI, data, helpers
2. Run `%4` to load CRUD functions
3. Run `%5` to start Main Loop

---

## Menu Flow
**Main Menu**
1. **Read Menu** — Show all / Show by Business ID / Back
2. **Create** — Add a new record
3. **Update** — Modify existing record by Business ID
4. **Delete** — Remove record by Business ID
5. **Exit**

---

## Demo Prompts
**Show All Customers**
```
Choose (1-5): 1
Choose (1-3): 1
```
**Show by ID**
```
Choose (1-3): 2
Enter Business ID to view: XBP10001
```
**Create**
```
Choose (1-5): 2
Business ID (unique): XBC20010
Legal Name: Nordic Gears AB
Trading Name: NordGears
Customer Type: Non-licensed
Industry: MANUFACTURING
Country (ISO-2): SE
Country Risk: Low
Overall Risk: Medium
```
**Update**
```
Choose (1-5): 3
Enter Business ID to update: XBC20003
Trading Name []: KopiNusa+
Industry []: F&B
Overall Risk []: High
```
**Delete**
```
Choose (1-5): 4
Enter Business ID to delete: XBC20004
Confirm delete? (y/n): y
```
**Exit**
```
Choose (1-5): 5
```
---

## Closing Notes
X3D is a fantasy application developed as part of a Python fundamentals capstone project for Module 1 of the Purwadhika JC Data Science Program. It is designed to simulate a realistic yet simplified business tool. The chosen use case — a riak and compliance operations directory for cross-border payment services — draws directly from my professional experience in fintech and compliance operations, making it both relevant and familiar to implement.

While intentionally limited in scope, the project showcases core programming concepts such as CRUD operations, menu-driven navigation, and basic input validation.

The project can serve as:
- A starting point for building more advanced, real-world business applications.
- A teaching example on Python fundamentals.
- A base for experimenting with additional features such as data persistence, reporting, or integration with external risk scoring systems.


