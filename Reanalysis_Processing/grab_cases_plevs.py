import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2016',
        'month': '12',
        'day': '23',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20161223.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2016',
        'month': '12',
        'day': '24',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20161224.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2016',
        'month': '12',
        'day': '25',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20161225.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '01',
        'day': '29',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20170129.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '01',
        'day': '30',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20170130.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '01',
        'day': '31',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20170131.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '03',
        'day': '12',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20170312.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '03',
        'day': '13',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20170313.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '03',
        'day': '14',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20170314.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '11',
        'day': '13',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20171113.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '11',
        'day': '14',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20171114.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '11',
        'day': '15',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20171115.nc')

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content',
            'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
            'vertical_velocity', 'vorticity'
        ],
        'pressure_level': [
            '10', '100', '250', '500', '700', '850', '925', '1000'
        ],
        'year': '2017',
        'month': '11',
        'day': '16',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00'
        ],
        'area': [30, -100, -70, 0],
        'grid': [0.25, 0.25],
    },
    '../Data/REANALYSIS/ERA5/era5_plevs_20171116.nc')
