from discord.ext import commands, tasks
import http.client, urllib.request, urllib.parse, urllib.error, time, requests
import os
api_key = os.getenv('STATUS_API_TOKEN')
page_id = os.getenv('PAGE_ID')
smetric_id = os.getenv('SMETRIC_ID')
bmetric_id = os.getenv('BMETRIC_ID')
api_base = 'api.statuspage.io'

class API(commands.Cog):
    def __init__(self, bot):
        """Initilize. This function posts latency to the statuspage.io API."""
        self.bot = bot
        if api_key and page_id and smetric_id and bmetric_id:
            self.postapi.start()
        else:
            print("statuspage.io not configured! Not using the API")
    
    @tasks.loop(minutes=1)
    async def postapi(self):
        ts = int(time.time())
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "OAuth " + api_key}
        value = requests.get("https://amazon.com").elapsed.total_seconds()*1000
        params = urllib.parse.urlencode({'data[timestamp]': ts, 'data[value]': value})
        conn = http.client.HTTPSConnection(api_base)
        conn.request("POST", "/v1/pages/" + page_id + "/metrics/" + smetric_id + "/data.json", params, headers)
        
        print("Submitted Statcord point with value " + str(value) )


        value = requests.get("https://google.com").elapsed.total_seconds()*1000
        params = urllib.parse.urlencode({'data[timestamp]': ts, 'data[value]': value})        
        conn = http.client.HTTPSConnection(api_base)
        conn.request("POST", "/v1/pages/" + page_id + "/metrics/" + bmetric_id + "/data.json", params, headers)

        print("Submitted Bot List point with value " + str(value) )
        time.sleep(10)

def setup(bot):
    bot.add_cog(API(bot))