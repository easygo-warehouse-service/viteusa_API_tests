
import configparser,os,requests,json
proDir = os.getcwd()
configPath = os.path.join(proDir, "config\config.ini")
cf = configparser.ConfigParser()
cf.read(configPath)#encoding="utf-8-sig"






class Login_Token():
    def API_post_202012(self,url, payload):
        headers = {
            "x-api-key":"4bRfkpv7nr9sBNOEa3vkN44iK5Q9vVh99loZSOnJ",'Content-Type': 'application/json',
        }
        payload=json.dumps(payload)

        response = requests.request("POST", "%s" % (url), headers=headers, data=payload)
        re = json.loads(response.text)
        # print('入参：%s;返回值：%s' % (payload, re))
        return re
