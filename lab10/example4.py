class Dna:
    def __init__(self, dnaString):
        self.dnaString = dnaString
        self.containList = [letter for letter in dnaString]

    def returner(self):
        return self.dnaString

    def countNucleotides(self):
        self.countA = self.containList.count("A")
        self.countC = self.containList.count("C")
        self.countG = self.containList.count("G")
        self.countT = self.containList.count("T")
        dictionary = {"A": self.countA, "C": self.countC, "G": self.countG, "T": self.countT}
        self.dictionary = dictionary
        return dictionary

    def calculateComplement(self):
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

    def Mutations(self, dna1: object, dna2: object) -> object:
        if isinstance(dna1, Dna) and isinstance(dna1, Dna):
            counter = 0
            difference = 0
            a = len(dna1.returner())
            dna1Str = dna1.returner()
            dna2Str = dna2.returner()
            while counter < a:
                if dna1Str[counter] != dna2Str[counter]:
                    difference += 1
                counter += 1
            return difference

    def FindMotif(self,dna1,dna2):
        self.dna1 = dna1
        self.dna2 = dna2
        print(self.dna1,self.dna2)
        location = 0
        finded = []
        while True:
            if str(self.dna1).count(str(self.dna2)) == 0:
                break
            elif str(self.dna1).find(str(self.dna2)):
                finded.append(str(self.dna1).find(str(self.dna2)))
                self.dna1 = str(self.dna1[str(self.dna1).find(str(self.dna2)):])
        return finded




e1 = Dna("ATAT")
e2 = Dna("GATATATGCATATACTT")
print(Dna.FindMotif(Dna, "GATATATGCATATACTT", "ATAT"))
