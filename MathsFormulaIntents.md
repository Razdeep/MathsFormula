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
                },
                {
                    "name": "CosineIntent",
                    "slots": [
                        {
                            "name": "value",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "What is the cosine of {value} degree",
                        "What is the cos of {value} degree",
                        "Tell me the cosine of {value}",
                        "Cosine of {value}",
                        "Cos of {value}",
                        "Tell me the cos of {value}"
                    ]
                },
                {
                    "name": "TangentIntent",
                    "slots": [
                        {
                            "name": "value",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "Tangent of {value}",
                        "Tan of {value}",
                        "Tell me the tan of {value}",
                        "Tell me the tangent of {value}",
                        "what is tan of {value}",
                        "What is the tangent of {value} degree"
                    ]
                }
            ],
            "types": []
        }
    }
}