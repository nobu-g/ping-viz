import argparse
from typing import Dict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.axes import Axes
import seaborn as sns


def save(path: str):
    # pdfのフォントをTrueTypeに変更
    matplotlib.rcParams['pdf.fonttype'] = 42
    # defaultのdpi=100から変更
    matplotlib.rcParams['savefig.dpi'] = 300

    pdf = PdfPages(path)
    pdf.savefig()
    pdf.close()


def export_heatmap(data: Dict[str, Dict[str, float]], dest: str):
    # df = pd.read_csv(path)
    df = pd.DataFrame.from_dict(data, orient='index')
    # df = df.rdiv(0.025)
    df.sort_index(axis=0, inplace=True)
    df.sort_index(axis=1, inplace=True)

    # ヒートマップを出力
    print(df)
    plt.subplots(figsize=(20, 20))
    ax: Axes = sns.heatmap(
        df,
        fmt='1.3f',
        cmap='bwr',
        square=True,
        mask=df.isna())
    # ax: Axes = sns.heatmap(df, fmt='1.3f', cmap='bwr', cbar=False, square=True)
    ax.tick_params(labeltop=True, labelbottom=False)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    save(dest)
    # plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hosts', type=str, default=None,
                        help='hosts file path')
    parser.add_argument('--csv', type=str, default=None,
                        help='main data')
    parser.add_argument('--out', '-o', type=str, default=None,
                        help='output pdf path')
    args = parser.parse_args()

    with open(args.hosts) as f:
        hosts = [line.strip() for line in f]
    data = {src: {dst: np.nan for dst in hosts} for src in hosts}

    with open(args.csv) as f:
        for line in f:
            src, dst, min_, avg, max_, stddev = line.strip().split(',')
            data[src][dst] = float(avg)
    export_heatmap(data, args.out)


if __name__ == '__main__':
    main()
