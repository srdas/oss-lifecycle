"""
#!/bin/bash
Code to collect all commits and related information for a list of repos
"""

import os

repo_list = [
    "dask/dask",
    "huggingface/transformers",
    "ipython/ipython",
    "jax-ml/jax",
    "jupyter-server/jupyter-scheduler",
    "jupyterlab/jupyter-ai",
    "jupyterlab/jupyterlab",
    "kubeflow/kubeflow",
    "kubernetes/kubernetes",
    "kubernetes-sigs/kueue",
    "langchain-ai/langchain-aws",
    "langchain-ai/langchain-google",
    "langchain-ai/langchain",
    "microsoft/DeepSpeed",
    "mlflow/mlflow",
    "numpy/numpy",
    "pandas-dev/pandas",
    "pytorch/pytorch",
    "ray-project/ray",
    "run-llama/llama_index",
    "scikit-learn/scikit-learn",
    "tensorflow/tensorflow",
    "vllm-project/vllm",
]

for repo in repo_list:
    print(f"Repo = {repo}")
    # os.system('python -m oss_lifecycle.github_gather ' + repo)
    os.system('python -m oss_lifecycle.github_gather_old ' + repo)
    print(repo, '..Done')
