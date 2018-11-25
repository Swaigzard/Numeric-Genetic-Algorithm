import random
import numpy        # For graphing purposes

class Genetic_Algorithm:

    def __init__(self):
        """ Parameters """

        self.POPCAP = int(input('(100 suggested)Population Limit? '))        # Upper limit of population size
        # Suggested 100 because of space complexity, but this does allow outliers to skew the avg
        self.GENCAP = int(input('(1,000 suggested)Generation Limit? '))        # Upper limit of generations
        # Suggested 1000 because of big O complexity
        
        self.GenCounter = 0         # Keeps count of current generation
        self.population = {}        # The population dictionary
        self.DiverseCounter = 0     # For the DiverseChecker function
        self.Diversity = []         # ^^^
        self.AvgFitness = []        # For the AverageFitness function
        self.GenCounterList = []    # For graphing anything relative to amount of generations
        self.BestFit = []           # For BestFitness function
        self.MurderList = []        # For the Murder function
        self.ParentA = 0            # For the Crossover function
        self.ParentB = 0            # ^^^
        self.Terminate = False      # Used to enforce end cases of the algorithm
        self.Simulator = []         # For integration with the simulator
        self.SimulatorCounter = 0   # ^^^
        

    def Evolve(self):
        """ Calls all the functions that cause the evolution """

        self.PopulationInit()        
        
        for i in range(0,self.GENCAP,1):
            if self.Terminate == False:
                self.GenCounter = self.GenCounter + 1
                self.FitnessCheck()
                self.Murder()
                self.CrossOver()
                    
        if self.Terminate == True:  # If the TARGETNUMBER has been evolved
            print(TARGETNUMBER,'has been evolved, this took',self.GenCounter,'generation/s')

        if self.GenCounter == self.GENCAP and self.Terminate == False:
        # If the maximum amount of generations have occurred and TARGETNUMBER was not evolved
            print('in',self.GENCAP,'generations,',TARGETNUMBER,'was not evolved')

    def PopulationInit(self):
        """ Population Creation """

        PopInit = {}
        for i in range(0,self.POPCAP,1):    # Create a citizen until upper limit for population met
            PopInit[i] = random.randint(0,TARGETNUMBER * 2)
          
        self.population = {v:k for k,v in PopInit.items()}
        """
        This line swaps each value and key in the population because the population is
        origingally created with keys that are just consecutive integers and the x
        """

        self.DiverseChecker()


    def DiverseChecker(self):
        """
        A recursive function to ensure diversity within the population so that the dictionary
        doesn't break because when the keys and values are swapped around in the PopulationInit
        because swapping around keys and values risks duplicate keys that do not register as
        citizens of the population
        """

        self.DiverseCounter = self.POPCAP - len(self.population)
        # Checks how many new citizens need to be added

        if self.DiverseCounter == 0:    # If population doesn't need this function;return population
            return self.population

        else:
            for i in range(0,self.DiverseCounter,1):
            # Create a new random citizen per amount needed to meet upper limit of population
                self.population[random.randint(0,TARGETNUMBER * 2)] = 0
        self.DiverseChecker()        


    def FitnessCheck(self):
        """ Checks the fitness of each citizen """

        for key in self.population:  # Turns each value of each key into the fitness of that citizen
            self.population[key] = TARGETNUMBER - key   # Finds the difference/fitness of a citizen

        for key in self.population: # Iterates through each citizen checking if they're TARGETNUMBER
            if self.population[key] == 0:
                print('generation',self.GenCounter,'\n',self.population)
                self.Terminate = True

        

        if self.Terminate == False:
            print('generation',self.GenCounter,'\n',self.population)

        self.AverageFitness()
        self.BestFitness()
        

    def AverageFitness(self):
        """ Checks average fitness per generation for the graphing file """

        AverageCalc = []    # Temp list for storing fitness'
        TransitionList = []
        
        
        for key in self.population:     # Stores each fitness into AverageCalc
            AverageCalc.append(self.population[key])

        self.AvgFitness.append(numpy.mean(AverageCalc))
        # Appends the average value of every element in AverageCalc to self.AvgFitness

        for i in self.AvgFitness:   # Inits TransitionList to be abs(self.AvgFitness)
            TransitionList.append(abs(i))

        self.AvgFitness = TransitionList

        self.GenCounterList.append(self.GenCounter)
        # Stores a list of generations as long as self.AvgFitness

    def BestFitness(self):
        """ Finds the citizen with the greatest fitness per generation for graphing """

        FitnessHolder = []
        TransitionList = []

        for i in self.population:
            FitnessHolder.append(abs(self.population[i]))
            """
            Appends the absolute value of the fitness of each citizen fo FitnessHolder.
            The absolute value makes it easier to show which fitness is closest to zero because
            it allows for the use of the default min() function.
            """

        self.BestFit.append(min(i for i in FitnessHolder))
        # Appends closest value to zero to the BestFit list
        


    def Murder(self):
        """ Murders each citizen that isn't fit enough to survive """

        self.Parents = []   # Established here so that it is reset each generation
        SortedParents = []
        
        for k in self.population:   # Adds each fitness to a new list
            self.Parents.append(self.population[k])
            
        SortedParents = sorted(self.Parents,reverse = False) # Sorts the parents into ascending order

        for i in range(0,self.POPCAP//2,1):
            
            pass
        
        
        """
        Each for loop kills a quarter of the parents. It does this by iterating through a quarter
        of it's least fit parents. The parent with the greatest negative fitness are killed
        in the first for loop, and then the parents with the greatest positive fitness are killed.
        By doing this to the Parents list, the population can be iterated and recreated using
        citizens with fitness' that match with the parents.
        """
        for i in range(0,self.POPCAP//4,1):
            del SortedParents[0]
        for i in range(0,self.POPCAP//4,1):
            del SortedParents[(len(SortedParents)-1)]

        TempPop = {}
        for i in SortedParents:         # For each guarenteed parent
            for j in self.population:   # Check it against a current population member
                if i == self.population[j]: # If parent still present in the population maintain it
                    TempPop[j] = i

        self.population = TempPop

        # Replaces the population with the temporary population that consists of only parents    

    def CrossOver(self):
        """ Gets the parents to generate the next generation """

        for i in range(len(self.population),self.POPCAP - 1, 1):
            self.ParentA = random.choice(list(self.population.items()))
            # Obtains a random parent from the population dictionary and converts to a tuple

            self.ParentA = self.Parent(self.ParentA)
            # Converts the tuple from above into a singular integer

            self.ParentB = random.choice(list(self.population.items()))
            self.ParentB = self.Parent(self.ParentB)

            """
            These if statements all create the children of the next generation from the parents.
            Each if statement creates the child with a different range so that the random.randint()
            function does not break
            """
            if self.ParentA > self.ParentB:
                child = random.randint(self.ParentB,self.ParentA)
            elif self.ParentA < self.ParentB:
                child = random.randint(self.ParentA,self.ParentB)
            elif self.ParentA == self.ParentB:
                child = self.ParentA
            self.population[child] = 0

        self.DiverseChecker()   # Effectively a mutate function in this scenario


    def Parent(self,Parent):
        """
        Called when manipulating tuples to obtain only the first element of the tuple
        The second argument dictates which parent it is creating
        """

        TempParent = 0  # The returned variable
        TupleWorkAround = 0     # The counter that will combat tuple restrictions
        
        for i in Parent:    # For each value in the tuple
            TupleWorkAround = TupleWorkAround + 1
            if TupleWorkAround == 1:    # This if statement will return the first value of the tuple
                TempParent = i
            else:
                pass
        return TempParent



TARGETNUMBER = int(input('What number to evolve to? (can not be smaller than half of the populatioin limit) '))     # The target number to evolve towards


GA = Genetic_Algorithm()


GA.Evolve()











