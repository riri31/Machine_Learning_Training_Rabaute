#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

# open the pikle file
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# open the txt file
with open("../final_project/poi_names.txt", "r") as file:
    poi_name=[]
    t=0
    # get the names of txt file
    for k in file.readlines():
        m=k.split(",")[0].split(" ")
        if len(m)>1:
            l=m[1].upper()
            poi_name.append(l)
            t+=1
                    
    #numbre of entries in the pickle file
    print 'number of entries in the text file:{}'.format(t)
    print 'number of entries in the pickle file:{}'.format(len(enron_data))
    
    j=0
    q=0
    # parsing of the dictionnary
    for i in enron_data:
        # test if dictionary entru is classified as poi
        if enron_data[i]['poi']==True:

            j+=1
            # Parse the name of poi entries
            p= i.split(' ')[0].upper()
            # test if dictionnary entry is in the txt file
            if p in poi_name:
                q+=1      
    print 'number of poi entries in the pickle file matching txt file entries on name:{}'.format(q)

# function to retrive features from given name
# I've created this function because I'm not sure about name and features wording
def find_feature(name,looked_feature):
    print "-------"
    for i in enron_data.keys():
        if name.upper() in i.upper().split(" ")[0]:
            print 'Found, {}'.format(i)
            for feature in enron_data[i]:
                #print feature
                if looked_feature in feature:
                    print '{}:{}'.format(feature,enron_data[i][feature])
    print "-------"


##### Find stock from James prentice
find_feature('prentice','total_stock_value')

##### Find mails from Wesley Colwell 
find_feature('Colwell','from_this_person_to_poi')

##### Find stock exercised by Jeffrey K Skilling
find_feature('skilling','exercised_stock_options')

##### Find long_term_incentive exercised by Jeffrey K Skilling
find_feature('skilling','incentive')

##### Find stock exercised by Jeffrey K Skilling
find_feature('lay','stock')



##### How many How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
#####  What percentage of people in the dataset as a whole is this?

def find_name_feature(looked_feature, value, poi_required = False ):
    count_total=0.
    count=0.
    for i in enron_data.keys():
        
        for feature in enron_data[i]:
            if looked_feature in feature and enron_data[i][feature]==value:
                    #print '{}/{}:{}'.format(i,feature,enron_data[i][feature])
                    if not poi_required:
                        count +=1
                    elif enron_data[i]['poi']== True:
                        count +=1
                        print ok
                        
        count_total+=1
    return int(count), round(100.*(count/count_total),2)


result_nan=find_name_feature(looked_feature='total_payments', value='NaN')
print 'Number/Percentage of E+F people have Nan as total payments: {}({}%)'.format(result_nan[0],result_nan[1])


#### How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this? 
result_poi_nan=find_name_feature(poi_required=True, looked_feature='total_payments', value='NaN')
print 'Number/Percentage of POI E+F people have Nan as total payments: {}({}%)'.format(result[0],result[1])

#### if we add 10 new NaN POI people

print 'new dataset people:{}'.format(len(enron_data)+10)
print 'new NaN for total payments:{} ({}%)'.format(result_nan[0]+10,100*round((result_nan[0]+10.)/(len(enron_data)+10.),4))
count_poi=0
for i in enron_data:
    count_poi+=enron_data[i]['poi']
print 'new number of poi in dataset:{}'.format(count_poi+10)
print 'new Number of POI E+F people have Nan as total payments: {}({}%)'.format(result[0]+10,100*round(((result[0]+10.)/(count_poi+10)),4))