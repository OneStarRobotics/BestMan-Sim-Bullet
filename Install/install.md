# Installation

## Install with conda (Linux)

### Basic Env

> ***Note**: This will only install the basic module. More functional modules will be continuously updated in the future.*




1. Pull the repository and update the submodule


```
git clone https://github.com/OneStarRobotics/BestMan-Sim-Bullet.git
cd BestMan-Sim-Bullet
cd Install
git clone https://github.com/starry521/third_party.git
```
><p >Please Download <a href="https://drive.google.com/drive/folders/1j73iejffo2SeBglY_Wjdo9-3MVpAdAGu?usp=sharing">the necessary compressed file</a> and decompressed them in the main folder this project. 



2. Run the following script to add the project to the PYTHON search path
```
chmod 777 pythonpath.sh
bash pythonpath.sh
source ~/.bashrc
```


3. Install ffmpeg to enable video record
```
sudo apt update && sudo apt install ffmpeg
```

4. Configure related libraries and links to support OpenGL rendering (If it already exists, skip this step.)
```
sudo apt update && sudo apt install -y libgl1-mesa-glx libglib2.0-0
sudo mkdir /usr/lib/dri
sudo ln -s /lib/x86_64-linux-gnu/dri/swrast_dri.so /usr/lib/dri/swrast_dri.so
```

5. Install gcc/g++ 9 (If it already exists, skip this step.)
```
sudo apt install -y build-essential gcc-9 g++-9
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 9
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 9
sudo update-alternatives --config gcc  # choice gcc-9
sudo update-alternatives --config g++  # choice g++-9

# Make sure gcc and g++ versions are consistent (conda enviroment don't install gcc to prevent problems caused by inconsistent versions)
gcc -v
g++ -v
```

6. Create basic conda environment

> **Note**: 
> - If you want to install for other python version, please change to **basic_env_pyxx.yaml** and install the right ompl library like **ompl-1.6.0-cpxx-cpxx-manylinux_2_28_x86_64.whl** in the third_party folder.
> - Next, we will take **Python 3.8 version** as an example for installation.

```
conda env create -f basic_env_py38.yaml
conda activate BestMan-Sim-Bullet
pip install -r requirements.txt
pip install third_party/ompl/ompl-1.6.0-cp38-cp38-manylinux_2_28_x86_64.whl
```

