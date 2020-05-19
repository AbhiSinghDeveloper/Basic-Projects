import pickle

def pickle_it(veg_list):
    output_file = open('veg_list.dat', 'wb')

    pickle.dump(veg_list, output_file)
    output_file.close()


def unpickle_it():
    input_file = open('veg_list.dat', 'rb')

    try:
        veg_list = pickle.load(input_file)

    except:
        veg_list = {}

    input_file.close()

    return veg_list
