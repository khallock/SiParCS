import xarray as xa
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import math
'''

Redo of "3D_plot_initial.py" to have structuring more appropriate for
GUI work.

A class for plotting 2D observation data from DART's obs_sequence_tool. 
Lifted variables names from read_obs_netcdf.m and plot_obs_netcdf.m.


Possible 1-off indexing issues. None obvious right now.

Also string format is weird in nCDF (b's before each entry in large string sets)

Also may have to fiddle with datatypes in initializing args, as well as make sure
inf is float('inf')

'''

class plot_2D_obs_initial:

    def __init__(self, file_path):
        
        self.dataset = xa.open_dataset(file_path)
  
        def bytes_to_string(self, bytes):
            return ''.join(bytes.decode('UTF-8').split())

        bytes_to_string = np.vectorize(bytes_to_string)
               
        self.obs_types = self.dataset['ObsTypes']
        #print(type(self.obs_types[0]))
        self.obs_type_strings = bytes_to_string(self, self.dataset['ObsTypesMetaData'].values)
        #print(type(self.obs_type_strings[0]))
        self.copy_strings = bytes_to_string(self, self.dataset['CopyMetaData'].values)
        #print(type(self.copy_strings[0]))
        self.QC_strings = bytes_to_string(self, self.dataset['QCMetaData'].values)
        #print(type(self.QC_strings[0]))
        
        self.time = self.dataset['time'] #may need to change these three lines to .values
        #print(type(self.time[0]))
        self.obs_type = self.dataset['obs_type']
        #print(type(self.obs_type[0]))
        self.obs_keys = self.dataset['obs_keys']
        #print(type(self.obs_keys[0]))
        self.vert_type = self.dataset['which_vert']
        #print(type(self.vert_type[0]))
        '''
        MISSING MISSING DATA ACCOUNTABILITY HERE
        '''
        self.location = self.dataset['location']
        #print(type(self.location[0]))
        self.obs = self.dataset['observations']
        print(self.obs.size)
        #print(type(self.obs[0]))
        self.QC = self.dataset['qc']
        #print(type(self.QC[0]))

        self.my_types = np.unique(self.obs_type.values)
        self.time_units = self.time.dtype
        self.time_range = self.time.attrs['valid_range']
        self.calendar = 'Gregorian' #don't know how to get other calendar types
        #missing some other time stuff

        #don't have the verbose section

        '''
        self.num_copies = self.dataset['copy'].size
        
        if copy_string.lower() == 'all':
            self.my_type_ind = [i for i in range(0,self.num_copies)]
        else:
            #get_copy_index.m
            copy_meta_data = self.dataset['CopyMetaData']
            meta_data_length  = self.dataset['nlines'].size
            copy_string_no_white = ''.join(self.copy_string.split())
            copy_index = -1

            #find matching copy
            for i in range(0, self.num_copies):
                meta_data_no_white = ''.join(bytes_to_string(self, copy_meta_data.values[i].split()))
                if meta_data_no_white == copy_string_no_white:
                    copy_index = i
                    break

            if copy_index < 0:
                raise Exception('No matching copy found')

            self.my_type_ind = copy_index
        '''
        
        self.obs_ind = 0


        #this may be incorrect. it will currently be an inds by my_type_ind array.
        #similar concerns for subsequent assignments
        #print(self.inds, self.obs_ind)
        self.my_obs = self.obs[:, self.obs_ind]
        print(self.my_obs.size)
        self.my_locs = self.location
        self.my_keys = self.obs_keys
        self.my_vert_types = self.vert_type
        self.my_times = self.time

        
        self.my_lons = self.my_locs[:, 0]
        self.my_lats = self.my_locs[:, 1]
        self.my_z = self.my_locs[:, 2]
        print('here')
        '''
        pd_array = pd.DataFrame({'obs' : self.my_obs.values,
                                 'keys' : self.my_keys.values,
                                 'lons' : self.my_lons.values,
                                 'lats' : self.my_lats.values,
                                 'z' : self.my_z.values,
                                 'times' : self.my_times.values})'''


        #index = pd.MultiIndex.from_tuples(tuples, names = ['times', 'lons', 'lats', 'z', 'obs', 'keys'])
        #print(index)
        index = pd.DataFrame
        ''''pd_array = pd.DataFrame({'obs' : self.my_obs.values,
                                 'keys' : self.my_keys.values,
                                 'lons' : self.my_lons.values,
                                 'lats' : self.my_lats.values,
                                 'z' : self.my_z.values,
                                 'times' : self.my_times.values})'''
        pd_array = pd.DataFrame({'obs' : self.my_obs.values,
                                 'lons' : self.my_lons.values,
                                 'lats' : self.my_lats.values})
        #pd_array.set_index(['times', 'lons', 'lats', 'z'], inplace = True)
        pd_array.set_index(['lons', 'lats'], inplace = True)
        pd_array.sort_index(inplace = True)
        #pd_array.unstack(level = -1)
        #print(pd_array.index)
        #print(pd_array)
        xa_array = xa.DataArray(pd_array)
        a = xa_array.where(xa_array.lats>80).values
        print(xa_array.where(xa_array.lats>80, drop = True).where
        b = xa_array.where(xa_array.lats > 80, drop = True)
        print(b.where(b.lons < 80, drop = True))
        #print(xa_array.
        #print(self.my_obs.expand_dims('lons', self.my_lons.values))
        #print(xa_array)
        #print('at unstack')
        #xa_array.unstack('dim_0')
        #print(xa_array)
        #print(xa_array[0])
        print('here')
        '''xa_set = xa.Dataset({'obs' : self.my_obs,
                                 'lons' : self.my_lons,
                                 'lats' : self.my_lats,
                                 'z' : self.my_z,
                                 'times' : self.my_times})'''
        print('here')
        #xa_array_grouped = xa_set.groupby('times')
        #pd_array_grouped = pd_array.groupby('times').groupby('lons')
        #print('here')
        #pd_array_final = pd_array_grouped
        #print(type(pd_array_final))
        #print(pd_array_final.groups)
        #print(np.array([self.my_times, [self.my_lons, [self.my_lats, [self.my_z, [self.my_obs, [self.my_keys]]]]]]))
        #print(xa.DataArray(pd_array_final))
        
        #self.data = xa.DataArray(self.my_obs, zip(
        

        #print(np.stack(np.array([self.lons, self.obs]), axis = 0).shape)
        #self.data=np.array([self.lats, self.lons, self.z, self.time, self.]).transpose()
        #self.data = np.array([self.my_times, self.my_lons, self.my_lats, self.my_z, self.my_obs])

        quit()
        #print(np.unique(self.lons).size, np.unique(self.lats).size, np.unique(self.time).size, np.unique(self.z).size, np.unique(self.obs).size)
        #print(self.data.shape)
        
        #print(self.obs.shape, self.lons.shape, self.lats.shape, self.z.shape, self.keys.shape, self.time.shape)
        #print(self.lons.flatten().shape, self.lats.flatten(), self.z.flatten(), self.keys.flatten(), self.time.flatten())
        #Create an xarray DataArray to hold everything. Will need to account for multiple ob types later
        #by instead making a Dataset

        self.data = xa.DataArray(self.obs, coords =
                                 {'lon': self.lons, 'lat': self.lats, 'vert': self.z,
                                   'key' : self.keys, 'time': self.time})
                                 #attrs = {'vert_units': self.vert_units,'vert_pos_dir' : self.vert_pos_dir}) 
                                                     
        
    def plot(self):
        p = None
        
        ''' obs_type_string, region, copy_string, QC_string, max_QC
        self.region = np.array(region) #e.g. [0, 360, -90, 90, -inf, inf] or [0, 360, -90, 90]
        
        'RADIOSONDE_TEMPERATURE',
                  [0, 360, -90, 90, -float('inf'), float('inf')], 'observation', '', 2, 1)

        if copy_string.lower() == 'all':
            self.copy_string = self.dataset['CopyMetaData'].values
        else:
            self.copy_string = copy_string
            
        self.QC_string = QC_string #e.g. 'DART quality control'
        self.max_QC = max_QC #e.g. 2
        self.verbose = verbose #True or False

        self.obs_type_string = obs_type_string #e.g. 'RADIOSONDE_U_WIND_COMPONENT', 'ALL'

        #find observations of the correct type
        if obs_type_string.lower() == 'all':
            self.inds = [i for i in range(0,self.obs.size)]

        else:
            self.my_ind_array = np.where(self.obs_type_strings == self.obs_type_string)[0]
            #print(self.obs_type_strings[0])
            #print(self.obs_type_string)
            #print(self.my_ind_array)
            if self.my_ind_array.size > 0:
                self.my_ind = self.my_ind_array[0] + 1 #first instance of my_ind
                self.inds = np.where(self.obs_type.values == self.my_ind)[0] #all instances of associated type

            else:
                print('FYI - no {} observations \n'.format(self.obs_type_string))
                self.inds = np.array([])


        self.my_obs = self.obs[self.inds, self.obs_ind].values

        self.my_locs = self.location[self.inds].value
        self.my_keys = self.obs_keys[self.inds].values
        self.my_vert_types = self.vert_type[self.inds].values
        self.my_times = self.time[self.inds].values

        #find QC values for obs

        if self.QC_string != '':
            #get_qc_index.m
            QC_meta_data = self.dataset['QCMetaData']
            #an issue is pointed out in matlab code where order of this array changes
            #based on number of copies
            num_QC_copies = self.dataset['qc_copy'].size
            copy_string_no_white = ''.join(self.QC_string.split())
            copy_index = -1

            #find matching copy
            for i in range(0, self.num_QC_copies):
                meta_data_no_white = ''.join(str(QC_meta_data.values[i].split()))
                if meta_data_no_white == copy_string_no_white:
                    copy_index = i
                    break

            if copy_index < 0:
                raise Exception('No matching copy found')

            self.my_QC_ind = copy_index
            #may be an issue here, confused about QC structure
            self.my_QC = self.QC[self.inds, self.my_QC_ind].values
            
        else:
            self.my_QC = np.array([])



        
        #locations_in_region.m
        if self.region.size == 6:
            z_min = min(self.region[[4,5]])
            z_max = max(self.region[[4,5]])
            
        elif self.region.size < 4:
            raise Exception('Region msut be an array of length 4 or 6')

        else:
            z_min = float(-inf)
            z_max = float(inf)
        
        y_min = min(self.region[[2,3]])
        y_max = max(self.region[[2,3]])
        x_min = self.region[0]%360.0
        x_max = self.region[1]%360.0

        #may not be possible with numpy array, may need some numpy function
        lons = self.my_locs[:, 0]%360.0

        #Need to revise the above code to no longer be a logical (should be a way to do it as one where)
        
        


        #need to redo the following chunk to be similar to the commented chunk below (faster), but not sure how
        #would be more pythonic

        self.loc_inds = []
        if (x_min == x_max):
            for i in range(self.my_locs[:, 0].size):
                #print(i)
                cur_loc = self.my_locs[i]
                #print(i)
                if cur_loc[1] >= y_min and cur_loc[1] <= y_max and cur_loc[2] >= z_min and cur_loc[2] <= z_max:
                    self.loc_inds.append(i)
                    #print(self.loc_inds)
        elif (x_min > x_max):
            for i in range(self.my_locs[:, 0].size):
                cur_loc = self.my_locs[i]
                if ((cur_loc[0] >= x_min or cur_loc[0] <= x_max) and
                    cur_loc[1] >= y_min and cur_loc[1] <= y_max and
                    cur_loc[2] >= z_min and cur_loc[2] <= z_max):

                    self.loc_inds.append(i)
        else:
            for i in range(self.my_locs[:, 0].size):
                cur_loc = self.my_locs[i]
                if ((cur_loc[0] >= x_min and cur_loc[0] <= x_max) and
                    cur_loc[1] >= y_min and cur_loc[1] <= y_max and
                    cur_loc[2] >= z_min and cur_loc[2] <= z_max):

                    self.loc_inds.append(i)
        '''            
        '''
        print(np.where(np.bitwise_and(self.my_locs[:, 1] > -40, self.my_locs [:, 1] < 0,
                                      self.my_locs[:, 2] >= z_min, self.my_locs[:, 2] <= z_max))[0].size)
        '''
        '''
        for i in range(self.mylocs[:, 0].size):
            if (x_min == x_max):
                
        if (x_min == x_max):
            self.loc_inds = np.where(self.my_locs[:, 1] >= y_min and self.my_locs[:, 1] <= y_max and
                                     self.my_locs[:, 2] >= z_min and self.my_locs[:, 2] <= z_max)
        else:
            if (x_min > x_max):
                #this line does not follow the sames structure as in matlab, but seems likely to work
                self.loc_inds = np.where((self.my_locs[:, 0] >=x_min or self.my_locs[:, 0] <= x_max) and
                                         self.my_locs[:, 1] >= y_min and self.my_locs[:, 1] <= y_max and
                                         self.my_locs[:, 2] >= z_min and self.my_locs[:, 2] <= z_max)
            else:
                self.loc_inds = np.where((self.my_locs[:, 0] >=x_min and self.my_locs[:, 0] <= x_max) and
                                         self.my_locs[:, 1] >= y_min and self.my_locs[:, 1] <= y_max and
                                         self.my_locs[:, 2] >= z_min and self.my_locs[:, 2] <= z_max)        
        '''
        
        '''        
        print(self.my_locs[:, 0].size)
        print(self.my_locs[:, 0])
        print(np.where((self.my_locs[:, 1] >= y_min)) - (self.my_locs[:, 1] <= y_max).all().size)
        if (x_min == x_max):
            self.loc_inds = np.where(self.my_locs[:, 1] >= y_min and self.my_locs[:, 1] <= y_max and
                                     self.my_locs[:, 2] >= z_min and self.my_locs[:, 2] <= z_max)
        else:
            if (x_min > x_max):
                #this line does not follow the sames structure as in matlab, but seems likely to work
                self.loc_inds = np.where((self.my_locs[:, 0] >=x_min or self.my_locs[:, 0] <= x_max) and
                                         self.my_locs[:, 1] >= y_min and self.my_locs[:, 1] <= y_max and
                                         self.my_locs[:, 2] >= z_min and self.my_locs[:, 2] <= z_max)
            else:
                self.loc_inds = np.where((self.my_locs[:, 0] >=x_min and self.my_locs[:, 0] <= x_max) and
                                         self.my_locs[:, 1] >= y_min and self.my_locs[:, 1] <= y_max and
                                         self.my_locs[:, 2] >= z_min and self.my_locs[:, 2] <= z_max)
        '''

        '''
        self.loc_inds = np.array(self.loc_inds)
        self.num_obs = self.loc_inds.size
        self.lons = self.my_locs[self.loc_inds, 0]
        self.lats = self.my_locs[self.loc_inds, 1]
        self.z = self.my_locs[self.loc_inds, 2]
        self.obs = self.my_obs[self.loc_inds]
        self.vert_type = self.my_vert_types[self.loc_inds]
        self.keys = self.my_keys[self.loc_inds]
        self.time = self.my_times[self.loc_inds]

        
        if self.my_QC.size > 0:
            self.QC = self.my_QC[self.loc_inds]
        else:
            self.QC = np.array([])

        
        self.vert_types = np.unique(self.vert_type)
        self.num_vert_types = self.vert_types.size

        for vert_type in self.vert_types:
            print(vert_type)
            if vert_type == -2: #Undefined vertical units, but positive is up
                self.vert_pos_dir = 'up'
                self.vert_units = 'unknown'
            elif vert_type == -1: #Vertical units are surface
                self.vert_pos_dir = 'up'
                self.vert_units = 'surface'
            elif vert_type == 1: #Vertical units are level where 1 is uppermost
                self.vert_pos_dir = 'down'
                self.vert_units = 'model level'
            elif vert_type == 2: #Vertical units are pressure
                self.vert_pos_dir = 'down'
                self.vert_units = 'pressure'
            elif vert_type == 3: #Vertical units are heights
                self.vert_pos_dir = 'up'
                self.vert_units = 'height'

                ''' '''A WORLD OCEAN DATABASE CAVEAT THAT I HAVE NOT IMPLEMENTED''' '''

        #print(self.vert_pos_dir, self.vert_units)
        #print(self.z)

        '''
        
plotter = plot_2D_obs_initial('../obs_series/obs_epoch_001.nc')
                

#def __init__(self, file_path, obs_type_string, region, copy_string, QC_string, max_QC, verbose):   
