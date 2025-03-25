def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
                    [ 
                      idx 0 = pet image label (string)
                      idx 1 = classifier label (string)
                      idx 2 = 1/0 (int) where 1 = labels match, 0 = no match
                      idx 3 = 1/0 (int) where 1 = pet image 'is-a' dog, 
                                           0 = pet Image 'is-NOT-a' dog
                      idx 4 = 1/0 (int) where 1 = Classifier classifies image 'as-a' dog,
                                           0 = Classifier classifies image 'as-NOT-a' dog
                    ]
      results_stats_dic - Dictionary containing the results statistics (percentages or counts) 
                          where the key is the statistic's name (starting with 'pct' for 
                          percentage or 'n' for count) and the value is the statistic's value
      model - Indicates which CNN model architecture is used: resnet | alexnet | vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything (default: False)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything (default: False) 
    Returns:
      None - simply printing results
    """
    # Print summary of results
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    
    # TODO: 6a. Print out the number of NOT-dog images
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Print a blank line for readability
    print(" ")
    
    # Print summary statistics (only the percentages) from results_stats_dic
    for key in results_stats_dic:
        # TODO: 6b. Print all key-value pairs where the key starts with 'p'
        #          (indicating it's a percentage)
        if key.startswith('p'):
            print("{}: {:.1f}%".format(key, results_stats_dic[key]))

    # Check whether to print incorrectly classified dogs
    # Only print if print_incorrect_dogs is True AND
    # the total number of correct dog + correct not-dog does NOT equal
    # total images (meaning there's at least one incorrect dog/not-dog).
    if (print_incorrect_dogs and 
        ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
         != results_stats_dic['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        for key in results_dic:
            # TODO: 6c. Print out pet & classifier labels for incorrectly 
            #          classified dogs:
            #   1) pet is-a-dog but classifier says NOT-a-dog
            #   2) pet is-NOT-a-dog but classifier says is-a-dog
            if ((results_dic[key][3] == 1 and results_dic[key][4] == 0) or
                (results_dic[key][3] == 0 and results_dic[key][4] == 1)):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], 
                                                                 results_dic[key][1]))

    # Check whether to print incorrectly classified breeds
    # Only print if print_incorrect_breed is True AND
    # the number of correctly classified dogs doesn't equal
    # the number of correctly classified breeds (meaning at least one breed
    # was misclassified).
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nINCORRECT Dog Breed Assignment:")

        for key in results_dic:
            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if (sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],
                                                                 results_dic[key][1]))
