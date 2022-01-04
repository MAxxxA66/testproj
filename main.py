bill_no = input("Enter bill no ")
product_name = input("Enter product name ")
unit = int(input("Enter quantity "))
price_per_unit = int(input("Product price "))

print("________________________________________")

print(product_name)
p = unit * price_per_unit

print("Bill Amount : ",p)

if p >5000:
    discount = 0.05
    np = p - (p * discount)
    print("Discount is : 5%")
   
else:
    discount =0.01
    np = p - (p * discount)
    print("Discount is : 1%")
        
print("Net Amount is : ",np)

print("________________________________________")
print("Thank You Come Again")
print("________________________________________")

