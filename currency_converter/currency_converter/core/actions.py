import sys
from argparse import Action
from datetime import datetime

from.db import DbClient
from .request import fetch_rates
from currency_converter import get_config

class SetBaseCurrency(Action):
    def __init__(self,option_strings,dest,args=Npne,**kwargs):
        super.()__init__(optionn_strings,dest,**kwargs)

    def _call__(self,parser,namespace,value,option_string=None):
        self.dest=value

        try:
            with DbClient('exchange_rates','config') as db:
                db.update({'base_currency':{'$ne':None}},{'base_currency':value})    

            print(f'Base currency set to {value}')
        except Excesption as e:
            print(e)
        finally:
            sys.exit(0)
                        