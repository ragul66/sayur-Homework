'''1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit use Dictionary.'''


cafe={
    'tea':{
    'name':'tea',
    'price':30,
    'stock':25,
    'refill':25,
    'profit':10,
    'sales':0,
    'totalprofit':0
    },
    'coffee':{
    'name':'coffee',
    'price':25,
    'stock':20,
    'refill':20,
    'profit':8,
    'sales':0,
    'totalprofit':0
    },
    'cookie':{
    'name':'cookies',
    'price':15,
    'stock':35,
    'refill':35,
    'profit':7,
    'sales':0,
    'totalprofit':0
    },
    'cappucino':{
    'name':'cappucino',
    'price':23,
    'stock':19,
    'refill':19,
    'profit':6,
    'sales':0,
    'totalprofit':0
}
}
#custinput='2 coffee 3 tea'
for i in range(3):
    custinput=input("What do you want").lower()

    custinput=custinput.split()
    for i,value in enumerate(custinput):
        if value in cafe:
            #index=i-1
            quantity=custinput[i-1]
            #print(quantity)
            if cafe[value]['stock']<=cafe[value]['refill']*0.2:
                cafe[value]['stock']=cafe[value]['refill']
            cafe[value]['sales']+=int(quantity)
            cafe[value]['stock']-=int(quantity)
            cafe[value]['totalprofit']+=int(quantity)*cafe[value]['profit']


top_sales=dict(sorted(cafe.items(),key=lambda x:x[1]['sales'],reverse=True)[:3])

top_profit=dict(sorted(cafe.items(),key=lambda x:x[1]['totalprofit'],reverse=True)[:3])

for x in top_sales:
    print(f"{x} {cafe[x]['sales']}")

for x in top_profit:
    print(f"{x} {cafe[x]['totalprofit']}")


















        