from discord.ext import commands, tasks
import http.client, urllib.request, urllib.parse, urllib.error, time, requests

api_key = ''
page_id = ''
smetric_id = ''
bmetric_id = ''
api_base = 'api.statuspage.io'

class API(commands.Cog):
    def __init__(self, bot):
        """Initilize. This function posts latency to the statuspage.io API."""
        self.bot = bot
        self.postapi.start()
    
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