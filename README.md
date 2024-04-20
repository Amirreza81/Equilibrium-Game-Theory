# Equilibrium-Game-Theory
Correlated Equilibrium and Mixed Nash Equilibrium with python

## Mixed Nash Equilibrium 

You can see the statements of this question [here](Amirreza81/Equilibrium-Game-Theory/Mixed-Nash-Equilibrium/Nash_Equilibrium.pdf).

I tried to find the mixed nash equilibrium with simplex algorithm. <br _>

I applied two different kind of LP for this question. 
> [First Version](Amirreza81/Equilibrium-Game-Theory/Mixed-Nash-Equilibrium/Nash_Equilibrium_v1.py) <br _>
> [Second Version](Amirreza81/Equilibrium-Game-Theory/Mixed-Nash-Equilibrium/Mixed-Nash-Equilibrium.py)

Second one is an easier implementation using M + N variables. You can see more details [here]([Amirreza81/Equilibrium-Game-Theory/Mixed-Nash-Equilibrium/LP.png](https://github.com/Amirreza81/Equilibrium-Game-Theory/blob/main/Mixed-Nash-Equilibrium/LP.png)).

<br _>

### An example:
<br _>

**Input:**

```
3 2
8 -5
-3 4
-5 -4
8 9
1 -2
8 5
```

**Output:**

```
0.750000 0.250000 0.000000 
0.450000 0.550000
```

Suppose two players wants to play a game. in this example, player 1 has 3 actions and player2 has 2 actions. After N lines we get 
the utilities of player1 and after N lines we get utilities of player2. The table of utilities is equal to:

```
(8, 8)  | (-5, 9)
------------------
(-3, 1) | (4, -2)
------------------
(-5, 8) | (-4, 5)
```

The *mixed nash eqilibrium* here shows the strategy of each player:

```
player1 -> (0.75, 0.25, 0)
player2 -> (0.45, 0.55)
```


## Q2 - Correlated Equilibrium

You can see the statements of this question [here](https://github.com/Amirreza81/Equilibrium-Game-Theory/blob/main/Correlated%20Equilibrium/Correlated_Equilibrium.pdf).<br _>

I tried to find the correlated equilibrium with simplex algorithm. <br _>
For finding correlated equilibrium, you should check this constraint and with solving the LP, you will find the answer.
```math
\sum_(\bar{s} \in S_(-P)) u_(i, \bar{s})^P x__(i, \bar{s})
```










