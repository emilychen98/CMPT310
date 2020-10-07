from pathlib import Path

#========================================================================================================
# Interactive Interpreter Class
class InteractiveInterpreter:
    def __init__(self):
        self.KB = []
        self.true_atoms = []
        self.infer = False

    def load(self, file):
        if Path(file).is_file():
            f = open(file, "r")
            rules = [rule for rule in f.readlines() if rule.strip()] # Remove blank spaces/ empty lines
            for i, rule in enumerate(rules):
                rules[i] = ' '.join(rule.split()) # Remove extra whitespace between tokens
            if self.KB:
                self.KB.clear()
                self.true_atoms.clear()
                self.infer = False
        else:
            print("Error: %s is not a valid knowledge base\n"%(file))
            return

        # check if all head / tokens are valid
        for rule in rules: 
            atoms = rule.split(' ')
            if "<--" in atoms:
                atoms.remove("<--")
            else:
                print("Error: %s is not a valid knowledge base - please input rules only\n"%(file))
                return
            atoms[:] = [x for x in atoms if x != '&']

            for atom in atoms:
                if not self.is_atom(atom):
                    print("Error: %s is not a valid knowledge base\n"%(file))
                    return
        
        self.KB = [rule.strip() for rule in rules]
        for rule in self.KB:
            print("  %s"%(rule))
        print("\n%d new rule(s) added\n"%(len(self.KB)))
    
    def tell(self, atoms):
        # No atoms
        if not atoms:
            print("Error: tell needs at least one atom\n")
            return
        # Ensure all atoms are valid
        for atom in atoms:
            if not self.is_atom(atom):
                print("Error: \"%s\" is not a valid atom\n"%(atom))
                return
        # Add atoms to KB
        for atom in atoms:
            if atom in self.KB:
                print("  Atom \"%s\" already known to be true"%(atom))
            else:
                self.KB.append(atom)
                print("  \"%s\" added to KB"%(atom))
                self.infer = True # infer_all function is now allowed
        print("")

    def infer_all(self):
        #Input : KB, containing rules and atoms
        #Output: set of all atoms that are logical consequences of KB

        if not self.infer:
            print("Error: No atoms can be inferred until one tell command is called\n")
            return

        C = [] # contains inferred atoms
        revalidate = True
        while revalidate:
            for i, rule in enumerate(self.KB):
                atoms = rule.split(' ')
                h = atoms.pop(0) # first element is the head

                for i, atom in enumerate(atoms):
                    if not self.is_atom(atom):
                        atoms.pop(i) # remove arrow and operators
                test = True
                for atom in atoms:
                    if atom not in C and atom not in self.KB:
                        test = False
            
                if len(atoms) == 0 and h not in self.true_atoms: # true atoms added through tell
                    self.true_atoms.append(h)
                    revalidate = False
                elif test and (h not in C and h not in self.KB):
                    C.append(h)
                    revalidate = True # loop through KB again to identify heads that are now true
                    break
                elif i == len(self.KB) - 1:
                    # reached end of KB without adding additional true atoms, no revalidation required
                    revalidate = False 

        print("  Newly inferred atoms:\n     ", end='')
        if len(C) == 0:
            print("<none>", end='')
        for i, atom in enumerate(C):
            if i == len(C)-1:
                print("%s "%(atom), end='')
            else:
                print("%s, "%(atom), end='')
        print("")

        print("  Atoms already known to be true:\n     ", end='')
        if len(self.true_atoms) == 0:
            print("%s "%(self.true_atoms(0)))
        else:
            for i,atom in enumerate(self.true_atoms):
                if i == len(self.true_atoms)-1:
                    print("%s "%(atom))
                else:
                    print("%s, "%(atom), end='')
        print("")

        if len(C) != 0:
            self.true_atoms = self.true_atoms + C
            self.KB = self.KB + C
        return C
       
    # returns True if, and only if, string s is a valid variable name
    def is_atom(self, s):
        if not isinstance(s, str):
            return False
        if s == "":
            return False
        return self.is_letter(s[0]) and all(self.is_letter(c) or c.isdigit() for c in s[1:])

    def is_letter(self, s):
        return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

#========================================================================================================
# Run the Interpreter
def runInterpreter():
    I = InteractiveInterpreter()
    while True: 
         print("kb> ", end='') 
         command = input()
         tokenized_command = command.split(' ')
         if tokenized_command[0] == "load":
             I.load(tokenized_command[1])
         elif tokenized_command[0] == "tell":
             tokenized_command.pop(0) # pass in all atoms to tell
             I.tell(tokenized_command)
         elif tokenized_command[0] == "infer_all":
             I.infer_all()
         else:
             print("Error: unknown command \"%s\"\n"%(tokenized_command[0]))

if __name__ == '__main__':
    runInterpreter()
