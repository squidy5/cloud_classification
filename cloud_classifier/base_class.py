import json
import os
from joblib import dump, load


class base_class:
    """
    Provides basic functionaltiry of parameter management and persistence 
    """


    def __init__(self, **kwargs):

        self.setting_files = [
            "config.json", 
            "training_sets.json", 
            "data_structure.json", 
            "input_files.json"
            ]
        dirname = os.path.dirname(__file__)

        self.default_path = os.path.join(dirname, "defaults")
        # self.__config_file = os.path.join("settings","config.json")
        # self.__data_file = os.path.join("settings","training_data.json")
        # self.__structure_file = os.path.join("settings","data_structure.json")



        if(not hasattr(self, 'class_variables')):
            print("Could not initalize class variables")
            return

        # init all class parameterst
        self.__dict__.update((k,None) for k in self.class_variables)
        self.load_settings(self.default_path)
        # update with given parameters
        self.set_parameters(**kwargs)


    def init_class_variables(self, class_variables):
        if (not hasattr(self, 'class_variables')):
            self.class_variables = []
        self.class_variables = set(self.class_variables).union(set(class_variables))


    def load_settings(self, path):
        for file in self.setting_files:
            filepath = os.path.join(path, "settings", file)
            self.load_parameters(filepath)

    def save_settings(self, path):
        for file in self.setting_files:
            filepath = os.path.join(path, "settings", file)
            self.save_parameters(path)



    def set_parameters(self, **kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in self.class_variables)


    def load_parameters(self, filepath):
        """
        Reads json file for parameters
        """

        with open(filepath, 'r') as parameters:
            kwargs =  json.load(parameters)
            self.set_parameters(**kwargs)


    def save_parameters(self, filepath):
        """
        Writes parameters
        """
        # get saved entries
        with open(filepath, 'r') as outfile:
            saved_params =  json.load(outfile)
            # update saved params
            saved_params.update({k:self.__dict__[k] for k in saved_params.keys() if k in self.class_variables})
            json_obj = json.dumps(saved_params, indent = 4)

        # write json
        with open(filepath, 'w') as outfile:
             outfile.write(json_obj)







    # def load_parameters_old(self, path, type = "config"):
    #     """
    #     Reads json file for parameters
    #     """

    #     file = self.__parse_parameter_type(type)
    #     filepath = os.path.join(path, file)
    #     with open(filepath, 'r') as parameters:
    #         kwargs =  json.load(parameters)
    #         self.set_parameters(**kwargs)


    # def save_parameters_old(self, path, type = "config"):
    #     """
    #     Writes parameters
    #     """

    #     file = self.__parse_parameter_type(type)
    #     filepath = os.path.join(path, file)

    #     # get saved entries
    #     with open(filepath, 'r') as outfile:
    #         saved_params =  json.load(outfile)
    #         # update saved params
    #         saved_params.update({k:self.__dict__[k] for k in saved_params.keys() if k in self.class_variables})
    #         json_obj = json.dumps(saved_params, indent = 4)

    #     # write json
    #     with open(filepath, 'w') as outfile:
    #          outfile.write(json_obj)




    # def get_class_variables(self):
    #     return list(self.class_variables)




    # def __parse_parameter_type(self, type):
    #     """
    #     Match type argument to settings file
    #     """
    #     file = None
    #     if (type == "config"):
    #         file = self.__config_file
    #     elif (type == "training_data"):
    #         file = self.__data_file
    #     elif (type == "data_structure"):
    #         file = self.__structure_file
    #     else:
    #         print("No valid parameter type given")
    #     return file



