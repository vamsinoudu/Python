individual_cost = 68
under_sixteen = 32.25
family_cost = 42.75
individual = int(input("Enter total number of individuals:"))
under_s = int(input("Enter total number of under 16s :"))
family_cost2 = int(input("Enter total number of families:"))
print("Category Price Breakdown.")
sum_1 = individual_cost * individual
six = under_sixteen * under_s
family = family_cost*family_cost2
family_mem = family_cost2*4
print("Price is £", sum_1, "for", individual, "individuals")
print("price is £", six, "for", under_s, "under 16s.")
print("price is £", family, "for",  family_cost2,   "family.")
print("total persons are :",    individual+under_s+family_mem)
print("Total Event Price is £", sum_1 + six + family)
print("More info and booking visit our website.")



