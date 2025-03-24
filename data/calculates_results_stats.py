def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using the 
    classifier's model architecture to classify pet images. Then puts the 
    results statistics in a dictionary (results_stats_dic) so that it's 
    returned for printing to help the user determine the 'best' model for 
    classifying images. 
    Note that the statistics calculated as the results are either 
    percentages or counts.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index) idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
      results_stats_dic - Dictionary containing the results statistics 
                          (percentages or counts) where the key is the 
                          statistic's name (starting with 'pct' for 
                          percentage or 'n' for count) and the value 
                          is the statistic's value.
    """        
    # Creates an empty dictionary for results_stats_dic
    results_stats_dic = dict()
    
    # Initialize counters to zero
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0
    
    # Process through the results dictionary
    for key in results_dic:
         
        # If pet label and classifier label are an exact match, increment n_match
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # TODO: 5a. Count how many dog images were correctly classified by breed:
        # That means pet label is-a-dog (idx 3 == 1) AND pet and classifier 
        # labels match (idx 2 == 1).
        if (results_dic[key][3] == 1) and (results_dic[key][2] == 1):
            results_stats_dic['n_correct_breed'] += 1
        
        # If pet image is a dog, increment n_dogs_img
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # If classifier also says dog, increment n_correct_dogs
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        else:
            # TODO: 5b. If pet is NOT a dog, check if classifier also says NOT a dog
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate total number of images
    results_stats_dic['n_images'] = len(results_dic)

    # Calculate the number of "not-a-dog" images
    results_stats_dic['n_notdogs_img'] = (
        results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']
    )

    # TODO: 5c. Percentage of correct matches: (n_match / n_images) * 100
    results_stats_dic['pct_match'] = (
        results_stats_dic['n_match'] / results_stats_dic['n_images']
    ) * 100.0

    # TODO: 5d. Percentage of correctly classified dog images:
    # (n_correct_dogs / n_dogs_img) * 100
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (
            results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0

    # TODO: 5e. Percentage of correctly classified dog breeds:
    # (n_correct_breed / n_dogs_img) * 100
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = (
            results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_breed'] = 0.0

    # Percentage of correctly classified “not-a-dog” images:
    # If n_notdogs_img > 0, then (n_correct_notdogs / n_notdogs_img)*100
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (
            results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    # TODO 5f. Return the results_stats_dic dictionary you created
    return results_stats_dic
