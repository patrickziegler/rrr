__version__ = "0.1.2"

import matplotlib.pyplot as plt
import numpy as np

import argparse


def eval_plot(ask_c, vol_min=200, vol_max=2000, risk_max=250, rrr=2, margin=0.08, p=1, res=500, step=2):
    bid_d = ask_c * np.linspace(1 - margin, 1, res);
    vol = np.linspace(vol_min, vol_max, res);

    [vv, dd] = np.meshgrid(vol, bid_d)

    tt = vv*ask_c / (vv - 2*p)
    uu = rrr*(tt - dd) + tt

    rr = (ask_c - dd) * (vv - 2*p) / ask_c

    nn = np.floor(vv / ask_c)

    extent = [np.min(vv), np.max(vv), np.min(dd), np.max(dd)]

    cs = plt.contour(nn, levels=np.arange(0, vol_max / ask_c, step), extent=extent, linewidths=.8, colors="grey")
    plt.clabel(cs, cs.levels, inline=True, fmt=lambda x: "%.0f" % x)

    cs = plt.contour(uu, 20, extent=extent, linewidths=.8, colors="cyan")
    plt.clabel(cs, cs.levels, inline=True, fmt=lambda x: "%.2f" % x)

    cs = plt.contour(rr, levels=np.arange(0, risk_max, 5), extent=extent, linewidths=.8, colors="yellow")
    plt.clabel(cs, cs.levels, inline=True, fmt=lambda x: "%.2f" % x)

    plt.imshow(uu, extent=extent, origin="lower", alpha=1, aspect="auto")
    plt.colorbar()

    plt.title("Risk / return ratio eval (ask=%.2f, rrr=%s, p=%s)" % (ask_c, str(rrr), str(p)))

    plt.tight_layout()
    plt.show()


def get_args():
    parser = argparse.ArgumentParser(prog="rrr - Risk / return value order evaluation")
    parser.add_argument("--margin", default=0.08, type=float, help="Max. relative loss")
    parser.add_argument("-p", "--provision", default=1, type=float, help="Order provision")
    parser.add_argument("--step", default=2, type=int, help="Division step")
    parser.add_argument("--vmin", default=200, type=float, help="Order volume (min)")
    parser.add_argument("--vmax", default=2000, type=float, help="Order volume (max)")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(dest="ask", type=float, help="Current ask price")
    parser.add_argument(dest="rrr", default=2, type=float, nargs="?", help="Risk / return ratio")
    return parser.parse_args()


def main():
    args = get_args()
    kwargs = {
        "margin": args.margin,
        "rrr": args.rrr,
        "p": args.provision,
        "step": args.step,
        "vol_min": args.vmin,
        "vol_max": args.vmax,
    }
    eval_plot(args.ask, **kwargs)
