 
lari = 20
კურსი = 3.20 # გვაქვს საშუალება გამოვიყენოთ ქართულად დაწერილი ცვლადები, მაგრამ რეალურ პრაქტიკაში არ არის სასურველი

res = lari / კურსი

# String concatenation (შეერთება) Method 1
print( str(lari) + " ლარი " + str(კურსი) + " კურსით, არის " + str(res) + " დოლარი" )

# String concatenation (შეერთება) Method 2
print( "{} ლარი {} კურსით, არის {} დოლარი".format(lari, კურსი, res) )

# String concatenation (შეერთება) Method 3
print( f"{lari} ლარი {კურსი} კურსით, არის {res} დოლარი" ) 



# Lists

# ინიციალიზაცია
lst_int = [ 1,2,3,4 ]
names = ["გია", "გიგა", "დავით"]

print( names ) # ყველა ელემენტის ნახვა
print( lst_int ) # ყველა ელემენტის ნახვა

print( len(names) ) # List-ის ელემენტების რაოდენობის ნახვა
print( len(lst_int) ) # List-ის ელემენტების რაოდენობის ნახვა

# List -იდან კონკრეტული ელემენტის ამოღება
# List -ის ათვლა იწყება ნულიდან
print( names[0] )


# List-ში ელემენტის ჩამატება
names.append("სხვა სახელი")
lst_int.append("აქ შეიძლება იყოს დამატებითი რიცხვი ან სტრიქონი")

# List-იდან ბოლო ელემენტის წაშლა
names.pop()
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]



# list slicing
# lst1[start:stop:step] syntax

print(lst1[50:]) # 50-ე ინდექსიდან ბოლომდე
print(lst1[:50]) # პირველი 50 ელემენტი
print(lst1[::-1]) # ელემენტების რევერსი
print(lst1[::2]) # გადაახტება ყოველ 2-ე ელემენტს



# Dictionaries
person1 = {
    "name":"John",
    "age":23,
} # ინიციალიზაცია / შექმნა


# გამოყენება
person1.get("name")


# განახლება/დამატება
person1["name"] = "Jane"



# Touple

touple1 = ("John", 23, "Doe")
lst1 = ["John", 23, "Doe"]

lst1[0] = "Jane" # იმუშავებს
# tuple1[0] = "Jane" # არ იმუშავებს



# Set
# ტოვებს მხოლოდ უნიკალურ ელემენტებს
# არ აქვს თანმიმდევრობა

thisset = {1,5,2,2,2,2,2,2,2} # არ არის 
print(thisset)

# Boolean
True
False


# შედარების ოპერატორები
# https://www.w3schools.com/python/gloss_python_comparison_operators.asp


# ლოგიკის დინება
numb = 1

if numb == 1:
    print(f"თქვენ შეიყვანეთ რიცხვი {numb}")
elif numb == 2:
    print(f"თქვენ შეიყვანეთ რიცხვი {numb}")
elif numb == 3:
    print(f"თქვენ შეიყვანეთ რიცხვი {numb}")
else:
    print(f"თქვენ შეიყვანეთ {numb}")
    
    
    
    
# FOR ციკლი
for i in lst1:
    print(i)