import matplotlib as mpl
import seaborn as sb


def megaplot(x, y, data, ax, color, **kwargs):
    data = data.reset_index()

    lw = mpl.rcParams["lines.linewidth"] * 1.8
    markersize = np.pi * np.square(lw) * 2

    a = data.groupby(x)[y].mean().index.values
    b = data.groupby(x)[y].mean().values

    ax.plot(a, b, color=color, linewidth=lw)

    sb.regplot(x, y, x_estimator=np.mean, x_ci=68, data=data, fit_reg=False, color=color, ax=ax,
               scatter_kws={'s': markersize}, **kwargs)