phones = ["Phone xs", "Samsung S8 Plus","lg is shit","sony erricson",1,2]

#print(phones)
#print(len(phones))
phones.append('some new brand')
#print(phones)
phones.append("Phone xs")
#print(phones.count('Phone xs'))


#{
#        some code here
#        and litile bit more code
#}
NewPhones={"Iphone Xr", "xiaomi mi10","huawei m2"}
#print(phones[0:2])
#if (phones[1] == "Samsung S8 Plus"):
#    print("yes it is")

def discounted(price,discount,max_discount=20):
    price=abs(float(price))
    discount=abs(float(discount))
    max_discount=abs(float(max_discount))
    if max_discount > 99 :
        raise ValueError("Max discount can't be bigger than 99%")
    if discount >= max_discount :
        return price
    else:
        return price - (price * discount / 100)
                          
print(discounted(100,25,100))

