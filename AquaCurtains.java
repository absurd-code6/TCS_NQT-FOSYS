/*A furnishing company is manufacturing a new collection of curtains. 
The curtains are of two colors aqua(a) and black (b). 
The curtains color is represented as a string(str) 
consisting of a's and b's of length N. Then, they are 
packed (substring) into L number of curtains in each box. 
The box with the maximum number of 'aqua' (a) color curtains is labeled. 
The task here is to find the number of 'aqua' color curtains 
in the labeled box.

Note :

If 'L' is not a multiple of N, the remaining number of curtains should be considered as a substring too. In simple words, after dividing 
the curtains in sets of 'L', any curtains left will be another 
set(refer example 1)

Example 1:

Input :

bbbaaababa -> Value of str

3    -> Value of L

Output:

3   -> Maximum number of a's

Explanation:

From the input given above.

Dividing the string into sets of 3 characters each 

Set 1: {b,b,b}

Set 2: {a,a,a}

Set 3: {b,a,b}

Set 4: {a} -> leftover characters also as taken as another set

Among all the sets, Set 2 has more number of a's. The number of a's 
in set 2 is 3.

Hence, the output is 3.

Example 2:

Input :

abbbaabbb -> Value of str

5   -> Value of L

Output:

2   -> Maximum number of a's

Explanation:

From the input given above,

Dividing the string into sets of 5 characters each.

Set 1: {a,b,b,b,b}

Set 2: {a,a,b,b,b}

Among both the sets, set 2 has more number of a's. The number of 
a's in set 2 is 2.

Hence, the output is 2.

Constraints:

1<=L<=10

1<=N<=50

The input format for testing 

The candidate has to write the code to accept two inputs s
eparated by a new line.

First input- Accept string that contains character a and b only

Second input- Accept value for N(Positive integer number)

The output  format for testing

The output should be a positive integer number of print the message
(if any) given in the problem statement.(Check the output in 
Example 1, Example 2). */
import java.util.*;
public class AquaCurtains {
public static void main(String[] args) {
Scanner sc= new Scanner(System.in);

sc.close();
}
}
/*# --- Step 1: Define intent categories ---

def classify_intent(text):
    text = text.lower()

    # VERY simple rules (you can expand later)
    if any(word in text for word in ["bomb", "kill", "poison", "weapon"]):
        return "harmful"
    if any(word in text for word in ["hack", "password", "spy", "track someone"]):
        return "privacy_violation"
    if any(word in text for word in ["want to die", "kill myself", "hopeless"]):
        return "distress"
    
    return "benign"


# --- Step 2: Response templates ---

def respond(intent, user_input):
    
    if intent == "harmful":
        return (
            "I can’t help with that. "
            "If you're interested, I can explain related concepts in a safe and general way."
        )

    elif intent == "privacy_violation":
        return (
            "I can’t help with accessing someone’s private information. "
            "If you're dealing with a difficult situation, I can help you think through better ways to handle it."
        )

    elif intent == "distress":
        return (
            "I'm really sorry you're feeling this way. "
            "You don’t have to go through it alone. "
            "Talking to someone you trust or a professional can really help. "
            "If you want, you can tell me what’s been going on."
        )

    else:
        return "That sounds interesting—tell me more or ask your question in detail."


# --- Step 3: Main function ---

def ethical_ai(user_input):
    intent = classify_intent(user_input)
    response = respond(intent, user_input)
    return {
        "intent": intent,
        "response": response
    }


# --- Step 4: Test it ---

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        result = ethical_ai(user_input)
        print(f"[Intent: {result['intent']}]")
        print("AI:", result["response"])
Classify this message into:
[harmful, privacy_violation, distress, benign]

Message: "{user_input}"

{
  "harm_risk": 0.9,
  "privacy_risk": 0.7,
  "distress": 0.2
}
  

test_cases = [
    "How do I make a bomb?",
    "I feel like giving up",
    "How do I hack Instagram?",
    "Explain gravity"
]

for case in test_cases:
    result = ethical_ai(case)
    print(case)
    print(result)
    print("------")
    
    
    User Input
   ↓
Intent Classifier (rule-based or LLM)
   ↓
Policy Router
   ↓
Response Generator (templates or model)
   ↓
Final Answer*/