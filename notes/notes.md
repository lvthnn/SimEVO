<<<<<<< Updated upstream
# SimEVO project

## Revisions of NN and movement/scanning

Currently we are using scanset grid for input mapping into NN. We might consider optimizing this and make it more closely reflect sensory inputs of biological organisms by dividing the organism's FOV into $x$ zones. A single corresponding input corresponds to **a)** organism, **b)** food, **c)** empty. We could design algorithmic expression that returns a higher value if individual / food is closer in particular zone compared to another one.

This does not implicate in which direction the individual must move in but indicates which zone is "most abundant in food".

![image](https://user-images.githubusercontent.com/63433562/150600593-c5def542-8c97-4253-b650-8e93e3f489a2.png)

Use raycasting for sensory mapping. Each individual raycasts in a conical area $A$ with radius $r$. When a collision is detected it registers the object type (individual or food) and feeds it into the NN. The behavioural networks outputs polar coordinate $O = (\Delta v, \Delta \theta)$ which represents change in velocity and change in forward facing angle. Implementing raycasting will be much faster as it replaces the need to iterate over and update an entity field to compare $(x,y)$ coordinates for confirming scan identity.

![image-20220122031745310](https://user-images.githubusercontent.com/63433562/150623119-4879b45b-1156-445e-a201-f2dd99fc0f67.png)

The conic area $A$ which organisms use to map their surroundings and feed into the network has the span $S_\theta = \theta_{\text{max}} - \theta_{\text{min}} = x \text{\: rad}$. The visual field resolution is defined by the integer $j$ which divides $A$ into subsections $A_1, \ldots, A_j$ with corresponding radians on the conic arch, $\theta_1, \ldots, \theta_j$. As $j \to \infty$, we gain higher degrees of movement and more sensory mapping capability at the expense of performance.

Divide environment into chunks to allow for localization and easier input mapping.

## 10.04.2022

### Chunks

Let $S$ be the radian of the organism FOV and $C$ be any given chunk within the environment. The subset $O$ (outside) of $C$ is the set where any section of the organisms FOV lands outside the chunk and $I$ (inside) is the subset where an organism's entire FOV is contained within the chunk no matter its orientation.
$$
\mathbb P(O) = \frac{\textsf{area}(O)}{\textsf{area}(O) + \textsf{area}(I)}
$$
**Challenge.** Find chunk size that minimizes the probability of organisms FOV landing outside of chunk. Requires that we determine regions $O$ and $I$.

### Raycasting



Have $d \in [0;1]$. When the food or the entity is just at the limit of the FOV, its value of $d$ is $0$. Let $d_m$ be the maximum distance of an entity 

# Notes on meeting 11. april

## Raycasting and sensory mapping

Ideally, inputs into the behavioural network of an organism is between 0 and 1. The sensory map needs to include entity type and distance from the organism. We denote the distance using $d$ as it is relevant in the following passage.

The maximum distance $d_M$ an entity can be from the organism equals the length of the radius of the sector which forms the organism's field of view. Let $E$ be some entity present in the organism's field of view. Under the assumption that all entities within the environment are represented by circles, we denote the radius of entity $E$ as $r_E$. We have for a given ray $\rho_i \in [\rho_1, \ldots, \rho_n]$ that $E$ collides with the ray iff
$$
\textsf{dist}(E, \rho_i) \leq r_E
$$
where $\textsf{dist}(E, \rho_i)$ is the function which returns the distance between the point location $E = (x,y)$ and the line $\rho_i$.
=======
# SimEVO notes
## 21. Jan 2022
### Revisions of NN and movement/scanning

Currently we are using scanset grid for input mapping into NN. We might consider optimizing this and make it more closely reflect sensory inputs of biological organisms by dividing the organism's FOV into $x$ zones. A single corresponding input corresponds to **a)** organism, **b)** food. We could design an algorithmic expression that returns a higher value if individual / food is closer in particular zone compared to another one.

This does not implicate in which direction the individual must move in but indicates which zone is "most abundant in food".

![image](https://user-images.githubusercontent.com/63433562/150600593-c5def542-8c97-4253-b650-8e93e3f489a2.png)

Use raycasting for sensory mapping. Each individual raycasts in a conic area $A$, their field of view, when a collision is detected it registers the object type (individual or food) and feeds it into the NN. The behavioural networks outputs polar coordinate $O = (\Delta v, \Delta \theta)$ which represents change in velocity and change in forward facing angle.

Divide environment into chunks to allow for localization and easier input mapping.

![image](https://user-images.githubusercontent.com/63433562/150603542-8d6083df-910a-45e3-9456-7e2d689fdef8.png)
>>>>>>> Stashed changes
