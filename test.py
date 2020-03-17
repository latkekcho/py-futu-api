# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:30:17 2020

@author: Caesar
"""

from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
print(quote_ctx.get_future_info(["HK.999010"]))
quote_ctx.close()