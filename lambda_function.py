import math

def sine(value):
    return math.sin(value*(22/7)/180)
def cosine(value):
    return math.cos(value*(22/7)/180)
def tangent(value):
    return math.tan(value*(22/7)/180)

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
    return say("CancelIntent", "You want to cancel")	#don't use CancelIntent as title it causes code reference error during certification 
def help_intent():
    return say("CancelIntent", "You want help")		#same here don't use CancelIntent
def stop_intent():
    return say("StopIntent", "You want to stop")		#here also don't use StopIntent
# Intent Handlers end here

def say(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = buildPlainSpeech(body)
    speechlet['card'] = buildSimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return buildResponse(speechlet)

def sayAndListen(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = buildPlainSpeech(body)
    speechlet['card'] = buildSimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return buildResponse(speechlet)

def onLaunch(event, context):
    return sayAndListen("Maths Formula", "Welcome to Maths formula")

def intentRouter(event, context):
    intent = event['request']['intent']['name']
    # Custom Intents
    if intent == 'SineIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The sine of '+str(value)+' is '+str(sine(value))
        return sayAndListen('Answer',text)
    elif intent == 'CosineIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The cosine of '+str(value)+' is '+str(cosine(value))
        return sayAndListen('Answer',text)
    elif intent == 'TangentIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The tangent of '+str(value)+' is '+str(tangent(value))
        return sayAndListen('Answer',text)
    # Required Intents
    elif intent == "AMAZON.CancelIntent":
        return cancel_intent()
    elif intent == "AMAZON.HelpIntent":
        return help_intent()
    elif intent == "AMAZON.StopIntent":
        return stop_intent()
    else:
        return say('Oops','This option is invalid right now, it might be available in the update. Please say Open Maths formula')

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return onLaunch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intentRouter(event, context)

if __name__=='__main__':
    print('The json object that is returned is...')
    print(lambda_handler('checking','json response in local'))