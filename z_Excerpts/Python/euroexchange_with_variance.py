try:
    query = int(input("Enter the amount you want to query : £"))
    if query < 6:
        for i in range(1, query+6):
            print(f"£{i} = €{round(i*1.17,2)}")
    else:
        for i in range(query-5, query+6):
            print(f"£{i} = €{round(i*1.14,2)}")
except:
    print("Enter a whole number")
