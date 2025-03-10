import numpy as np
from scipy.optimize import curve_fit

from .plots import plot_psf

class PSFFitter:
    def __init__(self, image, known_background, known_x0, known_y0):
        self.image = image
        self.known_background = known_background
        self.known_x0 = known_x0
        self.known_y0 = known_y0
        self.y, self.x = np.indices(image.shape)
        self.data = image.ravel()

    def moffat(self, x, y, alpha, beta):
        """Moffat's distribution function."""
        rr = (x - self.known_x0) ** 2 + (y - self.known_y0) ** 2
        return self.known_background + (alpha / ((1 + rr / beta ** 2)) ** 2)

    def gaussian(self, x, y, amplitude, sigma_x, sigma_y):
        """Gaussian distribution function."""
        return self.known_background + amplitude * np.exp(
            -(((x - self.known_x0) ** 2 / (2 * sigma_x ** 2)) + ((y - self.known_y0) ** 2 / (2 * sigma_y ** 2))))

    def fit_psf(self, psf_type='moffat'):
        """Fits a PSF (Moffat or Gaussian) profile to a star in an image."""
        xdata = np.vstack((self.x.ravel(), self.y.ravel()))

        if psf_type == 'moffat':
            params = np.array([0, 0])
            initial_guess = (self.image.max() - self.known_background, 2.5)
            # print('FITTING A MOFFAT DISTRIBUTION')
            # print('INITIAL GUESS :')
            # print(initial_guess)
            psf_func = lambda xy, a, b: self.moffat(xy[0], xy[1], a, b)
        elif psf_type == 'gaussian':
            params = np.array([0, 0, 0])
            initial_guess = (self.image.max() - self.known_background, 2, 2)
            # print('FITTING A GAUSSIAN DISTRIBUTION')
            # print('INITIAL GUESS :')
            # print(initial_guess)

            psf_func = lambda xy, a, b, c: self.gaussian(xy[0], xy[1], a, b, c)
        else:
            raise ValueError("Invalid PSF type. Choose 'moffat' or 'gaussian'.")

        try:
            params, _ = curve_fit(psf_func, xdata, self.data, p0=initial_guess)
        except:
            pass

        return params

def calc_PSF_scube(flux__lyx, centers_xy, sqr_cut=25, psf_function='gaussian', med_sqrt=True, save_plot=None):
    """ Calculate the PSF for stars in a data cube
        return: a masked array psf__bsxy shape:(bands, stars, x[0] or y[1]) or just the sqrt(x²+y²/2) median if median=True
        Zero means that was not able to compute the PSF, and it's masked.
        01/24
    """
    from astropy.stats import sigma_clipped_stats

    sky = []
    psf__bsxy = np.zeros(shape=(flux__lyx.shape[0], len(centers_xy), 2))
    # background noise levels
    for b in range(flux__lyx.shape[0]):
        mean, median, std = sigma_clipped_stats(flux__lyx[b, :200, :200])
        sky.append(mean)
    for i in range(len(centers_xy)):
        star_x, star_y = np.round(centers_xy[i]).astype(int)
        if (star_y - sqr_cut >= 0) & (star_x - sqr_cut >= 0):
            star_byx = flux__lyx[:, star_y - sqr_cut:star_y + sqr_cut + 1, star_x - sqr_cut:star_x + sqr_cut + 1]
            for b in range(flux__lyx.shape[0]):
                psf_fitter = PSFFitter(star_byx[b], sky[b], sqr_cut, sqr_cut)
                psf__bsxy[b, i, :] = psf_fitter.fit_psf(psf_type=psf_function)[1:] * 2.35
    psf__bsxy = np.ma.masked_where(psf__bsxy <= 0, psf__bsxy)
    psf__bsxy = np.ma.masked_where(psf__bsxy >= 7, psf__bsxy)

    if save_plot is not None:
        plot_psf(psf__bsxy, filename=save_plot)

    if med_sqrt:
        return np.sqrt((np.ma.median(psf__bsxy, axis=1)[:, 0]**2 + np.ma.median(psf__bsxy, axis=1)[:, 1]**2) / 2)
    else:
        return psf__bsxy