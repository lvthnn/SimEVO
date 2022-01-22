# SimEVO project

## Revisions of NN and movement/scanning

Currently we are using scanset grid for input mapping into NN. We might consider optimizing this and make it more closely reflect sensory inputs of biological organisms by dividing the organism's FOV into $x$ zones. A single corresponding input corresponds to **a)** organism, **b)** food, **c)** empty. We could design algorithmic expression that returns a higher value if individual / food is closer in particular zone compared to another one.

This does not implicate in which direction the individual must move in but indicates which zone is "most abundant in food".

![image](https://user-images.githubusercontent.com/63433562/150600593-c5def542-8c97-4253-b650-8e93e3f489a2.png)

Use raycasting for sensory mapping. Each individual raycasts in a conical area $A$ with radius $r$. When a collision is detected it registers the object type (individual or food) and feeds it into the NN. The behavioural networks outputs polar coordinate $O = (\Delta v, \Delta \theta)$ which represents change in velocity and change in forward facing angle. Implementing raycasting will be much faster as it replaces the need to iterate over and update an entity field to compare $(x,y)$ coordinates for confirming scan identity.

![image-20220122031745310](https://user-images.githubusercontent.com/63433562/150623119-4879b45b-1156-445e-a201-f2dd99fc0f67.png)

The conic area $A$ which organisms use to map their surroundings and feed into the network has the span $S_\theta = \theta_{\text{max}} - \theta_{\text{min}} = x \text{\: rad}$. The visual field resolution is defined by the integer $j$ which divides $A$ into subsections $A_1, \ldots, A_j$ with corresponding radians on the conic arch, $\theta_1, \ldots, \theta_j$. As $j \to \infty$, we gain higher degrees of movement and more sensory mapping capability.

Divide environment into chunks to allow for localization and easier input mapping.
