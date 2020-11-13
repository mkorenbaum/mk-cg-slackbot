###
### Slackbot general settings
###

# Slack API token to send/rcv messages
API_TOKEN = "xoxb-1017282983751-1506637546049-oizILOz6AapoborSwg6upuwh"


# Plugins - add Slackbot CloudGenix
PLUGINS = [
    'slackbot_cloudgenix',
]

# Errors / crashes, send to channel name
ERRORS_TO = 'cgx-demo-bot-errors'


###
### CloudGenix Related items
###

# Default reply
DEFAULT_REPLY = "Hello! I didn't understand you. Sorry!"

# CloudGenix AUTH token - minimum 'view_only', generate from CloudGenix Portal -> System Administration -> AUTH_TOKEN
# NOTE - this is a very long string! please quote!
# CGX Allstars Token #
CLOUDGENIX_AUTH_TOKEN = '030fbed6ec6ba61cb40bd2fff6c5089b674130bc-pa.u.exp=9223372036854775807&pa.p.id=password&t.id=1529&s.id=2&pa.u.id=mike.korenbaum%40cloudgenix.com&o.id=15004976533530062&region=elcapitan&client_ip=54.215.252.241&session_key=8oQSiYClDoUKUIp3XS4N2uo2L644RSppdXpltPSDI9aIpXey9NGPhTrYwnLTRriRsb1iEpKPw1ZK6r0BGWwVbLn8VAX6selwxSMLzW0WwV58alKw7B2hlPSJit44ihphcExuxWqoGZI06osmZCWtSwLK8wulAz5nJiXrxwUo7ae02sBPNuQ0DDTaPivNfRRfiWbGCItM'

# NWM Token #
#CLOUDGENIX_AUTH_TOKEN="4eb5978eade4fbb83001c8d5e760768ef2f4ab5d-pa.u.exp=9223372036854775807&pa.p.id=password&t.id=1146&s.id=2&pa.u.id=mike.korenbaum%40cloudgenix.com&o.id=15004976533530062&region=elcapitan&client_ip=54.215.252.241&session_key=N1EXjZ0G69NxHf1k6ApCeDRbOF0y7NC18fREnhX9Qrr3uml9YeOCkpQY9EDRaKQ2mU2JhFbwMFt4JaQeqAwyvWSvo6bVHmqrgJLfB9WWUGrCRjUqFurETIVDg9VICZh8VsQMzLCyEhWcjzWTdNsHgAvNgUny0KjBRXyhWM9X9QDYavySSqcRGG1v4QakrtwAgrJcnYfM"



###
### Debug level
#DEBUG_LEVEL = 3
###
