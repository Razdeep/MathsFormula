#!/bin/bash
echo "Removing MathsFormula.zip"
rm MathsFormula.zip
echo "Zipping files"
zip -r ./MathsFormula.zip ./*
echo "Successfully created MathsFormula.zip"