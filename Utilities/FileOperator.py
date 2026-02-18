# import pickle
# from telnetlib import OLD_ENVIRON
# import uuid
# import os
# import datetime

# def save_obj(obj, name):
#     """
#     Saves given object as a pickle file
#     :param obj:
#     :param name:
#     :return:
#     """
#     if name[-4:] != ".pkl":
#         name += ".pkl"
#     with open(name, 'wb') as f:
#         pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


# def load_obj(name):
#     """
#     Loads a pickle file object
#     :param name:
#     :return:
#     """
#     with open(name, 'rb') as f:
#         return pickle.load(f)


# def init_file_name():
#     dayTime = datetime.datetime.now().strftime('%Y-%m-%d')
#     hourTime = datetime.datetime.now().strftime('%H-%M-%S')
#     pwd = "/home/neardws/Documents/Game-Theoretic-Deep-Reinforcement-Learning/Data/" + dayTime + '-' + hourTime

#     if not os.path.exists(pwd):
#         os.makedirs(pwd)

#     uuid_str = uuid.uuid4().hex
#     convex_environment_name = pwd + '/' + 'convex_environment_%s.pkl' % uuid_str
#     random_environment_name = pwd + '/' + 'random_environment_%s.pkl' % uuid_str
#     local_environment_name = pwd + '/' + 'local_environment_%s.pkl' % uuid_str
#     edge_environment_name = pwd + '/' + 'edge_environment_%s.pkl' % uuid_str
#     old_environment_name = pwd + '/' + 'old_environment_%s.pkl' % uuid_str
#     global_environment_name = pwd + '/' + 'global_environment_%s.pkl' % uuid_str
    
#     return {
#         "convex_environment_name": convex_environment_name,
#         "random_environment_name": random_environment_name,
#         "local_environment_name": local_environment_name,
#         "edge_environment_name": edge_environment_name,
#         "old_environment_name": old_environment_name,
#         "global_environment_name": global_environment_name,
#     }
import pickle
import os
import uuid
import datetime

def save_obj(obj, name):
    """
    Saves given object as a pickle file.
    Ensures the directory exists before saving.
    """
    # Create the directory path if it doesn't exist
    directory = os.path.dirname(name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    if not name.endswith(".pkl"):
        name += ".pkl"
        
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    print(f"--- Object saved successfully to: {name} ---")


def load_obj(name):
    """
    Loads a pickle file object.
    """
    if not os.path.exists(name):
        raise FileNotFoundError(f"Could not find the file: {name}. Make sure you ran make_environment.py first!")
        
    with open(name, 'rb') as f:
        return pickle.load(f)


def init_file_name():
    """
    Generates a consistent path for Kaggle environments.
    We use a fixed folder 'current_task' so experiment.py 
    always knows where the latest environment is.
    """
    # 1. Set the root to the Kaggle working directory
    base_data_path = "/kaggle/working/Data"
    pwd = os.path.join(base_data_path, "current_task")

    # 2. Create the directory safely
    if not os.path.exists(pwd):
        os.makedirs(pwd, exist_ok=True)

    # 3. Use fixed filenames for easy loading between scripts
    # (If you prefer unique names, you can uncomment the uuid_str lines)
    # uuid_str = uuid.uuid4().hex 
    
    return {
        "convex_environment_name": os.path.join(pwd, 'convex_environment.pkl'),
        "random_environment_name": os.path.join(pwd, 'random_environment.pkl'),
        "local_environment_name":  os.path.join(pwd, 'local_environment.pkl'),
        "edge_environment_name":   os.path.join(pwd, 'edge_environment.pkl'),
        "old_environment_name":    os.path.join(pwd, 'old_environment.pkl'),
        "global_environment_name": os.path.join(pwd, 'global_environment.pkl'),
    }