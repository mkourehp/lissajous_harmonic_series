from matplotlib import pyplot as plt
import numpy as np
from scipy.special import binom
from helpers import HarmonicSerie
from typing import List, Dict, Tuple


class Lissajous:
    def __init__(self) -> None:
        self.harmonic_serie = HarmonicSerie()

    def _get_time_array(self) -> np.ndarray:
        return np.linspace(0, 2*np.pi, 1000)

    def _get_freq_time_series(self, v1: int, v2: int) -> Dict[str, np.ndarray]:
        v1_time_serie: np.ndarray = np.sin(v1 * self._get_time_array())
        v2_time_serie: np.ndarray = np.sin(v2 * self._get_time_array())
        return {"v1": v1_time_serie, "v2": v2_time_serie}

    def _create_plot_canvas(self, x, y) -> Tuple[plt.figure, plt.axes]:
        fig, axes = plt.subplots(x, y, sharex=True, sharey=True)
        plt.subplots_adjust(wspace=0, hspace=0)
        fig.suptitle('Lissajous Diagrams for Harmonic Series', weight='bold')
        return fig, axes

    def _populate_canvas_1d(self, axes, highest_harmonic):
        [ax.xaxis.set_visible(False) for ax in axes]
        [ax.yaxis.set_visible(False) for ax in axes]
        axes_x_length, v1 = axes.shape[0], 1
        for x in range(axes_x_length):
            freq_time_series = self._get_freq_time_series(v1, v1 + x + 1)
            axes[x].plot(freq_time_series["v1"], freq_time_series["v2"], color="#D85A7FFF")
            axes[x].text(x=0.0, y=0.0, horizontalalignment='center',
                         verticalalignment='center', s=f"${v1}$ , ${v2}$", alpha=0.9, color="black")

    def _populate_canvas_2d(self, axes, highest_harmonic):
        [axx.axis("off") for ax in axes for axx in ax]
        # [axx.yaxis.set_visible(False) for ax in axes for axx in ax]

        def _check_loop(v1, v2):
            if v2 == highest_harmonic:
                v1 = v1 + 1
                v2 = v1 + 1
                print(7 * "-")
            else:
                v2 = v2 + 1
            return v1, v2

        axes_x_length, axes_y_length = axes.shape
        v1, v2 = 1, 2
        for x in range(axes_x_length):
            for y in range(axes_y_length):
                freq_time_series = self._get_freq_time_series(v1, v2)
                axes[x, y].plot(freq_time_series["v1"], freq_time_series["v2"], color="#D85A7FFF")
                axes[x, y].text(x=0.0, y=0.0, horizontalalignment='center',
                                verticalalignment='center', s=f"${v1}$ , ${v2}$", alpha=0.9, color="black")
                v1, v2 = _check_loop(v1, v2)
                if v1 == highest_harmonic:
                    break
                print(v1, v2)
            if v1 == highest_harmonic:
                break

    def plot_all_possible_diagrams(self, highest_harmonic: int):
        number_of_plots = int(binom(highest_harmonic, 2))
        square_length = int(np.sqrt(number_of_plots))
        canvas_size_x, canvas_size_y = square_length + 1, square_length
        canvas_size_y = canvas_size_y + 1 if canvas_size_x * canvas_size_y < number_of_plots else canvas_size_y
        fig, axes = self._create_plot_canvas(canvas_size_x, canvas_size_y)
        if len(axes.shape) == 1:
            self._populate_canvas_1d(axes, highest_harmonic)
        else:
            self._populate_canvas_2d(axes, highest_harmonic)
        plt.tight_layout()
        plt.show()
