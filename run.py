"""Running the Xetra ETL application"""

import logging
import logging.config
import yaml


def main():
    # entry point to run the Xetra ETL job
    # parsing the Yaml file
     config_path ='C:/Users/jigee/OneDrive/Desktop/Spring22/Assignments/Cloud/Projects/Project_1/Cloud_FinalProject/configs/report1_config.yml'
     config = yaml.safe_load(open(config_path))
     #configure logging 
     log_config = config['logging']
     logging.config.dictConfig(log_config)
     logger= logging.getLogger(__name__)
     logger.info("This is a test.")


if __name__ == '__main__':
    main()