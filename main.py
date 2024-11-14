import re
import sys
import traceback

import requests
from log import getLogger

if __name__ == '__main__':
    print(sys.argv[1],sys.argv[2])
    endpoint = "http://10.68.198.66/SLTCrbt/ProvisionCallback.php";

    headers= {'content-type':'text/xml'}

    logger = getLogger('crbt', 'logs/crbt')

    xmlfile = open('files/CallBackStatus.xml', 'r')
    body = xmlfile.read()

    try:
        response = requests.request("POST",endpoint,headers=headers,
                                    data=body.format(msisdn=sys.argv[1],status= sys.argv[2] ))

        print(response.request.body)
        logger.info("Start : =========================================================================")
        logger.info(response.request.body)

        logger.info("Response : =================================")
        logger.info(response.text)
        logger.info("End : =========================================================================")

        ResultCode = re.findall("<return xsi:type=\"xsd:string\">(.*?)</return>", str(response.content))
        print(ResultCode[0])

    except Exception as e:
        logger.error(e)
        print("Exception : %s" % traceback.format_exc())


