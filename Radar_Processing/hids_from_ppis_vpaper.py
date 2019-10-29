# -*- coding: utf-8 -*-
"""
HYDROMETEOR CLASSIFICATION FROM POLARIMETRIC RADAR DATA (Paper Version)

- Reading radar files for specific cases, when hailfall occurred:
    - FCTH (S Band, Dual Pol)
        - corrected_reflectivity
        - cross_correlation_ratio
        - differential_reflectivity
        - specific_differential_phase
    - Cases:
    - 2017-03-14
    - 2017-11-15
- Processing data with CSU_RadarTools
- Classifying into 10 hydrometeor types (Drizzle, Rain, Ice Crystals,
    Aggregates, Wet/Melting Snow, Vertically Aligned Ice, Low-Density Graupel,
    High-Density Graupel, Hail and Big Drops)
- Calculating liquid and ice water mass
- Plotting data

Based on CSU_RadarTools Demonstration Notebook by Timothy Lang.

@author: Camila Lopes (camila.lopes@iag.usp.br)
"""

import radar_functions as rf
import custom_vars as cv
import custom_cbars


radar = rf.read_radar(cv.filename)
# radar = pyart.io.read_uf(cv.filename)
radar = rf.calculate_radar_hid(radar, cv.sounding_name, "S")
radar.fields['specific_differential_phase']['units'] = r'$\degree\  km^{-1}$'
radar.fields['differential_reflectivity']['units'] = 'dB'

name = 'FCTH'
level = 2

rf.plot_ppi_panel(
    radar, 'FH', level=level, fmin=0, fmax=10, cmap=cv.cmaphid,
    lat_index=cv.cs_lat, lon_index=cv.cs_lon,
    date=cv.date_name, name_multi=name,
    shp_name=cv.shp_path, hailpad_pos=cv.hailpad,
    zero_height=cv.zerodeg_height, minusforty_height=cv.fortydeg_height,
    grid_spc=cv.plotgrid_spc, xlim=cv.xlim, ylim=cv.ylim,
    save_path=cv.save_path, index="a", hailpad_cs_flag=cv.hail_flag,
    pt_br=cv.pt_br)

rf.plot_ppi_panel(
    radar, 'MW', level=level, fmin=0, fmax=10, cmap='mass',
    lat_index=cv.cs_lat, lon_index=cv.cs_lon,
    date=cv.date_name, name_multi=name,
    shp_name=cv.shp_path, hailpad_pos=cv.hailpad,
    zero_height=cv.zerodeg_height, grid_spc=cv.plotgrid_spc,
    xlim=cv.xlim, ylim=cv.ylim, save_path=cv.save_path, index="b",
    hailpad_cs_flag=cv.hail_flag, pt_br=cv.pt_br)

rf.plot_ppi_panel(
    radar, 'MI', level=level, fmin=0, fmax=30, cmap='mass',
    lat_index=cv.cs_lat, lon_index=cv.cs_lon,
    date=cv.date_name, name_multi=name,
    shp_name=cv.shp_path, hailpad_pos=cv.hailpad,
    zero_height=cv.zerodeg_height, grid_spc=cv.plotgrid_spc,
    xlim=cv.xlim, ylim=cv.ylim, save_path=cv.save_path, index="c",
    hailpad_cs_flag=cv.hail_flag, pt_br=cv.pt_br)

rf.plot_ppi_panel(
    radar, 'corrected_reflectivity', level=level, fmin=0, fmax=70, cmap='dbz',
    lat_index=cv.cs_lat, lon_index=cv.cs_lon,
    date=cv.date_name, name_multi=name,
    shp_name=cv.shp_path, hailpad_pos=cv.hailpad,
    zero_height=cv.zerodeg_height, grid_spc=cv.plotgrid_spc,
    xlim=cv.xlim, ylim=cv.ylim, save_path=cv.save_path, index="a",
    hailpad_cs_flag=cv.hail_flag, pt_br=cv.pt_br)

rf.plot_ppi_panel(
    radar, 'differential_reflectivity', level=level, fmin=-2, fmax=4,
    cmap='zdr', lat_index=cv.cs_lat, lon_index=cv.cs_lon,
    date=cv.date_name, name_multi=name,
    shp_name=cv.shp_path, hailpad_pos=cv.hailpad,
    zero_height=cv.zerodeg_height, grid_spc=cv.plotgrid_spc,
    xlim=cv.xlim, ylim=cv.ylim, save_path=cv.save_path, index="b",
    hailpad_cs_flag=cv.hail_flag, pt_br=cv.pt_br)

rf.plot_ppi_panel(
    radar, 'specific_differential_phase', level=level, fmin=-2, fmax=3.2,
    cmap='kdp', lat_index=cv.cs_lat, lon_index=cv.cs_lon,
    date=cv.date_name, name_multi=name,
    shp_name=cv.shp_path, hailpad_pos=cv.hailpad,
    zero_height=cv.zerodeg_height, grid_spc=cv.plotgrid_spc,
    xlim=cv.xlim, ylim=cv.ylim, save_path=cv.save_path, index="c",
    hailpad_cs_flag=cv.hail_flag, pt_br=cv.pt_br)

rf.plot_ppi_panel(
    radar, 'cross_correlation_ratio', level=level, fmin=0.8, fmax=1.013,
    cmap='rho', lat_index=cv.cs_lat, lon_index=cv.cs_lon,
    date=cv.date_name, name_multi=name,
    shp_name=cv.shp_path, hailpad_pos=cv.hailpad,
    zero_height=cv.zerodeg_height, grid_spc=cv.plotgrid_spc,
    xlim=cv.xlim, ylim=cv.ylim, save_path=cv.save_path, index="d",
    hailpad_cs_flag=cv.hail_flag, pt_br=cv.pt_br)
