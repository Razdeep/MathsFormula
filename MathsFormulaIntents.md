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
                        "What is the value of sine {value}",
                        "What is the value of sine {value} degree",
                        "What is sine of {value}",
                        "What is sine of {value} degree",
                        "What is the sine of {value}",
                        "What is the sine of {value} degree",
                        "Tell me the sine of {value}",
                        "Tell me the sine of {value} degree",
                        "Tell me sine of {value}",
                        "Tell me sine of {value} degree",
                        "Sine of {value}",
                        "Sine of {value} degree"
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
                        "What is the cosine of {value}",
                        "What is the cos of {value}",
                        "What is cosine of {value} degree",
                        "What is cos of {value} degree",
                        "What is cosine of {value}",
                        "What is cos of {value}",
                        "Tell me the cosine of {value}",
                        "Tell me the cos of {value}",
                        "Tell me cosine of {value}",
                        "Tell me cos of {value}",
                        "Tell me the cosine of {value} degree",
                        "Tell me the cos of {value} degree",
                        "Tell me cosine of {value} degree",
                        "Tell me cos of {value} degree",
                        "Cosine of {value}",
                        "Cos of {value}",
                        "Cosine of {value} degree",
                        "Cos of {value} degree"
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
                        "Tangent of {value} degree",
                        "Tan of {value} degree",
                        "Tell me the tan of {value}",
                        "Tell me the tangent of {value}",
                        "Tell me the tan of {value} degree",
                        "Tell me the tangent of {value} degree",
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
                        "Who is your developer",
                        "Who made you",
                        "Who created you",
                        "Who is your creator"
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
                        "What is the value of cosec {value}",
                        "What is the value of cosec {value} degree",
                        "What is cosec of {value}",
                        "What is cosec of {value} degree",
                        "What is the cosec of {value}",
                        "What is the cosec of {value} degree",
                        "Tell me the cosec of {value}",
                        "Tell me the cosec of {value} degree",
                        "Tell me cosec of {value}",
                        "Tell me cosec of {value} degree",
                        "cosec of {value}",
                        "cosec of {value} degree"
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
                        "What is the secant of {value} degree",
                        "What is the sec of {value} degree",
                        "What is the secant of {value}",
                        "What is the sec of {value}",
                        "What is secant of {value} degree",
                        "What is sec of {value} degree",
                        "What is secant of {value}",
                        "What is sec of {value}",
                        "Tell me the secant of {value}",
                        "Tell me the sec of {value}",
                        "Tell me secant of {value}",
                        "Tell me sec of {value}",
                        "Tell me the secant of {value} degree",
                        "Tell me the sec of {value} degree",
                        "Tell me secant of {value} degree",
                        "Tell me sec of {value} degree",
                        "secant of {value}",
                        "sec of {value}",
                        "secant of {value} degree",
                        "sec of {value} degree"
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
                        "What is the value of cot {value}",
                        "What is the value of cot {value} degree",
                        "What is cot of {value}",
                        "What is cot of {value} degree",
                        "What is the cot of {value}",
                        "What is the cot of {value} degree",
                        "Tell me the cot of {value}",
                        "Tell me the cot of {value} degree",
                        "Tell me cot of {value}",
                        "Tell me cot of {value} degree",
                        "cot of {value}",
                        "cot of {value} degree"
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
                        "What is the value of factorial {value}",
                        "What is value of factorial {value}",
                        "What is value of {value} factorial",
                        "What is the value of {value} factorial",
                        "{value} factorial",
                        "Factorial {value}",
                        "What is the factorial of {value}",
                        "What is factorial of {value}"
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
                },
                {
                    "name": "FormulaIntent",
                    "slots": [],
                    "samples": [
                        "Learn math formulas",
                        "Learn maths formulae",
                        "Learn maths formula",
                        "Learn formula",
                        "Learn math formula"
                    ]
                }
            ],
            "types": []
        }
    }
}