'''
 *
 * Copyright (C) Rajdeep Roy Chowdhury 2019 <rrajdeeproychowdhury@gmail.com>
 *
 * You may redistribute it and/or modify it under the terms of the
 * GNU General Public License, as published by the Free Software
 * Foundation; either version 2 of the License, or (at your option)
 * any later version.
 *
 * MathsFormula is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
'''

from logic import Logic

ending_text='Thank you for using Maths Formula. You can always invoke this skill by saying "Alexa, open Maths Formula".'

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

def say(title, body):
    body=body+'. '+ending_text
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

def sayWithoutCards(text):
    speechlet = {}
    speechlet['outputSpeech'] = buildPlainSpeech(text)
    speechlet['shouldEndSession'] = True
    return buildResponse(speechlet)

def onLaunch(event, context):
    text= "Welcome to Maths formula, you can ask me to compute any mathematical function by saying something like, 'What is the sine of 45 degree?' or say 'Learn maths formula' to learn new maths formulae"
    return sayAndListen("Maths Formula",text)

def intentRouter(event, context):
    intent = event['request']['intent']['name']
    logic = Logic()
    # Custom Intents
    if intent == 'FormulaIntent':
        text = 'Let\'s learn maths formula...\n'
        for i in logic.formula.keys():
            text = text + logic.formula[i] + '. '
        return sayWithoutCards(text)
    elif intent == 'SineIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The sine of '+str(value)+' is '+str(logic.sine(value))
        return say('Answer',text)
    elif intent == 'CosineIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The cosine of '+str(value)+' is '+str(logic.cosine(value))
        return say('Answer',text)
    elif intent == 'TangentIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The tangent of '+str(value)+' is '+str(logic.tangent(value))
        return say('Answer',text)
    elif intent == 'CosecIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The cosec of '+str(value)+' is '+str(1/logic.sine(value))
        return say('Answer',text)
    elif intent ==  'SecantIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The secant of '+str(value)+' is '+str(1/logic.cosine(value))
        return say('Answer',text)
    elif intent == 'CotIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=float(value)
        text='Haha! The cot of '+str(value)+' is '+str(1/logic.tangent(value))
        return say('Answer',text)
    elif intent == 'FactorialIntent':
        value=event['request']['intent']['slots']['value']['value']
        value=int(value)
        text='Haha! The factorial of '+str(value)+' is '+str(logic.factorial(value))
        return say('Answer',text)
    elif intent == 'PowerIntent':
        ''' Here a is the base and b is the exponent'''
        a=event['request']['intent']['slots']['a']['value']
        b=event['request']['intent']['slots']['b']['value']
        a=int(a)
        b=int(b)
        text='Haha! The value of '+str(a)+' to the power '+str(b)+' is '+str(a**b)
        return say('Answer',text)
    elif intent == 'NaturalNumbersIntent':
        n=event['request']['intent']['slots']['n']['value']
        n=int(n)
        text='Haha! The Sum of the first '+str(n)+' Natural Numbers is '+str(logic.sumOfNaturalNumbers(n))
        return say('Answer',text)
    elif intent == 'nPrIntent':
        n=event['request']['intent']['slots']['n']['value']
        r=event['request']['intent']['slots']['r']['value']
        n=int(n)
        r=int(r)
        text='Haha! The value of '+str(n)+' P '+str(r)+' is '+str(logic.factorial(n)//(logic.factorial(n-r)))
        return say('Answer',text)
    elif intent == 'nCrIntent':
        n=event['request']['intent']['slots']['n']['value']
        r=event['request']['intent']['slots']['r']['value']
        n=int(n)
        r=int(r)
        text='Haha! The value of '+str(n)+' C '+str(r)+' is '+str(logic.factorial(n)//(logic.factorial(n-r)*logic.factorial(r)))
        return say('Answer',text)
    elif intent == 'AboutIntent':
        text='I was created by Rajdeep Roy Chowdhury. '
        return say('Developer',text)
    # Required Intents
    elif intent == "AMAZON.CancelIntent":
        return sayWithoutCards("Ok! Cancelling...")
    elif intent == "AMAZON.HelpIntent":
        text=('You can ask me to calculate trigonometric functions, Factorials,'
        'Exponents, Permutations and combinations. I would learn more functions as soon as possible.')
        return sayAndListen('Help',text)
    elif intent == "AMAZON.StopIntent":
        return sayWithoutCards("Ok! Stopping...")
    else:
        return say('Oops','Oops! This option is invalid right now, it might be available in the next version.')

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return onLaunch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intentRouter(event, context)

# For local debugging purposes only
if __name__=='__main__':
    print('The json object that is returned is...')
    print(Logic().formula['sin2X'])
    # json_request=dict()
    # context=dict()
    # print(lambda_handler(json_request,context))
    # This is only for debugging locally