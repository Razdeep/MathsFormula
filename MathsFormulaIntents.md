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
                },
                {
                    "name": "AboutIntent",
                    "slots": [],
                    "samples": [
                        "What is the name of the developer who created you",
                        "Who is the developer",
                        "Who made you",
                        "Who created you"
                    ]
                },
                {
                    "name": "CosecIntent",
                    "slots": [
                        {
                            "name": "value",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "Tell me the cosec of {value}",
                        "Cosec of {value}",
                        "What is the cosec of {value} degree"
                    ]
                },
                {
                    "name": "SecantIntent",
                    "slots": [
                        {
                            "name": "value",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "secant of {value}",
                        "sec of {value}",
                        "What is the sec of {value} degree",
                        "What is the secant of {value} degree",
                        "Tell me the sec of {value}",
                        "Tell me the secant of {value}"
                    ]
                },
                {
                    "name": "CotIntent",
                    "slots": [
                        {
                            "name": "value",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "cot of {value}",
                        "Tell me the cot of {value}",
                        "What is the cot of {value} degree"
                    ]
                },
                {
                    "name": "FactorialIntent",
                    "slots": [
                        {
                            "name": "value",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "What is the value of {value} factorial",
                        "{value} factorial",
                        "Factorial {value}",
                        "What is the factorial of {value}"
                    ]
                },
                {
                    "name": "PowerIntent",
                    "slots": [
                        {
                            "name": "a",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "b",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "What is {a} power {b}",
                        "What is {a} to the power {b}",
                        "{a} to power {b}",
                        "{a} power {b}",
                        "{a} raised to the power {b}",
                        "What is the value of {a} to the power {b}"
                    ]
                },
                {
                    "name": "NaturalNumbersIntent",
                    "slots": [
                        {
                            "name": "n",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "Tell me the sum of first {n} natural numbers",
                        "Tell me the sum of first {n} numbers",
                        "What is the sum of first {n} natural numbers"
                    ]
                },
                {
                    "name": "nPrIntent",
                    "slots": [
                        {
                            "name": "n",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "r",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "Tell me the value of {n} P {r}",
                        "What is the value of {n} P {r}",
                        "Tell me what is {n} P {r}",
                        "{n} P {r}",
                        "What is {n} P {r}"
                    ]
                },
                {
                    "name": "nCrIntent",
                    "slots": [
                        {
                            "name": "n",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "r",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "Tell me the value of {n} C {r}",
                        "What is the value of {n} C {r}",
                        "Tell me what is {n} C {r}",
                        "{n} C {r}",
                        "What is {n} C {r}"
                    ]
                }
            ],
            "types": []
        }
    }
}