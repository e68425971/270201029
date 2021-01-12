class Dna:
    def __init__(self, dnaString):
        self.dnaString = dnaString
        self.containList = [letter for letter in dnaString]

    def countNucleotides(self):
        self.countA = self.containList.count("A")
        self.countC = self.containList.count("C")
        self.countG = self.containList.count("G")
        self.countT = self.containList.count("T")
        dictionary = {"A": self.countA, "C": self.countC, "G": self.countG, "T": self.countT}
        self.dictionary = dictionary
        return dictionary

    def reverseDna(self):
        lastForm = ""
        counter = 0
        dnaReformat = self.dnaString
        while len(dnaReformat) > len(lastForm):
            if dnaReformat[counter] == "A":
                str(dnaReformat).replace("A", "X")
                lastForm += "T"
            elif dnaReformat[counter] == "T":
                str(dnaReformat).replace("T", "X")
                lastForm += "A"
            elif dnaReformat[counter] == "G":
                str(dnaReformat).replace("G", "X")
                lastForm += "C"
            elif dnaReformat[counter] == "C":
                str(dnaReformat).replace("C", "X")
                lastForm += "G"
            counter += 1
        self.lastform = lastForm
        print(lastForm)

    def calculateComplement(self):
        print("re")


FirstDna = Dna("ATGCCG")
FirstDna.reverseDna()

