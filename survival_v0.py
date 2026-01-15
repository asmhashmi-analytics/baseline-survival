print("SCRIPT STARTED")
# ===== ASSUMPTIONS =====

monthly_rent = 6950
monthly_mortgage = 4200
monthly_operating_costs = 1200
monthly_living_costs = 2000

starting_buffer = 50000

rent_drop_pct = 0.15
cost_increase_pct = 0.10

time_horizon_years = 10

# =======================

months = time_horizon_years * 12
buffer = starting_buffer

for month in range(1, months + 1):
    stressed_rent = monthly_rent * (1 - rent_drop_pct)
    stressed_costs = (monthly_operating_costs + monthly_living_costs) * (1 + cost_increase_pct)

    net_cashflow = stressed_rent - monthly_mortgage - stressed_costs
    buffer += net_cashflow

    if buffer < 0:
        print(f"FAILS at month {month}. Buffer: £{round(buffer, 2)}")
        break
else:
    print(f"SURVIVES {time_horizon_years} years. Final buffer: £{round(buffer, 2)}")
