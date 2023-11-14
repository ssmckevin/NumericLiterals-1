class FloatingPointDFA:
    states = {"q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12" } # Set of States of decimal integer DFA
    acceptstates = {"q5", "q6", "q8"} # Set of accept States of decimal integer DFA
    start_state = "q1" # initial state
    alphabet = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", ".", "E", "e", "+", "-"}
    digit = alphabet - {"_",  ".", "E", "e", "+", "-"}
    transition = {}

    def __init__(self):
        self.transition = { # transition function for all states
            "q1": lambda c: "q2" if c in self.digit else("q4" if c=="." else "q12"), 
            "q2": lambda c: "q2" if c in self.digit else("q3" if c=="_" else ("q5" if c=="." else ("q7" if c=="e" or c=="E"else "q12"))),
            "q3": lambda c: "q2" if c in self.digit else "q12",
            "q4": lambda c: "q6" if c in self.digit else "q12",
            "q5": lambda c: "q6" if c in self.digit else("q7" if c=="e" or c=="E" else "q12"),
            "q6": lambda c: "q6" if c in self.digit else("q7" if c=="e" or c=="E" else ("q9" if c=="_" else "q12")),
            "q7": lambda c: "q8" if c in self.digit else("q10" if c=="+" or c=="-" else "q12"),
            "q8": lambda c: "q8" if c in self.digit else("q11" if c=="_" else "q12"),
            "q9": lambda c: "q6" if c in self.digit else "q12",
            "q10": lambda c: "q8" if c in self.digit else "q12",
            "q11": lambda c: "q8" if c in self.digit  else "q12",
            "q12": lambda c: "q12"
        }
    
    def accepts(self, str):
        state = self.start_state # set start state
        for char in str: # Step through characters in input
            state = self.transition[state](char) # apply lambda based on state
            
        if state in self.acceptstates: 
            return True # accept if final state is in accept states
        else:
            return False
        