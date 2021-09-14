import os
import pickle

file = 'algo_db_rds.pkl'
config = {'db': {'user': 'postgres',
                 'password': 'wasddddddii'
                 },
          'finnhub': {'api': 'c4m0o2iad3icjh0e9gd0'
                      },
          'twilio': {'sid': 'AC682642684bf969ec88020bbed473e381',
                     'token': 'b46895276babfaebf376c557d290ea81'}
          }
with open(file, 'wb') as f:
    pickle.dump(config, f)