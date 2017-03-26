class Armed_Forces:

    def __init__(self, pilot, grunt, programmer, amphib):
        self.pilot = pilot
        self.grunt = grunt
        self.programmer = programmer
        self.amphib = amphib

navy = Armed_Forces("marcus", "kalu", "kade", "paul")

class Company:

    def __init__(self, tech, business, law, human_services):
        self.tech = tech
        self.business = business
        self.law = law
        self.human_services = human_services

looklive = Company("DeepNet", "BizDev", "The6", "TheSofties")

print looklive.tech
