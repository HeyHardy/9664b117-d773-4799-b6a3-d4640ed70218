#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    
    
  dognames_dic = dict()

   
  with open(dogfile, "r") as infile:
        # Reads in dognames from first line in file
        line = infile.readline()
 
        while line != "":

          line = line.strip()
          if line not in dognames_dic:
            dognames_dic[line] = 1
            line = infile.readline()

  
  for key in results_dic:
      pet_label = results_dic[key][0]
      classifier_label = results_dic[key][1]
        # Pet Image Label IS of Dog (e.g. found in dognames_dic)
      
      if pet_label in dognames_dic:
       
            if classifier_label in dognames_dic:
                results_dic[key].extend((1, 1))

            else:
                results_dic[key].extend((1, 0))
                pass

        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
      else:
            if classifier_label in  dognames_dic:
               # Nur Classifier ist Hund
                results_dic[key].extend((0, 1))
          
            else:
                  # Keiner ist Hund
                results_dic[key].extend((0, 0))
            pass
    
 
