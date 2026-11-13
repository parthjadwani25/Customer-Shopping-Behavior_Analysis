import pandas as pd
#1 load the data and print top 5 rows
df=pd.read_csv("customer_shopping_behavior.csv")


#2
print(20*'=',"CUSTOMER_SHOPPING_TABLE_TRANFORMATION",20*'=')
print(20*'=',"TOP 5 DATA",20*'=')
print(df.head())  
print(30*'=',"XXXXX",30*'=')


#3
print(69*'=')
print(30*'=',"information of table",30*'=')
print(df.info())
#this will give full info about table(info like how much rows and column,data type ,non_null_count)
print(20*'=',"XXXXX",20*'=')
#summary startistic using .describe()


#4
print(20*'=',"summary (statistic)",20*'=')
print(df.describe(include='all'))
print(20*'=',"XXXXX",20*'=')


#5
# checking null value
print(20*'-',"Before filling",20*'-')
print(df.isnull().sum())
print(20*'=',"XXXXX",20*'=')


#6
#we can change the null value with(1.mean,2medium,or we can delete that coloumn)
#since review rating has 37 null value will put medium of that coloumn (we can not use mean because it may contain outliers)
# and review rating may change by its category (every category may have diff rating)
# will count medium based on each category
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


#7
# checking null value again
print(20*'=',"After filling",20*'=')
print(df.isnull().sum())
print(20*'=',"XXXXX",20*'=')




#8 
# now as we can see the column name has space between them
# we use snake casing
# snake-casing means  between that space it will put underscoure'_' 
# and also it lower the case of all letters


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
print(20*'=',"column_lower_case+ replace the space betweem them",20*'=')

print(df.columns)
print(20*'=',"XXXXX",20*'=')

print(20*'=',"rename is requird in 1 column",20*'=')

#also now u can see in 1 column there is mistake in name purchase_amount_(usd)
# i want to change the that particular coloumn name remving the usd\
print(20*'=',"XXXXX",20*'=')

df=df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'}) 
print(20*'=',"XXXXX",20*'=')

print(20*'=',"After rename",20*'=')
print(df.columns)



#9
#now i want new column age group 
#want to divde age into 4 groups (young ,adult ,middle age ,senior)


label=['Young_Adult','Adult','Middle_Ageg','Senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=label)
print(df[['age','age_group']].head(10))
#qcut means divide into 4 partsf


print(df.head())





#10
#create new column purchase_fequency_days
#to convert text value in numeric value using map ()

frequency_mapping={
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi_Weekly':14,
    'Annually':365,
    'Every 3 Months':90


}
df['purchase_frequency_days']= df ['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))




#11
#check duplicacy between two tables
print(
df[['discount_applied','promo_code_used']].head(10))
#these two columns are identical

#delete 1
df=df.drop('promo_code_used',axis=1)
print(df.columns)



#data is cleaned now
df.to_csv("customer_shopping_behavior_cleaned.csv", index=False)