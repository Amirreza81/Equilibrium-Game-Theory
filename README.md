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

Suppose two players wants to play a game. In this example, player 1 has 3 actions and player2 has 2 actions. After N lines we get 
the utilities of player1 and after N lines we get utilities of player2. The table of utilities is equal to:

```
(8, 8)  | (-5, 9)
-----------------
(-3, 1) | (4, -2)
-----------------
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
\sum_{{\bar{s}}\; \in \; S_{-p}} u_{i, {\bar{s}}}^p \; x_{i,\; {\bar{s}}} \geq \sum_{{\bar{s}}\; \in \; S_{-p}} u_{j,\; {\bar{s}}}^p \; x_{i,\; {\bar{s}}},\;\; \forall \; p \; and \; \forall \; i,j\; \in S_{p}
```

### An example:

**Input:**

```
1 1
3 3
6 6 -2 0 0 7
2 2 2 2 0 0
0 0 0 0 3 3
```

**Output:**

```
8.000000
0.500000 0.000000 0.000000 
0.250000 0.250000 0.000000 
0.000000 0.000000 0.000000
```

Suppose two players wants to play a game. In this example, player 1 has 3 actions and player2 has 3 actions. We should find the probability of playing each strategy profile and maximum optimal social benefit. For this example, the table of utilities is:

```
(6, 6) |  (-2, 0) | (0, 7)
--------------------------
(2, 2) |  (2, 2)  | (0, 0)
--------------------------
(0, 0) |  (0, 0)  | (3, 3)
```

After solving LP, for finding maximum optimal social benefit we have:

```
0.5 * (6 + 6) + 0.25 * (2 + 2) + 0.25 * (2 + 2) = 8
```

For more questions or any problem, feel free to contact with [me](amirrezaazari1381@gmail.com).





