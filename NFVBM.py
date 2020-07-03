def P_Contrastive_Divergence(Data, theta_0, k, iterations, beta):
    """
    Persisten Contrastive Divergence (CD-k) alorithm for binary FVBM
    with N nodes. N is defined by the input Data.

    Parameters:
    Data: matrix of M datapoints. Shape: NxM
    k: The number of steps that the MCMC chain will take
    iterations: number of times the update equation is applied
    beta, J, h : additional parameters

    Returns:
    theta: sequence of parameters theta_i for i = 1, ..., iteration
    generated by the persistent CD algorithm
    """
    NN = len(theta_0)
    N = Data.shape[0]
    M = Data.shape[1]
    theta = np.zeros((NN,iterations))
    theta[:,0] = theta_0
    M_subset = int(M/10)
    Data_sample = np.zeros((N, M_subset))
    D1 = np.zeros((N, M_subset))

    D2 = Data.copy()

    for i in range(1,iterations):

        res_2 = np.zeros(NN)
        res_1 = np.zeros(NN)

        k_Ms = 0
        for j in np.random.choice(M, M_subset, replace = False):
            D2[:, j] = MCMC_sample(sigma = D2[:,j],
                                   W = createW(theta[:,i-1], N),
                                   beta = beta, iterations = k)
            Data_sample[:, k_Ms] = D2[:, j]
            D1[:,k_Ms] = Data[:,j]
            k_Ms = k_Ms + 1

        k_N = 0
        for ii in range(N):
            for jj in range(ii + 1, N):
                res_2[k_N] = Data_sample[ii, :].
                dot(np.transpose(Data_sample[jj, :]))
                res_1[k_N] = D1[ii, :].dot(np.transpose(D1[jj, :]))
                k_N = k_N + 1

        theta[:, i] = theta[:,i-1] + 0.2*((1/M_subset)*beta*res_1 -
                                          (1/M_subset)*beta*res_2)
    return(theta)
