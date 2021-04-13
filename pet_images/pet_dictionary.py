from os import listdir


def get_pet_labels(image_dir):

    results_dic = dict()
    filenames = listdir(image_dir)
    # print(filenames)
    pet_labels = list()
    for pet_image in filenames:
        # print(pet_image)
        low_pet_image = pet_image.lower()
        word_list_pet_image = low_pet_image.split("_")
        pet_name = ""
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "
        pet_name = pet_name.strip()
        pet_labels.append(pet_name)

    for idx in range(len(filenames)):
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx]]

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic


print(get_pet_labels("pet_images"))
