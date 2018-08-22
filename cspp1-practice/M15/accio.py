class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        return self.incantation


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    # def __str__(self):
    #     return self.name + " " + self.incantation
    def getDescription(self):
        return "This charm summons an object to the caster, potentially over a significant distance. "

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    return spell

def main():
    spell = Accio()
    spell.execute()
    studySpell(spell)
    print(studySpell(Accio()))

if __name__ == "__main__":
    main()