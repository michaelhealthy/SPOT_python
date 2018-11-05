import numpy as np


if __name__ == '__main__':
    # Flo files are stored here
    flow_files_lib = '/Users/michaelkolomenkin/Code/ml/flownet2-pytorch/work/inference/run.epoch-0-flow-field/'
    # Image files
    img_files_lib = '/Users/michaelkolomenkin/Data/tel_ha_shomer/1524472684/clean/'
    # pickle for features
    features = '/Users/michaelkolomenkin/Data/tel_ha_shomer/1524472684/clean/features.txt'

    # save_feature_file(flow_files_lib, img_files_lib, features)
    # pd.read_pickle(pickle_features)
    reconstruct_from_features(features)
