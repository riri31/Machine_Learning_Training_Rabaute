#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    

    from math import pow as mt
    import numpy as np

    
    residual_error = predictions-net_worths
      
    squares=[]
    squares=pow(residual_error,2)
    max=np.sort(squares,axis=None)[-9]
  
    j=0
    for i in predictions:
        if pow(predictions[j]-net_worths[j],2) <max:
            item = (ages[j], net_worths[j],residual_error[j])
            cleaned_data.append(item)
        j+=1
    print 'Length of cleaned data={}'.format(len(cleaned_data))

    
    ### your code goes here

    
    return cleaned_data

