from .utilities.sextractor import SEX_TOPHAT_FILTER, SEX_DEFAULT_STARNNW

# Keys are the FILTER NAMES at the original fits.

# EFF is the same as the pivot
WAVE_EFF = {
    'U': 3563.0,
    'F378': 3770.0,
    'F395': 3940.0,
    'F410': 4094.0,
    'F430': 4292.0,
    'G': 4751.0,
    'F515': 5133.0,
    'R': 6258.0,
    'F660': 6614.0,
    'I': 7690.0,
    'F861': 8611.0,
    'Z': 8831.0,
}

EXPTIMES = {
    'F378': 660, 'F395': 354, 'F410': 177, 'F430': 171,  
    'F515': 183, 'F660': 870, 'F861': 240,
    'U': 681, 'G': 99, 'R': 120, 'I': 138, 'Z': 168,
}

FILTER_NAMES_ZP_TABLE = {
    'F378': 'J0378', 'F395': 'J0395', 'F410': 'J0410', 'F430': 'J0430',
    'F515': 'J0515', 'F660': 'J0660', 'F861': 'J0861', 
    'U': 'u', 'G': 'g', 'R': 'r', 'I': 'i', 'Z': 'z',
}

FILTER_NAMES = {
    'F378': 'J0378', 'F395': 'J0395', 'F410': 'J0410', 'F430': 'J0430',
    'F515': 'J0515', 'F660': 'J0660', 'F861': 'J0861', 
    'U': 'uJAVA', 'G': 'gSDSS', 'R': 'rSDSS', 'I': 'iSDSS', 'Z': 'zSDSS',
}

SPLUS_DEFAULT_SEXTRACTOR_CONFIG = {
    'FILTER_NAME': SEX_TOPHAT_FILTER,
    'STARNNW_NAME': SEX_DEFAULT_STARNNW,
    'DETECT_TYPE': 'CCD',
    'DETECT_MINAREA': 4,
    'ANALYSIS_THRESH': 3.0,
    'FILTER': 'Y',
    'DEBLEND_NTHRESH': 64,
    'DEBLEND_MINCONT': 0.0002,
    'CLEAN': 'Y',
    'CLEAN_PARAM': 1.0,
    'MASK_TYPE': 'CORRECT',
    'PHOT_APERTURES': 5.45454545,
    'PHOT_AUTOPARAMS': '3.0,1.82',
    'PHOT_PETROPARAMS': '2.0,2.73',
    'PHOT_FLUXFRAC': '0.2,0.5,0.7,0.9',
    'MAG_ZEROPOINT': 20,
    'MAG_GAMMA': 4.0,
    'PIXEL_SCALE': 0.55,
    'BACK_FILTERSIZE': 7,
    'BACKPHOTO_TYPE': 'LOCAL',
    'BACKPHOTO_THICK': 48,
    'CHECKIMAGE_TYPE': 'SEGMENTATION',
}

SPLUS_DEFAULT_SEXTRACTOR_PARAMS = [
    'NUMBER', 'X_IMAGE', 'Y_IMAGE', 'KRON_RADIUS', 'ELLIPTICITY', 'THETA_IMAGE', 
    'A_IMAGE', 'B_IMAGE', 'MAG_AUTO', 'FWHM_IMAGE', 'CLASS_STAR'
]

#iDR4_FORNAX_RUN_7_106_Fornax_SPLUS-s28s33.00025, HYDRA_FULL+SPLUS-n17s10.00020, SPLUS-n16s09.00003
