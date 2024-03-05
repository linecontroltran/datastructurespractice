# Create a hash table (dictionary) of sports cars from the 1990s
cars_1990s_sports_hash_table = {
    "Ferrari F355": "1994",
    "Porsche 911 (964)": "1990-1994",
    "Dodge Viper RT/10": "1992",
    "Acura NSX": "1990",
    "Toyota Supra MKIV": "1993-1998",
    "Mazda RX-7 FD": "1992-2002",
    "Chevrolet Corvette C4 ZR-1": "1990-1995",
    "Nissan 300ZX Z32": "1990-1996",
    "BMW M3 E36": "1992-1999",
    "Lotus Esprit V8": "1996-2004"
}

# Display the hash table contents
print("Cars from the 1990s sports hash table:")
for car, year_range in cars_1990s_sports_hash_table.items():
    print(f"{car} - Production Years: {year_range}")
