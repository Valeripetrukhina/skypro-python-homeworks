def bank(X, Y):
    total_amount = X
    
    for year in range(Y):
        total_amount *= 1.1 

    return total_amount

initial_investment = 1000 
years = 5 
final_amount = bank(initial_investment, years)
print(f"Сумма на счету спустя {years} лет: {final_amount:.2f} рублей")
