#!/usr/bin/env python3

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

NUM_PARTS = 500
NUM_TRANSACTIONS = 8000

categories = ["Fasteners","Bearings","Electronics","Motors","Hydraulics"]
suppliers = ["BoltCo","MotionSupply","ElectroParts","HydroWorks"]

# ---------- Inventory Master ----------

parts = []

for i in range(NUM_PARTS):
	
	part_number = f"P{i:04d}"
	
	category = random.choice(categories)
	supplier = random.choice(suppliers)
	
	lead_time = np.random.randint(5,30)
	unit_cost = round(np.random.uniform(1,150),2)
	
	reorder_point = np.random.randint(20,200)
	safety_stock = np.random.randint(10,50)
	
	parts.append([
		part_number,
		category,
		supplier,
		unit_cost,
		lead_time,
		reorder_point,
		safety_stock
	])
	
inventory_master = pd.DataFrame(parts, columns=[
	"part_number",
	"category",
	"supplier",
	"unit_cost",
	"lead_time_days",
	"reorder_point",
	"safety_stock"
])

# ---------- Transactions ----------

transactions = []

start_date = datetime(2024,1,1)

for i in range(NUM_TRANSACTIONS):
	
	date = start_date + timedelta(days=np.random.randint(0,365))
	
	part = random.choice(inventory_master.part_number.tolist())
	
	transaction_type = np.random.choice(
		["issue","receipt"],
		p=[0.75,0.25]
	)
	
	if transaction_type == "issue":
		qty = np.random.randint(1,8)
	else:
		qty = np.random.randint(80,250)
	
	transactions.append([
		i,
		date,
		part,
		transaction_type,
		qty
	])
	
transactions = pd.DataFrame(transactions, columns=[
	"transaction_id",
	"date",
	"part_number",
	"transaction_type",
	"qty"
])

transactions = transactions.sort_values("date")
transactions["transaction_id"] = range(1, len(transactions)+1)

# ---------- Save ----------

inventory_master.to_csv("data/inventory_master.csv",index=False)
transactions.to_csv("data/transactions.csv",index=False)

print("Data generated.")