# FatmanEvolutionaryModel

Outputs graphs (in the gml format), each describing an intermediate state in the model.
Done as a part of the NPTEL Social Networks course https://nptel.ac.in/courses/106/106/106106169/

# Fatman Hypothesis :
- If a person's friend is obese, then s/he is likely to become obese too.

# What is an Evolutionary Model ?
- An evolutionary model is a model that evolves with time.
- A network model is evolutionary if new edges are formed with time and some previous edges get removed from the network.

# Description of the model
- There is a a society consisting of 100 members of different kinds, different in terms of their body weight and hence their BMI value.
- The range of BMI values is [15,40].
- The usually acceptable BMI range is 18-25; any value less than 18 is considered as underweight and any value greater than 25 is taken as overweight
- We have 5 social foci in discussion, i.e. Eatout, Gym, Movie Club, Karate club, and Yoga Club.
- People having comparable BMI will become friends with each other. (Homophily)
- People having a common friend will become friends with each other. (Triadic Closure)
- People who are members of the same social foci will become friends with each other. (Foci closure)
- If one of the two friends is a member of a particular social foci, then the other one will also become a member of that social foci. (Membership closure)

# Assumptions made
- In the beginning of the evolution process, each citizen is a member of exactly one social foci.
- Only two (Eatout and Gym) out of five social focus will participate initially.
- Though new edges can form between nodes (as a result of homophily, closures, etc), but none of the edges can be deleted.

# Visualization reference
- The social foci nodes are red colored.
- The person nodes are blue colored.
- The obese people nodes are yellow colored.
- The underweight people nodes are green colored.
- Size of each person node is directly proportional to its BMI value.
