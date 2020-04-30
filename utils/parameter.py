# -*- coding:utf-8 -*-

HiddenLayer = 64
LearningRateBR = 0.1
LearningRateAR = 0.005
Gamma = 0.96
Epsilon = 0.06
EpsilonDecay = 0.06
EpsilonMin = 0
MiniBatchSize = 16
Penalty = -1
Eta = 0.2
MRLSize = 200000
MSLSize = 500000
Omega = 0.003
TargetModelUpdateRate = 150


Decksize = 6
Playercount = 2
Choices = 4
MaxRounds = 2
Suits = 2
# has to be 3 because: maximal 0 to 2 raises
MaxRaises = 3
#ActionSpace is 2 -> folding is not encoded
ActionSpace = 2
TotalActionSpace = 3

Buffersize = 40000
Seed = 12

MaxEpisodes = 10000
Episodes = 5000
TestEpisodes = 100