# My Experiments with Computer Vision Using Python

### Installation of opencv3 with python3 support on macOS Sierra 10.12
> Installation through traditional make build failed due to QT library issues on Sierra
However homebrew installation was successful using the following options

```bash
$ brew reinstall opencv3 --with-python3 --with-ffmpeg --with-tbb --with-contrib
```

> After the build the shared object representing the python bindings needs to be linked from the PYTHONPATH location as follows.

```bash
$ cd /usr/local/lib/python3.5/site-packages
$ ln -s /usr/local/Cellar/opencv3/HEAD-6328076_4/lib/python3.5/site-packages/cv2.cpython-35m-darwin.so cv2.so
```

Some random exrcises for image and vision handling using `Python`.

> Following are some of the major python bindings and libraries required for opencv3 build and used here

- `opencv 3.x.x`
- `mahootas`
- `numpy`
- `matplotlib`
- `scipy`
- `scikitlearn`
