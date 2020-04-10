import numpy as np

def halving_algorithm(k=10,n=1000,variance=0.1): # k is number of arms, n is budget
    arm_means = [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0]
    rewards = arm_means.copy()
    L = np.ceil(np.log2(k))
    A = k
    index_list = [0,1,2,3,4,5,6,7,8,9]
    for l in range(int(L)):
        T = np.floor(n/(L*A))
        avg_rewards = np.zeros(int(A))
        for i in range(int(A)):
            arm_rewards = []
            for t in range(int(T)):
                Z = np.random.normal(loc=0,scale=np.sqrt(variance))
                reward = rewards[i]+Z
                arm_rewards.append(reward)

            avg_rewards[i] = np.mean(arm_rewards)

        A = np.ceil(A/2)
        indices = np.argpartition(avg_rewards, int(-A))[int(-A):]
        indices = [int(x) for x in indices]
        rewards = [rewards[g] for g in indices]


    return arm_means.index(rewards[0]) + 1


halving_algorithm()