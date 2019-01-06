{
    "interactionModel": {
        "languageModel": {
            "invocationName": "maths formula",
            "intents": [
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                },
                {
                    "name": "SineIntent",
                    "slots": [
                        {
                            "name": "value",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "Tell me the sine of {value}",
                        "Sine of {value}",
                        "What is the sine of {value} degree"
                    ]
                }
            ],
            "types": []
        }
    }
}