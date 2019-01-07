import math

def sine(value):
    '''Returns sine of an angle (in degrees)'''
    return math.sin(value*(22/7)/180)
def cosine(value):
    '''Returns cosine of an angle (in degrees)'''
    return math.cos(value*(22/7)/180)
def tangent(value):
    '''Returns tangent of an angle (in degrees)'''
    return math.tan(value*(22/7)/180)
def sumOfNaturalNumbers(n):
    '''Return sum of n natural numbers'''
    return n*(n+1)//2

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
def helpIntent():
    text='You can ask me calculate sine, cos, tan of any value. I would learn more functions as soon as possible.'
    return sayAndListen("Help", text)		#same here don't use CancelIntent
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
    elif intent == 'CosecIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The cosec of '+str(value)+' is '+str(1/sine(value))
        return sayAndListen('Answer',text)
    elif intent ==  'SecantIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The secant of '+str(value)+' is '+str(1/cosine(value))
        return sayAndListen('Answer',text)
    elif intent == 'CotIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The cot of '+str(value)+' is '+str(1/tangent(value))
    elif intent == 'AboutIntent':
        return sayAndListen('Developer','I was created by Rajdeep Roy Chowdhury')
    # Required Intents
    elif intent == "AMAZON.CancelIntent":
        return cancel_intent()
    elif intent == "AMAZON.HelpIntent":
        return helpIntent()
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
    json_request=dict()
    context=dict()
    print(lambda_handler(json_request,context))
    # This is only for debugging locally