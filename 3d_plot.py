from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.special import binom
from helpers import HarmonicSerie
from typing import List, Dict, Tuple, Union
import pandas as pd


class Lissajous3D:
    def __init__(self) -> None:
        self.harmonic_serie = HarmonicSerie()

    def _get_time_array(self) -> np.ndarray:
        return np.linspace(0, 2*np.pi, 1000)

    def _get_time_series_dict(self, v: int) -> Dict[str, np.ndarray]:
        t = self._get_time_array()
        v_time_serie_y: np.ndarray = np.sin(v * t)
        v_time_serie_x: np.ndarray = np.cos(v * t)
        return {"t": t, "x": v_time_serie_x, "y": v_time_serie_y}

    def _create_plot_canvas(self) -> Tuple[plt.figure, plt.axes]:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        plt.axis('off')
        return fig, ax

    def plot_sigle_3d_diagrams(self, *args):
        fig, ax = self._create_plot_canvas()
        for i, v in enumerate(args):
            data = self._get_time_series_dict(v)
            ax.plot(data["x"], data["y"], data["t"], color=f"C{i}")
            intersections_indexes = np.where(np.abs(data["x"]-data["y"]) < data["t"][1])[0]
            for index in intersections_indexes:
                ax.scatter(data["x"][index], data["y"][index], data["t"][index], color=f"C{i}")
        plt.show()


Lissajous3D().plot_sigle_3d_diagrams(2, 3)
