import sys  # Import the sys module to access command-line arguments
import nbformat  # Import nbformat to work with Jupyter notebook files

def merge_notebooks(notebook1_path, notebook2_path, output_path):
    """ Function which appends one notebook to another """
    # Load the first notebook
    with open(notebook1_path, encoding="utf-8") as f:
        nb1 = nbformat.read(f, as_version=4)

    # Load the second notebook
    with open(notebook2_path, encoding="utf-8") as f:
        nb2 = nbformat.read(f, as_version=4)

    # Append the cells from the second notebook to the first notebook
    nb1.cells.extend(nb2.cells)

    # Save the merged notebook to the specified output path
    with open(output_path, 'w', encoding="utf-8") as f:
        nbformat.write(nb1, f)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python merge_notebooks.py <notebook1.ipynb> <notebook2.ipynb> <output.ipynb>")
    else:
        # Call the merge_notebooks function with the provided arguments
        merge_notebooks(sys.argv[1], sys.argv[2], sys.argv[3])
