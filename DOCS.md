# SimEvo v1.0.0 documentation
This file includes information on the structure and functionality
of the SimEvo evolutionary simulation tool. For installation guides,
see the ```README.md``` file.

### Table of contents
- [Algorithm structure](#algorithm-structure)
    - [Individual based simulation](#individual-based-simulation)
    - [Populations](#populations)
    - [The environment](#the-environment)

## Algorithm structure
### Individual based simulation
Instead of using mathematical methods to determine changes in population metrics, the SimEvo algorithm functionality is based on individual-level metrics. Although this may be computationally unfavourable compared to the usage of population metrics. SimEvo ```v1.0.0```
only allows for one parameter to be configured, the ```fitness``` attribute (read more in the [Environmental checks](#environmental-checks) section).

**Individual parameters**
- ```max_age```: A global variable for all ```individal``` objects. The maximum lifespan in generations. When an individuals ```age``` exceeds that of ```max_age```, he dies and is removed from the population.
- ```offspring_num```: The number of offspring produced per reproduction.
- ```age```: An individual's age in generations.
### Populations
Populations can be viewed as sets of individuals, each with their corresponding individual attributes, such as fitness and age. However, a population has several parameters which it recieves as input at the start of simulations which are used to map the initial population:

**Population parameters**
- ```init_population_size```: Population size at start of simulation.
- ```genome_composition```: Percentage of indivudals within the population with a derivative genotype, resulting in abnormal offspring inheritance
- ```selection_ratio```: Per-turn percentage of population that is subjected to environmental check
- ```selection_method```: Which method to employ when selective population is formed; for example, ```strict(0.2)``` Selects the individuals in the lowest 20% of fitness distribution

**Population object**
- ```population```: List which contains population
- ```params```: Dictionary containing population parameters (see above)

**Functions**
- ```set_params()```: Initialize or modify population parameters. Saves input as ```params``` dictionary. To set parameters to their default value, pass ```"default"``` as the input value for the respective parameter.
- ```run(n)```: Runs the population for ```n``` generations. For non-specified values of ```n```, the algorithm advances one generation.
### The environment
**Selection**<br>
When an individual is exposed to an environmental check, his chances of survival are determined by a logical comparison between the environmental factor ```difficulty``` and the individual's ```fitness``` attribute. Thus, if ```difficulty > fitness```, the individual dies and is removed from the simulation. Else, he survives.

**Difficulty**<br>
The ```difficulty``` is a numeric variable which defines the difficulty of the environment relative to its population. If a checked individual's ```fitness``` attribute's numeric value is lower than that of the environmental difficulty, that individual dies.

**Population difficulty**<br>
The variable ```population_difficulty``` can be accessed by calling the ```calc_population_diff()``` function on the population object. This returns a double value equals to the ratio of individuals who suffice the condition $w_i < \mathscr E_d$ over the population size. The value of ```population_difficulty``` is hence between [0;1]. Higher values of this variable indicates lower degree of adaptation whereas lower values indicate higher degree of adaptation to the environment.