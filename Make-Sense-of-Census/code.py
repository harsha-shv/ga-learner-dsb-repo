# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Code starts here
data=np.genfromtxt(path,delimiter=',',skip_header=1)
census=np.concatenate((data,new_record))


# --------------
#Code starts here
age=np.array([census[:,0]])
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)


# --------------
#Code starts here
import numpy as np

race=np.array([census[:,2]])
race_0=np.array([race[race==0]])
race_1=np.array([race[race==1]])
race_2=np.array([race[race==2]])
race_3=np.array([race[race==3]])
race_4=np.array([race[race==4]])
len_0=race_0.size
len_1=race_1.size
len_2=race_2.size
len_3=race_3.size
len_4=race_4.size

lem=np.array([[len_0],[len_1],[len_2],[len_3],[len_4]])

inde=min(lem)
index=list(lem).index(inde)
minority_race=index


# --------------
#Code starts here

#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=high.mean(axis=0)[7]
avg_pay_low=low.mean(axis=0)[7]
avg_pay_high>avg_pay_low



