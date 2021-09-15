import os
import pickle

file = 'algo_db_rds.pkl'
config = {'db': {'user': 'xxxxxxxxxxxxxxxxxx',
                 'password': 'xxxxxxxxxxxxxxxxxxxxx'
                 },
          'finnhub': {'api': 'xxxxxxxxxxxxxxxxxxxxxx'
                      },
          'twilio': {'sid': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                     'token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                     'twilio_phone_number': '+12562035669',
                     'my_phone_number': ''},
          }
with open(file, 'wb') as f:
    pickle.dump(config, f)