from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.special import binom
from helpers import HarmonicSerie
from typing import List, Dict, Tuple, Union
import pandas as pd


class LissajousAnimated:
    def __init__(self) -> None:
        self.harmonic_serie = HarmonicSerie()

    def _get_time_array(self) -> np.ndarray:
        return np.linspace(0, 2*np.pi, 1000)

    def _get_time_series_dict(self, v: int) -> Dict[str, np.ndarray]:
        t = self._get_time_array()
        v_time_serie_y: np.ndarray = np.sin(v * t)
        v_time_serie_x: np.ndarray = np.cos(v * t)
        return {"t": t, "x": v_time_serie_x, "y": v_time_serie_y}

    def get_canvas(self) -> Tuple[plt.figure, plt.axes]:
        fig = plt.figure()
        ax = fig.add_subplot()
        plt.axis('off')
        return fig, ax

    def plot(self, v1, v2):
        data_1 = self._get_time_series_dict(v1)
        data_2 = self._get_time_series_dict(v2)
        fig, ax = self.get_canvas()

        def animate(i):
            if i == 0:
                x = np.array([])
                y = np.array([])
            x = np.append(x, data_1["x"][i])
            y = np.append(y, data_2["x"][i])
            ax.plot(x, y)
            ani = FuncAnimation(fig, animate, frames=len(data_1["t"]), interval=10, repeat=True)
            plt.show()
            stopme = 1


LissajousAnimated().plot(1, 2)
