from matplotlib import pyplot as plt
import numpy as np
from scipy.special import binom
from helpers import HarmonicSerie
from typing import List, Dict, Tuple


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return set(primfac)


def has_common_prime_factor(v1, v2):
    return True if primes(v1).intersection(primes(v2)) else False


class Lissajous:
    def __init__(self) -> None:
        self.harmonic_serie = HarmonicSerie()

    def _get_time_array(self) -> np.ndarray:
        return np.linspace(0, 2*np.pi, 1000)

    def _get_freq_time_series(self, v: int) -> Dict[str, np.ndarray]:
        t = self._get_time_array()
        v_time_serie: np.ndarray = np.sin(v * t)
        return {"y": v_time_serie, "t": t}

    def _create_2dplot_canvas(self, x, y) -> Tuple[plt.figure, plt.axes]:
        fig, axes = plt.subplots(x, y, sharex=True, sharey=True)
        if x*y >= 2:
            plt.subplots_adjust(wspace=0.1, hspace=0.1)
        else:
            axes = np.array([axes])
        return fig, axes

    def _populate_axis_interference(self, ax, v1, v2):
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        wave1, wave2 = self._get_freq_time_series(v1), self._get_freq_time_series(v2)
        ax.plot(wave1["t"], wave1["y"] + wave2["y"])
        ax.text(x=0.45, y=0.9, s=f"${v1}$ , ${v2}$", alpha=0.7, color="black", transform=ax.transAxes)

    def _populate_axis_lissajous(self, ax, v1, v2):
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        wave1, wave2 = self._get_freq_time_series(v1), self._get_freq_time_series(v2)
        ax.plot(wave1["y"], wave2["y"], c="C1")
        ax.text(x=0.45, y=0.9, s=f"${v1}$ , ${v2}$", alpha=0.7, color="black", transform=ax.transAxes)

    def _populate_canvas_2d_diff(self, highest_harmonic):
        def _check_loop(v1, v2):
            if v2 == highest_harmonic:
                v1 = v1 + 1
                v2 = v1 + 1
                print(7 * "-")
            else:
                v2 = v2 + 1
            return v1, v2

        v1, v2 = 1, 2
        prime_frequencies = [[v1, v2]]
        while True:
            v1, v2 = _check_loop(v1, v2)
            if has_common_prime_factor(v1, v2):
                continue
            if v1 == highest_harmonic:
                break
            prime_frequencies.append([v1, v2])
            print(v1, v2)
        self._plot_subplots(prime_frequencies)

    def _plot_subplots(self, v_pairs: List[List[int]]):
        canvas_size_x, canvas_size_y = self._get_subplot_shape(len(v_pairs))
        fig_1, axes_1 = self._create_2dplot_canvas(canvas_size_x, canvas_size_y)
        fig_2, axes_2 = self._create_2dplot_canvas(canvas_size_x, canvas_size_y)
        if len(axes_1.shape) == 2:
            axes_1 = axes_1.reshape(axes_1.shape[0] * axes_1.shape[1])
            axes_2 = axes_2.reshape(axes_2.shape[0] * axes_2.shape[1])
        for ax_1, ax_2, v in zip(axes_1, axes_2, v_pairs):
            self._populate_axis_interference(ax_1, v[0], v[1])
            self._populate_axis_lissajous(ax_2, v[0], v[1])
        fig_1.tight_layout()
        fig_2.tight_layout()

    def _get_subplot_shape(self, number_of_plots: int):
        square_length = int(np.sqrt(number_of_plots))
        canvas_size_x, canvas_size_y = square_length, square_length
        canvas_size_y = canvas_size_y + 1 if canvas_size_x * canvas_size_y < number_of_plots else canvas_size_y
        return canvas_size_x, canvas_size_y

    def plot_all_differences(self, highest_harmonic: int):
        self._populate_canvas_2d_diff(highest_harmonic)
        plt.show()


Lissajous().plot_all_differences(10)
