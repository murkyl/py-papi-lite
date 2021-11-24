import papi_lite
import json
import logging

logging.basicConfig(level=logging.WARNING)
#logging.basicConfig(level=logging.DEBUG)
RUN_RAN = True
RUN_PAPI = True
pl = papi_lite.papi_lite(user='root', password='a', server='192.168.200.225:8080')

if RUN_RAN:
  print("="*50)
  print("RAN EXAMPLE")
  print("="*50)
  q_args = {'acl': 'true'}
  path_list = ['ifs', 'ifs/data']
  for p in path_list:
    response = pl.rest_call('%s'%str(p), query_args=q_args, api_type=papi_lite.API_RAN)
    print("RETURN CODE: %s"%response[0])
    print("RETURN REASON: %s"%response[1])
    print("JSON RESPONSE:\n%s"%json.dumps(response[2], indent=4))

if RUN_PAPI:
  print("="*50)
  print("PAPI EXAMPLE")
  print("="*50)
  q_args = {}
  response = pl.rest_call('/3/zones', query_args=q_args)
  print("RETURN CODE: %s"%response[0])
  print("RETURN REASON: %s"%response[1])
  print("JSON RESPONSE:\n%s"%json.dumps(response[2], indent=4))
