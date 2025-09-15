import os

def run_shell_command(command, desc):
    print(f"[INFO] {desc} in progress...")
    exit_code = os.system(command)
    if exit_code != 0:
        print(f"[ERROR] {desc} failed.")
    else:
        print(f"[INFO] {desc} completed successfully.")

if __name__ == '__main__':
    # Step 1: Create and activate the Conda environment
    run_shell_command("conda env create -f environment.yml", "Creating Conda environment")
    run_shell_command("conda activate gausugar", "Activating Conda environment")

    # Step 2: Install submodules
    submodules = {
        "diff-gaussian-rasterization": "./gaussian_splatting/submodules/diff-gaussian-rasterization",
        "simple-knn": "./gaussian_splatting/submodules/simple-knn",
    }
    for name, path in submodules.items():
        os.chdir(path)
        run_shell_command("pip install -e .", f"Installing {name} submodule")
        os.chdir("../../../")

    # Step 3: Install Nvdiffrast
    run_shell_command("git clone https://github.com/NVlabs/nvdiffrast", "Downloading Nvdiffrast")
    os.chdir("nvdiffrast")
    run_shell_command("pip install .", "Installing Nvdiffrast")
    os.chdir("../")

    print("[INFO] Environment setup completed!")
