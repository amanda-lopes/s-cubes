from os import getcwd

from . import __author__, __zp_cat__, __zpcorr_path__
from .utilities.sextractor import SEX_TOPHAT_FILTER, SEX_DEFAULT_STARNNW

MOTD_TOP = '┌─┐   ┌─┐┬ ┬┌┐ ┌─┐┌─┐ '
MOTD_MID = '└─┐───│  │ │├┴┐├┤ └─┐ '
MOTD_BOT = '└─┘   └─┘└─┘└─┘└─┘└─┘ '
MOTD_SEP = '----------------------'

SPLUS_PROG_DESC = f'''
{MOTD_TOP} | Create S-PLUS galaxies data cubes, a.k.a. S-CUBES. 
{MOTD_MID} | S-CUBES is an organized FITS file with data, errors, 
{MOTD_BOT} | mask and metadata about some galaxy present on any 
{MOTD_SEP} + S-PLUS observed tile. Any problem contact:

   {__author__}

'''

WAVE_EFF = {
    'U': 3536.0,
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

NAMES_CORRESPONDENT = {
    'F378': 'J0378', 'F395': 'J0395','F410': 'J0410', 'F430': 'J0430', 
    'F515': 'J0515', 'F660': 'J0660', 'F861': 'J0861', 
    'U': 'u', 'G': 'g', 'R': 'r', 'I': 'i', 'Z': 'z',
}

SPLUS_ARGS = {
    # optional arguments
    'redo': ['r', dict(action='store_true', default=False, help='Enable redo mode to overwrite final cubes.')],
    'clean': ['c', dict(action='store_true', default=False, help='Clean intermediate files after processing.')],
    'force': ['f', dict(action='store_true', default=False, help='Force overwrite of existing files.')],
    'bands': ['b', dict(default=list(WAVE_EFF.keys()), nargs='+', help='List of S-PLUS bands (space separated).')],
    'size': ['l', dict(default=500, type=int, help='Size of the cube in pixels.')],
    'angsize': ['a', dict(default=50, type=float, help="Galaxy's Angular size in arcsec.")],
    'work_dir': ['w', dict(default=getcwd(), help='Working directory.')],
    'output_dir': ['o', dict(default=getcwd(), help='Output directory.')],
    'sextractor': ['x', dict(default='sex', help='Path to SExtractor executable.')],
    'class_star': ['p', dict(default=0.25, type=float, help='SExtractor CLASS_STAR parameter for star/galaxy separation.')],
    'verbose': ['v', dict(action='count', default=0, help='Verbosity level.')],
    'debug': ['D', dict(action='store_true', default=False, help='Enable debug mode.')],
    'satur_level': ['S', dict(default=1600.0, type=float, help='Saturation level for the png images.')],
    'zpcorr_dir': ['Z', dict(default=__zpcorr_path__, help='Zero-point correction directory.')],
    'zp_table': ['z', dict(default=__zp_cat__, help='Zero-point table.')],
    'back_size': ['B', dict(default=64, type=int, help='Background mesh size for SExtractor.')],
    'detect_thresh': ['T', dict(default=1.1, type=float, help='Detection threshold for SExtractor.')],
    'username': ['U', dict(default=None, help='S-PLUS Cloud username.')],
    'password': ['P', dict(default=None, help='S-PLUS Cloud password.')],
    'mask_stars': ['M', dict(action='store_true', default=False, help='Run SExtractor to auto-identify stars on stamp.')],
    'det_img': ['I', dict(action='store_true', default=False, help='Downloads detection image for the stamp. Needed if --mask_stars is active.')],

    # positional arguments
    'tile': ['pos', dict(metavar='SPLUS_TILE', help='Name of the S-PLUS tile')],
    'ra': ['pos', dict(metavar='RA', help="Galaxy's right ascension")],
    'dec': ['pos', dict(metavar='DEC', help="Galaxy's declination")],
    'galaxy': ['pos', dict(metavar='GALAXY_NAME', help="Galaxy's name")],
    'specz': ['pos', dict(type=float, metavar='REDSHIFT', help='Spectroscopic or photometric redshift of the galaxy')],
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
    'NTHREADS': 2,
}

SPLUS_DEFAULT_SEXTRACTOR_PARAMS = [
    'NUMBER', 'X_IMAGE', 'Y_IMAGE', 'KRON_RADIUS', 'ELLIPTICITY', 'THETA_IMAGE', 
    'A_IMAGE', 'B_IMAGE', 'MAG_AUTO', 'FWHM_IMAGE', 'CLASS_STAR'
]
