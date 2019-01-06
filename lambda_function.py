import math

def sine(value):
    return round(math.sin(value*(22/7)/180))
def cosine(value):
    return round(math.cos(value*(22/7)/180))
def tangent(value):
    return round(math.tan(value*(22/7)/180))

def buildPlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech

def buildResponse(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response

def buildSimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card

# Intent Handlers
def cancel_intent():
    return statement("CancelIntent", "You want to cancel")	#don't use CancelIntent as title it causes code reference error during certification 
def help_intent():
    return statement("CancelIntent", "You want help")		#same here don't use CancelIntent
def stop_intent():
    return statement("StopIntent", "You want to stop")		#here also don't use StopIntent
# Intent Handlers end here

def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = buildPlainSpeech(body)
    speechlet['card'] = buildSimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return buildResponse(speechlet)

def statementAndListen(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = buildPlainSpeech(body)
    speechlet['card'] = buildSimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return buildResponse(speechlet)

def onLaunch(event, context):
    return statementAndListen("Maths Formula", "Welcome to Maths formula created by Rajdeep Roy Chowdhury")

def intentRouter(event, context):
    intent = event['request']['intent']['name']
    # Custom Intents
    if intent == 'SineIntent':
        return 'This would return Sine Json object'
    # Required Intents
    if intent == "AMAZON.CancelIntent":
        return cancel_intent()
    if intent == "AMAZON.HelpIntent":
        return help_intent()
    if intent == "AMAZON.StopIntent":
        return stop_intent()

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return onLaunch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intentRouter(event, context)

if __name__=='__main__':
    print('The json object that is returned is...')
    print(lambda_handler('checking','json response in local'))