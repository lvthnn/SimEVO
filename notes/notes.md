# SimEVO notes
## 21. Jan 2022
### Scanset

If $N \times N$ 

### Revision of NN

Currently we are using scanset grid for input mapping into NN. We might consider optimizing this and make it more closely reflect sensory inputs of biological organisms by dividing the organism's FOV into $x$ zones. A single corresponding input corresponds to **a)** organism, **b)** food, **c)** empty. We could design algorithmic expression that returns a higher value if individual / food is closer in particular zone compared to another one.

This does not implicate in which direction the individual must move in but indicates which zone is "most abundant in food"

![image](https://user-images.githubusercontent.com/63433562/150600593-c5def542-8c97-4253-b650-8e93e3f489a2.png)
