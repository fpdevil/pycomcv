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

# list the required dylib packages
#
λ pkg-config --cflags --libs /usr/local/opt/opencv3/lib/pkgconfig/opencv.pc
-I/usr/local/Cellar/opencv3/3.2.0/include/opencv -I/usr/local/Cellar/opencv3/3.2.0/include -L/usr/local/Cellar/opencv3/3.2.0/lib -lopencv_stitching -lopencv_superres -lopencv_videostab -lopencv_aruco -lopencv_bgsegm -lopencv_bioinspired -lopencv_ccalib -lopencv_dpm -lopencv_fuzzy -lopencv_line_descriptor -lopencv_optflow -lopencv_reg -lopencv_saliency -lopencv_stereo -lopencv_structured_light -lopencv_phase_unwrapping -lopencv_rgbd -lopencv_surface_matching -lopencv_tracking -lopencv_datasets -lopencv_text -lopencv_face -lopencv_plot -lopencv_dnn -lopencv_xfeatures2d -lopencv_shape -lopencv_video -lopencv_ximgproc -lopencv_calib3d -lopencv_features2d -lopencv_flann -lopencv_xobjdetect -lopencv_objdetect -lopencv_ml -lopencv_xphoto -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_photo -lopencv_imgproc -lopencv_core
```

Some random exrcises for image and vision handling using `Python`.

> Following are some of the major python bindings and libraries required for opencv3 build and used here

- `opencv 3.x.x`
- `mahootas`
- `numpy`
- `matplotlib`
- `scipy`
- `scikitlearn`
