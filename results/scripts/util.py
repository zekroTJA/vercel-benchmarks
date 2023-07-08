import pandas as pd
import matplotlib.pyplot as plt
import os


class Colors:
    GO = "#00ADD8"
    NODE = "#339933"
    PYTHON = "#3776AB"
    RUST = "#fc7b02"


def get_dataset(path):
    tables = [pd.read_csv(os.path.join(path, file), names=(
        'time', 'status', 'took')) for file in os.listdir(path)]
    return pd.DataFrame([t.iloc[:, 2] / 1_000_000 for t in tables]).T


def plot_dataset(dataset, **kwargs):
    std = dataset.std(1)
    median = dataset.median(1)
    plt.figure(figsize=(20, 7))
    plt.bar(range(0, len(median)), median, yerr=std,
            error_kw=dict(capsize=2, alpha=0.7), **kwargs)
    plt.show()


def plot_combined(dataset_go, dataset_node, dataset_python, dataset_rust,
                  trans=lambda x: x):
    median_go = trans(dataset_go.median(1)).mean()
    median_node = trans(dataset_node.median(1)).mean()
    median_python = trans(dataset_python.median(1)).mean()
    median_rust = trans(dataset_rust.median(1)).mean()

    quant90_go = trans(dataset_go.quantile(0.90, 1)).mean()
    quant90_node = trans(dataset_node.quantile(0.90, 1)).mean()
    quant90_python = trans(dataset_python.quantile(0.90, 1)).mean()
    quant90_rust = trans(dataset_rust.quantile(0.90, 1)).mean()

    quant95_go = trans(dataset_go.quantile(0.95, 1)).mean()
    quant95_node = trans(dataset_node.quantile(0.95, 1)).mean()
    quant95_python = trans(dataset_python.quantile(0.95, 1)).mean()
    quant95_rust = trans(dataset_rust.quantile(0.95, 1)).mean()

    quant99_go = trans(dataset_go.quantile(0.99, 1)).mean()
    quant99_node = trans(dataset_node.quantile(0.99, 1)).mean()
    quant99_python = trans(dataset_python.quantile(0.99, 1)).mean()
    quant99_rust = trans(dataset_rust.quantile(0.99, 1)).mean()

    std_go = trans(dataset_go.std(1)).mean()
    std_node = trans(dataset_node.std(1)).mean()
    std_python = trans(dataset_python.std(1)).mean()
    std_rust = trans(dataset_rust.std(1)).mean()

    labels = ("Go", "Node", "Python", "Rust")
    errors = (std_go, std_node, std_python, std_rust)
    colors = (Colors.GO, Colors.NODE, Colors.PYTHON, Colors.RUST)

    plt.bar(labels, (median_go, median_node, median_python, median_rust),
            yerr=errors, color=colors, error_kw=dict(capsize=5, alpha=0.7))
    plt.bar(labels, (quant90_go, quant90_node, quant90_python,
            quant90_rust), alpha=0.3, color=colors)
    plt.bar(labels, (quant95_go, quant95_node, quant95_python,
            quant95_rust), alpha=0.3, color=colors)
    plt.bar(labels, (quant99_go, quant99_node, quant99_python,
            quant99_rust), alpha=0.3, color=colors)
    plt.show()
