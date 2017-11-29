from multiprocessing import Pool
from h5py import File

def chi2_kernel(data):
    H0, OmegaM = data

    chi = chi_2(H0, OmegaM)

    return chi

def parallel_chi2(kernel, data_array, processes=None):
    """
    Evaluates the chi2 function over the data saved in 'data_array'
    and distributes the workload among several independent python
    processes.
    """

    # Let's create a pool of processes to execute calculate chi2 in
    # parallel.

    
    with Pool(processes=processes) as pool:
        # The data accepted by the map method must be an iterable, like
        # a list, a tuple or a numpy array. The function is applied over
        # each element of the iterable. The result is another list with
        # the values returned by the function after being evaluated.
        #
        # [a, b, c, ...]  -> [f(a), f(b), f(c), ...]
        #
        # Here we use the imap method, so we need to create a list to
        # gather the results.
        results = []
        pool_imap = pool.imap(kernel, data_array)
        
        for result in pool_imap:
            results.append(result)
            
    return np.array(results)

# Reference: arXiv:1306.0573


def exec_chi2():
    
    points = 200 
    m_params = 2
    
    H0_range = np.linspace(50, 100, points)
    OmegaMatter_range = np.linspace(0.1, 0.6, points)

    #this will create the coordinate axis for the array
    H, OM = meshgrid(H0_range, OmegaMatter_range, indexing='ij')

    #and we use them to create our grid
    grid_data = stack((H,OM), axis=-1)

    # Flatten array
    
    flattened_grid = grid_data.reshape(points * points, m_params)
    
    # Execute parallel routine
    chi2_data = parallel_chi2(chi2_kernel, flattened_grid)

    # Reshape chi2 results with a similar shape as the original
    # data_grid, but with only one element.¡: the chi squared.
    
    chi2_data = chi2_data.reshape(points, points, 1)
    
    #################
    # Save data to file
    
    filename = 'H0-OmegaM_grid.h5'
    
    with File(filename, 'w') as file:
        # Add data
        file['/DataGrid'] = grid_data
        file['/Chi2'] = chi2_data
        # Save data to file
        file.flush()

    print(chi2_data.shape)


    if __name__ == '__main__':
    exec_chi2()
