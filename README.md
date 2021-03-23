# spoken-to-written-english
A Python project to convert Spoken language given as input to written English

## Code Walkthrough
This system can be used to convert spoken English text to written English text. 
The application is currently in development. It first takes spoken English text 
as input and then iterates through the text tokens. Depending on the tokens it 
tries to identify what knid of a statement is being spoken and it then displays 
the final written English output.

For sample purposes, the input text is set to "triple B". The system is expected 
to output "B B B".

Due to the lack of time, I could not debug the system in various use cases.
Currently, it supports the following conversion rules:
1. Currency rules
    Ex: "ninety five dollars" should be written as "$95"
2. Arithmetic signs
    Ex: "1 plus 2" should be written as "1 + 2"
3. Abbreviation
    Ex: "A C M" should be written as "ACM"
4. Time in 12/24 hour format
    Ex: "12 hundred hours" should be written as "1200 hours"

The system uses the word2number library which converts a number in words to number
in numerical form. It can be found here:
https://pypi.org/project/word2number/

## Future Extension
Rules can be easily added to this system by adding more if-else conditions in the code.
Also, we can make the system also identify cases which are a combination of multiple 
conversion rules by splitting the sentence at appropriate places. Ex: "3 apples for 20 dollars"
should give "3 apples for $20" as output. Punctuation marks should also be handled in the code.