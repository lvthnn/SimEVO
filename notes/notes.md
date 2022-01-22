# SimEVO notes
## 21. Jan 2022
### Revisions of NN and movement/scanning

Currently we are using scanset grid for input mapping into NN. We might consider optimizing this and make it more closely reflect sensory inputs of biological organisms by dividing the organism's FOV into $x$ zones. A single corresponding input corresponds to **a)** organism, **b)** food, **c)** empty. We could design algorithmic expression that returns a higher value if individual / food is closer in particular zone compared to another one.

This does not implicate in which direction the individual must move in but indicates which zone is "most abundant in food".

![image](https://user-images.githubusercontent.com/63433562/150600593-c5def542-8c97-4253-b650-8e93e3f489a2.png)

Use raycasting for sensory mapping. Each individual raycasts in an elliptical area $A$, when a collision is detected it registers the object type (individual or food) and feeds it into the NN. The behavioural networks outputs polar coordinate $O = (\Delta v, \Delta \theta)$ which represents change in velocity and change in forward facing angle.

![image](https://user-images.githubusercontent.com/63433562/150622902-aa2168c3-6421-4664-a242-8621c9a429c2.png)


Divide environment into chunks to allow for localization and easier input mapping.

