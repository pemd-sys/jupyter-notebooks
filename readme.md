# Various Jupyter notebooks for power electronics calculations

## Important instructions to run the jupyter notebooks

### Enable Mathjax to render latex equations

To do this first go to command line and generate the jupyter config file.

```
jupyter notebook --generate-config
```

In the .jupyter folder in your home directory find the jupyter_notebook_config.py file and uncomment the line below

```python
# c.NotebookApp.mathjax_url = ''
c.NotebookApp.enable_mathjax = True
```

### Enable Equation Numbering for latex

To enable the equation numbering in jupyter we have to install the nbextensions package. Run the following in the command prompt to install and enable the equation numbering option.

```
pip install jupyter_contrib_nbextensions

jupyter contrib nbextension install --user
jupyter nbextension enable equation-numbering/main
```

## Useful tips
use ctrl+k v to see preview of markdown files in vscode

### References
https://stackoverflow.com/questions/32625939/ipython-notebook-where-is-jupyter-notebook-config-py-in-mac

https://stackoverflow.com/questions/31965667/local-copy-of-mathjax-on-a-jupyter-notebook/32166264#32166264

https://linuxhint.com/use-latex-jupyter-notebook/

https://www.overleaf.com/learn/latex/Spacing_in_math_mode

https://stackoverflow.com/questions/12090472/how-do-i-center-an-image-in-the-readme-md-file-on-github

https://stackoverflow.com/questions/32370281/how-to-embed-image-or-picture-in-jupyter-notebook-either-from-a-local-machine-o

https://code.visualstudio.com/docs/datascience/jupyter-notebooks

https://docs.document360.com/docs/how-to-center-align-the-text-in-markdown

https://www.ibm.com/docs/en/watson-studio-local/1.2.3?topic=notebooks-markdown-jupyter-cheatsheet

https://stackoverflow.com/questions/41241984/equation-numbering-in-jupyter-notebooks

https://stackoverflow.com/questions/35916658/how-to-git-ignore-ipython-notebook-checkpoints-anywhere-in-repository

https://code.visualstudio.com/docs/languages/markdown
