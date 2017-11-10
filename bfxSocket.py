import websocket
import json

class bfxApi:
	def subscribe(self,ws,channel,pair):
		print("Subscribing..")
		tmp=dict()
		tmp['event']='subscribe'
		tmp['channel']=channel
		tmp['symbol']=pair
		print("Debug: %s" % (json.dumps(tmp)))
		ws.send(json.dumps(tmp))
	def updateChannel(self, message):
		tmp=json.loads(message)
		self.pairs[tmp[0]].update(message)
	def on_message(self,ws, message):
		print("1")
		obj=json.loads(message)
		print(type(obj))
		if(type(obj)==list):
			print ("Message is list")
			self.updateChannel(message) 
		elif(type(obj)==dict):
			print ("Message is dict")
			#self.handleDictMessage(obj)

		if (obj['event']=='info'):
			#Subscribe
			print("Handshake recieved - subscribing channels..")
			self.subscribe(ws,'ticker','BCHUSD')
		elif(obj['event']=='subscribed'):
			print("Debug: Successfully subscribed to: %s %s" % (obj['pair'],obj['channel']))
			print("Debug: real message was: %s" % (message))
			self.pairs[obj['pair']]=pair(obj)
			#Next we would like to map a channel to a piar ...
			self.channel[obj['chanId']]=obj['pair'] 

		else:
			#print("< %s" % (message))
			print(message)

		
	def on_open(self,ws):
		print("Opening connection..")

	def __init__(self,secret='',key=''):
		self.secret=secret
		self.key=key
		ws = websocket.WebSocketApp("wss://api.bitfinex.com/ws/2",on_message=self.on_message,on_open=self.on_open)
		ws.run_forever()
		
	secret="mysecret"
	key="mykey"
	wsStatus=False
	channels=list()
	pairs=dict()

class pair:
	channel=''
	chanId=''
	pair=''
	def __init__(self,obj):
		if (obj['channel'] == 'ticker'):
			self.channel=ticker.create(obj['channel']) 
			self.chanId=obj['chanId']
			self.pair=obj['pair'] 
			
class channel_orderbook:
	event=""
	channel=""
	chanId="-99"
	pair=""
	prec=""
	freq=""




