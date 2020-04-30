# -*- coding:utf-8 -*-
from collections import deque  # 队列
import random
import numpy as np
import itertools
import copy


class ReservoirBuffer():

    def __init__(self, buffer_size, random_seed=123):
        """
        The right side of the deque contains the most recent experiences
        """
        self.buffer_size = buffer_size
        self.count = 0
        self.buffer = deque()
        random.seed(random_seed)
        self.last_recent_batch = 0

    # 保存监督学习数据
    def add(self, s, a, env):
        s_ = copy.deepcopy(np.reshape(s, (1, env.state_space)))
        a_ = copy.deepcopy(np.reshape(a, (1, env.total_action_space)))
        experience = (s_, a_)
        if self.count < self.buffer_size:
            self.buffer.append(experience)
            self.count += 1
        else:
            j = random.randrange(1, self.buffer_size + 1)
            if j < self.buffer_size:
                self.buffer[j] = experience

    def size(self):
        return self.count

    def sample_batch(self, batch_size):
        batch = []
        if self.count < batch_size:
            batch = random.sample(self.buffer, self.count)
        else:
            batch = random.sample(self.buffer, batch_size)

        s_batch = np.array([_[0] for _ in batch])
        a_batch = np.array([_[1] for _ in batch])

        return s_batch, a_batch

    def reservoir_sample(self, batch_size):
        batch = list(itertools.islice(self.buffer, 0, batch_size))
        if self.count > batch_size:
            for i in range(batch_size, (len(self.buffer) - 1)):
                j = random.randrange(1, i + 1)
                if j < batch_size:
                    batch[j] = self.buffer[i]

        s_batch = np.array([_[0] for _ in batch])
        a_batch = np.array([_[1] for _ in batch])

        return s_batch, a_batch
