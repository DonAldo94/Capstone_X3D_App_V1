###### Capstone Project 1 - Customer Due Diligence Directory for Crossborder Payment Service.
###### App Name: XBorder Due Diligence Directory (X3D) V.1.0

###### Scope:
# A simple python-based console application to store and manage CDD records for cross‑border payment services.
# Not including transaction monitoring, no amounts, no sender/beneficiary details.

###### It allows users to:
# Create new customer records....Manual Input...But we'll improve in the next iteration
# View all customers or a specific customer by Business ID
# Update a customer's fields
# Delete a customer by Business ID

###### Features
# Data stored in a Python list of dictionaries (collection data type)
# One unique key: business_id ----> Main identifier
# Basic functions for each main feature: create/read/update/delete
# Basic input prompts and validation (e.g., unique Business ID check)
# Main Menu -> Submenus (Read / Create / Update / Delete) -> Exit....Exit....That's it! For now at least :)

###### Program Flow (high level)
# Main Menu
#   1. Read Menu
#       - Show all customers
#       - Show one customer by Business ID
#       - Back to Main Menu
#   2. Create Menu
#       - Create one new customer (manual input)
#       - Back to Main Menu
#   3. Update Menu
#       - Update a customer by Business ID
#       - Back to Main Menu
#   4. Delete Menu
#       - Delete a customer by Business ID
#       - Back to Main Menu
#   5. Exit

# ===========%1==============
# ====== Banner / UI ========
# ===========================

def print_banner():
    print("\n========== XBorder Due Diligence Directory (X3D) V1.0 ==========")


def print_main_menu():
    print("\nMain Menu")
    print("1. Read Menu")
    print("2. Create Menu")
    print("3. Update Menu")
    print("4. Delete Menu")
    print("5. Exit")


def print_read_menu():
    print("\n========= Read Menu =========")
    print("1. Show all customers")
    print("2. Show by Business ID")
    print("3. Back to Main Menu")


def pause():
    input("\nPress Enter to continue...")


# =============%2============
# ======  Dummy Data  =======
# ===========================
customers = [
    {"business_id": "XBP10001", "cust_name": "Wise Global Pte Ltd", "cust_trading_name": "Wise", "cust_type": "Licensed", "industry": "PSP", "country": "SG", "country_risk": "Low", "overall_risk": "High"},
    {"business_id": "XBC20001", "cust_name": "Marinex Global LLC", "cust_trading_name": "Marinex", "cust_type": "Non-licensed", "industry": "LOGISTICS", "country": "US", "country_risk": "Low", "overall_risk": "Medium"},
    {"business_id": "XBP10002", "cust_name": "Satoshi Crypto Services Ltd", "cust_trading_name": "SatoCrypto", "cust_type": "Licensed", "industry": "CRYPTO", "country": "HK", "country_risk": "Medium", "overall_risk": "High"},
    {"business_id": "XBC20002", "cust_name": "Aurora Foods GmbH", "cust_trading_name": "Aurora", "cust_type": "Non-licensed", "industry": "FMCG", "country": "DE", "country_risk": "Low", "overall_risk": "Low"},
    {"business_id": "XBP10003", "cust_name": "Lionpay Technologies Ltd", "cust_trading_name": "Lionpay", "cust_type": "Licensed", "industry": "PSP", "country": "UK", "country_risk": "Low", "overall_risk": "High"},
    {"business_id": "XBC20003", "cust_name": "Kopi Nusantara PT", "cust_trading_name": "KopiNusa", "cust_type": "Non-licensed", "industry": "FOOD & BEVERAGE", "country": "ID", "country_risk": "Medium", "overall_risk": "Medium"},
    {"business_id": "XBC20004", "cust_name": "Bulldog Mining PLC", "cust_trading_name": "Bulldog", "cust_type": "Non-licensed", "industry": "MINING", "country": "ZA", "country_risk": "High", "overall_risk": "High"},
    {"business_id": "XBP10004", "cust_name": "Merlion Remit Pte Ltd", "cust_trading_name": "Merlion Remit", "cust_type": "Licensed", "industry": "PSP", "country": "SG", "country_risk": "Low", "overall_risk": "High"},
    {"business_id": "XBC20005", "cust_name": "Caspian Oil Trading JSC", "cust_trading_name": "Caspian Trading", "cust_type": "Non-licensed", "industry": "ENERGY", "country": "RU", "country_risk": "High", "overall_risk": "High"},
    {"business_id": "XBP10005", "cust_name": "Harbor Digital Payments Pty Ltd", "cust_trading_name": "HarborPay", "cust_type": "Licensed", "industry": "PSP", "country": "AU", "country_risk": "Low", "overall_risk": "High"},
    {"business_id": "XBC20006", "cust_name": "Lotus Textiles Co., Ltd.", "cust_trading_name": "LotusTex", "cust_type": "Non-licensed", "industry": "TEXTILES", "country": "VN", "country_risk": "Medium", "overall_risk": "Medium"},
    {"business_id": "XBC20009", "cust_name": "Alpine Components SARL", "cust_trading_name": "AlpineCo", "cust_type": "Non-licensed", "industry": "MANUFACTURING", "country": "FR", "country_risk": "Low", "overall_risk": "Low"}
]

# ============%3=============
# ===== Helper Functions ====
# ===========================

def find_customer_index_by_id(business_id: str) -> int:
    for i, row in enumerate(customers):
        if row.get("business_id") == business_id:
            return i
    return -1


def show_one_customer(row: dict) -> None:
    print("\n-- Customer Detail --")
    print(f"Business ID   : {row.get('business_id')}")
    print(f"Legal Name    : {row.get('cust_name')}")
    print(f"Trading Name  : {row.get('cust_trading_name')}")
    print(f"Customer Type : {row.get('cust_type')}")
    print(f"Industry      : {row.get('industry')}")
    print(f"Country (ISO) : {row.get('country')}")
    print(f"Country Risk  : {row.get('country_risk')}")
    print(f"Overall Risk  : {row.get('overall_risk')}")


def show_all_customers() -> None:
    """Display all customers with Legal Name + Trading Name."""
    if len(customers) == 0:
        print("No data. The directory is empty.")
        return

    print("-- All Customers --")
    # Simple header for readability
    print(f"{'No':>2} | {'Business ID':<10} | {'Legal Name':<30} | {'Trading':<12} | {'Type':<12} | {'Industry':<15} | {'Country':<7} | {'Overall':<6}")
    print("-" * 120)

    for idx, row in enumerate(customers, start=1):
        print(f"{idx:>2} | {row['business_id']:<10} | {row['cust_name']:<30} | {row['cust_trading_name']:<12} | {row['cust_type']:<12} | {row['industry']:<15} | {row['country']:<7} | {row['overall_risk']:<6}")


# ============%4=============
# ===== CRUD Functions ======
# ===========================

def create_customer() -> None:
    print("\n=== Create New Customer ===")
    new_id = input("Business ID (unique): ").strip()
    if find_customer_index_by_id(new_id) != -1:
        print("[X] Business ID already exists. Creation cancelled.")
        return
    cust_name = input("Legal Name: ").strip()
    trading = input("Trading Name: ").strip()
    cust_type = input("Customer Type (Licensed/Non-licensed): ").strip()
    industry = input("Industry: ").strip()
    country = input("Country (ISO-2): ").strip().upper()
    country_risk = input("Country Risk (Low/Medium/High): ").strip().title()
    overall_risk = input("Overall Risk (Low/Medium/High): ").strip().title()
    new_row = {
        "business_id": new_id,
        "cust_name": cust_name,
        "cust_trading_name": trading,
        "cust_type": cust_type,
        "industry": industry,
        "country": country,
        "country_risk": country_risk,
        "overall_risk": overall_risk,
    }
    customers.append(new_row)
    print("[√] Customer created successfully.")


def read_menu() -> None:
    while True:
        print_read_menu()
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            show_all_customers()
            pause()
        elif choice == "2":
            bid = input("Enter Business ID to view: ").strip()
            idx = find_customer_index_by_id(bid)
            if idx == -1:
                print("[X] Not found.")
            else:
                show_one_customer(customers[idx])
            pause()
        elif choice == "3":
            break
        else:
            print("[X] Invalid choice. Try again.")


def update_customer() -> None:
    print("\n=== Update Customer ===")
    bid = input("Enter Business ID to update: ").strip()
    idx = find_customer_index_by_id(bid)
    if idx == -1:
        print("[X] Not found. Update cancelled.")
        return
    row = customers[idx]
    show_one_customer(row)
    print("\nLeave input blank to keep current value.")
    new_name = input(f"Legal Name [{row['cust_name']}]: ").strip()
    new_trad = input(f"Trading Name [{row['cust_trading_name']}]: ").strip()
    new_type = input(f"Customer Type [{row['cust_type']}]: ").strip()
    new_ind  = input(f"Industry [{row['industry']}]: ").strip()
    new_ctry = input(f"Country (ISO-2) [{row['country']}]: ").strip().upper()
    new_crsk = input(f"Country Risk [{row['country_risk']}]: ").strip().title()
    new_or   = input(f"Overall Risk [{row['overall_risk']}]: ").strip().title()
    if new_name:
        row['cust_name'] = new_name
    if new_trad:
        row['cust_trading_name'] = new_trad
    if new_type:
        row['cust_type'] = new_type
    if new_ind:
        row['industry'] = new_ind
    if new_ctry:
        row['country'] = new_ctry
    if new_crsk:
        row['country_risk'] = new_crsk
    if new_or:
        row['overall_risk'] = new_or
    print("[√] Customer updated successfully.")


def delete_customer() -> None:
    print("\n=== Delete Customer ===")
    bid = input("Enter Business ID to delete: ").strip()
    idx = find_customer_index_by_id(bid)
    if idx == -1:
        print("[X] Not found. Delete cancelled.")
        return
    show_one_customer(customers[idx])
    confirm = input("Confirm delete? (y/n): ").strip().lower()
    if confirm == 'y':
        customers.pop(idx)
        print("[√] Deleted.")
    else:
        print("[i] Cancelled.")


# ============%5=============
# ======== Main Loop ========
# ===========================
print_banner()
user_choice = ''
while user_choice != '5':
    print_main_menu()
    user_choice = input("Choose (1-5): ").strip()
    if user_choice == '1':
        read_menu()
    elif user_choice == '2':
        create_customer()
        pause()
    elif user_choice == '3':
        update_customer()
        pause()
    elif user_choice == '4':
        delete_customer()
        pause()
    elif user_choice == '5':
        print("\nGoodbye! Thanks for using X3D.")
    else:
        print("[X] Invalid choice. Try again.")
